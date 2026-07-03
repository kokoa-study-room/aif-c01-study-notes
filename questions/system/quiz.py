#!/usr/bin/env python3
"""
quiz.py — AIF-C01 대화형 퀴즈 실행기.

사용법:
    python questions/system/quiz.py                    # 랜덤 전체 문제
    python questions/system/quiz.py --domain 1         # 도메인 1만
    python questions/system/quiz.py --task 1.1         # 태스크 1.1만
    python questions/system/quiz.py --wrong-only       # 오답만 재풀이
    python questions/system/quiz.py --unseen           # 미풀이 문항만
    python questions/system/quiz.py --limit 10         # 세션당 문항 수
    python questions/system/quiz.py --lang bilingual   # bilingual | en | kr
    python questions/system/quiz.py --stats            # 진도 통계만 표시
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK_PATH = ROOT / "system" / "bank.json"
PROGRESS_PATH = ROOT / "system" / "progress.json"
WRONG_LOG_PATH = ROOT / "system" / "wrong-log.md"

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


@dataclass
class Progress:
    seen: dict[str, dict]

    @classmethod
    def load(cls) -> "Progress":
        if PROGRESS_PATH.exists():
            data = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
            return cls(seen=data.get("seen", {}))
        return cls(seen={})

    def save(self) -> None:
        PROGRESS_PATH.write_text(
            json.dumps({"seen": self.seen}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def record(self, qid: str, correct: bool) -> None:
        entry = self.seen.setdefault(qid, {"attempts": 0, "correct": 0, "last": None, "last_result": None})
        entry["attempts"] += 1
        if correct:
            entry["correct"] += 1
        entry["last"] = datetime.now(timezone.utc).isoformat()
        entry["last_result"] = "correct" if correct else "wrong"

    def is_wrong_last(self, qid: str) -> bool:
        entry = self.seen.get(qid)
        return bool(entry and entry.get("last_result") == "wrong")

    def is_unseen(self, qid: str) -> bool:
        return qid not in self.seen


def load_bank() -> list[dict]:
    if not BANK_PATH.exists():
        print(f"{RED}❌ bank.json 이 없습니다. 먼저 `python questions/system/build_bank.py` 를 실행하세요.{RESET}")
        sys.exit(1)
    return json.loads(BANK_PATH.read_text(encoding="utf-8"))


def apply_filters(bank: list[dict], progress: Progress, args) -> list[dict]:
    filtered = bank
    if args.domain:
        filtered = [q for q in filtered if q.get("domain") == args.domain]
    if args.task:
        filtered = [q for q in filtered if q.get("task") == args.task]
    if args.wrong_only:
        filtered = [q for q in filtered if progress.is_wrong_last(q["id"])]
    if args.unseen:
        filtered = [q for q in filtered if progress.is_unseen(q["id"])]
    return filtered


def render_question(q: dict, lang: str) -> None:
    print()
    print(f"{BOLD}{CYAN}=== {q['id']} · Domain {q['domain']} · Task {q['task']} · [{q['difficulty']}] ==={RESET}")
    if lang in ("bilingual", "kr"):
        print(f"\n{BOLD}🇰🇷 문제{RESET}\n{q['question_kr']}")
    if lang in ("bilingual", "en"):
        print(f"\n{BOLD}🇺🇸 Question{RESET}\n{q['question_en']}")
    print(f"\n{BOLD}보기 / Options{RESET}")
    for opt in q["options"]:
        if lang == "kr":
            print(f"  {BOLD}{opt['key']}.{RESET} {opt['kr']}")
        elif lang == "en":
            print(f"  {BOLD}{opt['key']}.{RESET} {opt['en']}")
        else:
            print(f"  {BOLD}{opt['key']}.{RESET} {opt['en']}")
            print(f"     {DIM}└ {opt['kr']}{RESET}")


def prompt_answer(q: dict) -> list[str]:
    valid_keys = {opt["key"] for opt in q["options"]}
    if q.get("type") == "multiple":
        hint = "(복수 선택 · 쉼표 또는 공백 구분, 예: A,C)"
    else:
        hint = "(단일 선택)"
    while True:
        raw = input(f"\n{YELLOW}답 입력 {hint} · 'q'=종료 · 's'=스킵 > {RESET}").strip().upper()
        if raw in {"Q", "QUIT", "EXIT"}:
            return ["__QUIT__"]
        if raw in {"S", "SKIP"}:
            return ["__SKIP__"]
        raw_letters = [c for c in raw.replace(",", " ").split() if c]
        if not raw_letters:
            continue
        if all(letter in valid_keys for letter in raw_letters):
            return raw_letters
        print(f"{RED}유효한 보기 키를 입력하세요 ({', '.join(sorted(valid_keys))}).{RESET}")


def show_result(q: dict, user: list[str], correct: list[str]) -> bool:
    ok = sorted(user) == sorted(correct)
    if ok:
        print(f"\n{GREEN}✅ 정답! (Correct: {', '.join(correct)}){RESET}")
    else:
        print(f"\n{RED}❌ 오답. 정답: {', '.join(correct)} / 제출: {', '.join(user)}{RESET}")

    print(f"\n{BOLD}💡 해설 / Explanation{RESET}")
    print(f"{DIM}[한글]{RESET}")
    print(q["explanation_kr"])
    print(f"\n{DIM}[English]{RESET}")
    print(q["explanation_en"])

    if q.get("related"):
        print(f"\n{BOLD}🔗 관련 개념 / Related{RESET}")
        for rel in q["related"]:
            print(f"  • {rel['label']} → {rel['path']}")
    return ok


def append_wrong_log(q: dict, user: list[str]) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    entry = (
        f"\n---\n"
        f"### {q['id']} · {ts}\n"
        f"- Domain {q['domain']} · Task {q['task']} · [{q['difficulty']}]\n"
        f"- 제출: `{','.join(user)}` / 정답: `{','.join(q['answer'])}`\n"
        f"- 태그: {', '.join(q.get('tags', []))}\n"
        f"- 관련: " + ", ".join(f"[{r['label']}]({r['path']})" for r in q.get("related", []))
        + "\n"
    )
    if not WRONG_LOG_PATH.exists():
        WRONG_LOG_PATH.write_text("# 오답 노트 (Wrong Answer Log)\n", encoding="utf-8")
    with WRONG_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(entry)


def print_stats(bank: list[dict], progress: Progress) -> None:
    total = len(bank)
    seen = sum(1 for q in bank if q["id"] in progress.seen)
    correct_last = sum(1 for q in bank if progress.seen.get(q["id"], {}).get("last_result") == "correct")

    print(f"\n{BOLD}=== AIF-C01 학습 진도 ==={RESET}")
    print(f"전체 진도: {BOLD}{seen}/{total}{RESET} ({100*seen/total:.1f}%)" if total else "빈 문제 은행")
    if seen:
        print(f"정답률(최근):   {BOLD}{100*correct_last/seen:.1f}%{RESET} ({correct_last}/{seen})")

    for d in sorted({q.get("domain") for q in bank if q.get("domain") is not None}):
        dbank = [q for q in bank if q.get("domain") == d]
        dseen = [q for q in dbank if q["id"] in progress.seen]
        dcorrect = [q for q in dseen if progress.seen[q["id"]].get("last_result") == "correct"]
        rate = f"{100*len(dcorrect)/len(dseen):.0f}%" if dseen else "—"
        print(f"  Domain {d}: {len(dseen)}/{len(dbank)} · 최근 정답률 {rate}")


def main() -> int:
    ap = argparse.ArgumentParser(description="AIF-C01 대화형 퀴즈")
    ap.add_argument("--domain", type=int)
    ap.add_argument("--task", type=str)
    ap.add_argument("--wrong-only", action="store_true")
    ap.add_argument("--unseen", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--lang", choices=["bilingual", "en", "kr"], default="bilingual")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--order", choices=["random", "sequential"], default="random")
    args = ap.parse_args()

    bank = load_bank()
    progress = Progress.load()

    if args.stats:
        print_stats(bank, progress)
        return 0

    pool = apply_filters(bank, progress, args)
    if not pool:
        print(f"{YELLOW}필터 조건에 맞는 문제가 없습니다.{RESET}")
        return 0

    if args.order == "random":
        random.shuffle(pool)
    if args.limit:
        pool = pool[: args.limit]

    session_correct = 0
    session_total = 0
    for q in pool:
        render_question(q, args.lang)
        user = prompt_answer(q)
        if user == ["__QUIT__"]:
            break
        if user == ["__SKIP__"]:
            print(f"{DIM}스킵 — 진도에 기록되지 않음.{RESET}")
            continue
        correct = show_result(q, user, q["answer"])
        progress.record(q["id"], correct)
        if not correct:
            append_wrong_log(q, user)
        session_total += 1
        if correct:
            session_correct += 1

    progress.save()

    if session_total:
        print(f"\n{BOLD}세션 결과:{RESET} {session_correct}/{session_total} "
              f"({100*session_correct/session_total:.1f}%)")
    print_stats(bank, progress)
    return 0


if __name__ == "__main__":
    sys.exit(main())
