#!/usr/bin/env python3
"""
build_bank.py — 마크다운 문항 파일을 통합 JSON으로 빌드.

사용법:
    python questions/system/build_bank.py

동작:
    - questions/domain-*/**/*.md 의 모든 문항 파싱
    - id 중복, 필수 필드 누락 검증
    - questions/system/bank.json 생성
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
BANK_PATH = ROOT / "system" / "bank.json"

QUESTION_BLOCK = re.compile(
    r"^---\s*$(?P<meta>.*?)^---\s*$(?P<body>.*?)(?=^---\s*$|\Z)",
    re.MULTILINE | re.DOTALL,
)


@dataclass
class ValidationError:
    file: str
    qid: str
    message: str


@dataclass
class BuildReport:
    parsed: int = 0
    errors: list[ValidationError] = field(default_factory=list)

    def fail(self, file: str, qid: str, msg: str) -> None:
        self.errors.append(ValidationError(file, qid, msg))


def parse_meta(meta_text: str) -> dict[str, Any]:
    """단순 YAML 프론트매터 파서 (외부 의존성 회피)."""
    result: dict[str, Any] = {}
    for line in meta_text.strip().splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            items = [x.strip().strip("'\"") for x in raw[1:-1].split(",") if x.strip()]
            result[key] = items
        elif raw in {"true", "false"}:
            result[key] = raw == "true"
        else:
            try:
                result[key] = int(raw)
            except ValueError:
                result[key] = raw.strip("'\"")
    return result


def parse_body(body: str) -> dict[str, Any]:
    parsed: dict[str, Any] = {}

    def grab(header: str, until: list[str]) -> str:
        pattern = rf"###\s*{re.escape(header)}\s*\n(.*?)(?=###\s+(?:{'|'.join(re.escape(u) for u in until)})|\Z)"
        m = re.search(pattern, body, re.DOTALL)
        return m.group(1).strip() if m else ""

    sections = ["🇺🇸 Question (English)", "🇰🇷 문제 (한글)", "Options / 보기",
                "✅ Correct Answer / 정답", "💡 Explanation / 해설", "🔗 Related Concepts / 관련 개념"]

    parsed["question_en"] = grab(sections[0], sections[1:])
    parsed["question_kr"] = grab(sections[1], sections[2:])
    options_raw = grab(sections[2], sections[3:])
    answer_raw = grab(sections[3], sections[4:])
    explanation_raw = grab(sections[4], sections[5:])
    related_raw = grab(sections[5], [])

    parsed["options"] = parse_options(options_raw)
    parsed["answer"] = parse_answer(answer_raw)
    parsed["explanation_en"], parsed["explanation_kr"] = parse_explanation(explanation_raw)
    parsed["related"] = parse_related(related_raw)

    return parsed


def parse_options(text: str) -> list[dict[str, str]]:
    opts: list[dict[str, str]] = []
    for m in re.finditer(
        r"-\s*\*\*(?P<key>[A-E])\.\*\*\s*(?P<en>.+?)(?:\n\s*-\s*한글:\s*(?P<kr>.+?))?(?=\n-\s*\*\*[A-E]\.\*\*|\Z)",
        text,
        re.DOTALL,
    ):
        opts.append({
            "key": m.group("key"),
            "en": m.group("en").strip(),
            "kr": (m.group("kr") or "").strip(),
        })
    return opts


def parse_answer(text: str) -> list[str]:
    hits = re.findall(r"\b([A-E])\b", text)
    seen: list[str] = []
    for h in hits:
        if h not in seen:
            seen.append(h)
    return seen


def parse_explanation(text: str) -> tuple[str, str]:
    en_match = re.search(r"\*\*English\*\*\s*:?\s*\n(.*?)(?=\*\*한글\*\*|\Z)", text, re.DOTALL)
    kr_match = re.search(r"\*\*한글\*\*\s*:?\s*\n(.*?)\Z", text, re.DOTALL)
    return (
        en_match.group(1).strip() if en_match else "",
        kr_match.group(1).strip() if kr_match else "",
    )


def parse_related(text: str) -> list[dict[str, str]]:
    rel: list[dict[str, str]] = []
    for m in re.finditer(r"-\s*\[(?P<label>[^\]]+)\]\((?P<path>[^)]+)\)", text):
        rel.append({"label": m.group("label"), "path": m.group("path")})
    return rel


def validate(qid: str, data: dict[str, Any], src: str, report: BuildReport) -> bool:
    ok = True
    required = ["question_en", "question_kr", "options", "answer", "explanation_en", "explanation_kr"]
    for f in required:
        if not data.get(f):
            report.fail(src, qid, f"missing field: {f}")
            ok = False
    if data.get("options") and len(data["options"]) < 2:
        report.fail(src, qid, "options must have at least 2 entries")
        ok = False
    if not data.get("related"):
        report.fail(src, qid, "at least one Related Concepts link required")
        ok = False
    return ok


def build() -> int:
    report = BuildReport()
    bank: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    md_files = sorted(ROOT.glob("domain-*/**/*.md"))
    for md in md_files:
        text = md.read_text(encoding="utf-8")
        for m in QUESTION_BLOCK.finditer(text):
            meta = parse_meta(m.group("meta"))
            qid = str(meta.get("id", "")).strip()
            if not qid:
                continue  # 파일 헤더 프론트매터일 수 있음 — 스킵
            if qid in seen_ids:
                report.fail(str(md), qid, "duplicate id")
                continue
            seen_ids.add(qid)

            body = parse_body(m.group("body"))
            entry = {
                "id": qid,
                "domain": meta.get("domain"),
                "task": meta.get("task"),
                "difficulty": meta.get("difficulty"),
                "type": meta.get("type"),
                "tags": meta.get("tags", []),
                "source_file": str(md.relative_to(ROOT.parent)),
                **body,
            }
            if validate(qid, entry, str(md), report):
                bank.append(entry)
                report.parsed += 1

    if report.errors:
        print(f"❌ {len(report.errors)} validation error(s):", file=sys.stderr)
        for e in report.errors:
            print(f"  [{e.file}] {e.qid}: {e.message}", file=sys.stderr)
        return 1

    bank.sort(key=lambda x: x["id"])
    BANK_PATH.write_text(json.dumps(bank, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Built {report.parsed} questions → {BANK_PATH.relative_to(ROOT.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(build())
