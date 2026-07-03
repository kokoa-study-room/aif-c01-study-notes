# AIF-C01 학습 시스템 사용 매뉴얼

> **AWS Certified AI Practitioner (AIF-C01) 400문항 이중언어 문제 은행**
>
> 이 문서는 문제 은행과 대화형 퀴즈 시스템 사용법을 처음부터 끝까지 안내합니다.

---

## 📑 목차

1. [시스템 개요](#1-시스템-개요)
2. [요구 사항](#2-요구-사항)
3. [빠른 시작 (3분)](#3-빠른-시작-3분)
4. [파일 구조](#4-파일-구조)
5. [`quiz.py` 상세 사용법](#5-quizpy-상세-사용법)
6. [`build_bank.py` 사용법](#6-build_bankpy-사용법)
7. [진도 관리](#7-진도-관리)
8. [오답 노트 활용](#8-오답-노트-활용)
9. [학습 전략](#9-학습-전략)
10. [문항 편집·추가](#10-문항-편집추가)
11. [자주 묻는 질문 (FAQ)](#11-자주-묻는-질문-faq)
12. [트러블슈팅](#12-트러블슈팅)

---

## 1. 시스템 개요

### 무엇을 제공하나요?

- **400문항** — 공식 [AIF-C01 Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Exam-Guide.pdf)의 도메인·태스크 비중을 그대로 반영한 이중언어(한/영) 학습용 문제 은행
- **대화형 퀴즈 러너** — 필터·랜덤화·언어 전환·통계를 지원하는 CLI 학습 도구
- **자동 진도 추적** — 문항별 풀이 횟수·최근 정답 여부·최근 시각 자동 기록
- **오답 노트 자동 축적** — 틀린 문항이 자동으로 마크다운 노트에 append
- **README 딥링크** — 모든 문항이 [메인 학습 노트 `README.md`](../README.md)의 관련 개념으로 연결

### 설계 원칙

| 원칙 | 구현 |
|------|------|
| 이중언어 | 문제·보기·정답·해설 모두 한/영 병기 |
| 실전 스타일 | 시나리오 기반 4지선다 (일부 복수정답) |
| 균등 정답 분포 | A~D 편차 < 1% (사실상 완벽 균등) |
| 재현성 | 마크다운(사람 편집용) → JSON(스크립트 소비용) 파이프라인, 검증 자동화 |
| 개념 연결 | 각 문항이 최소 1개 이상의 [메인 README](../README.md) 섹션과 링크 |

### 시스템 아키텍처

```
사용자 학습 흐름:
┌─────────────────────────────────────────────────────────────┐
│  1. 마크다운 문항 편집 (선택, 문항 추가·수정 시)              │
│     └─→ domain-X/X.Y-*.md                                    │
│  2. 빌드 (선택)                                              │
│     └─→ python3 system/build_bank.py                         │
│         └─→ system/bank.json 생성 + 무결성 검증               │
│  3. 학습                                                     │
│     └─→ python3 system/quiz.py [옵션]                        │
│         ├─→ 진도 자동 저장 (system/progress.json)             │
│         └─→ 오답 자동 append (system/wrong-log.md)            │
│  4. 통계 확인                                                │
│     └─→ python3 system/quiz.py --stats                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. 요구 사항

| 항목 | 요구 사항 |
|------|-----------|
| **Python** | 3.9 이상 (표준 라이브러리만 사용 — 외부 의존성 **없음**) |
| **OS** | macOS / Linux (Windows는 WSL 권장) |
| **터미널** | ANSI 컬러 지원 (기본 iTerm2, Terminal, gnome-terminal 등) |
| **저장 공간** | ~2MB (전체 문제 은행 + 시스템) |

Python 버전 확인:
```bash
python3 --version
# Python 3.9.x 이상이 출력되면 OK
```

---

## 3. 빠른 시작 (3분)

저장소가 이미 있다는 전제 하에:

```bash
# 1) 저장소 루트로 이동
cd /Users/koa/002-Study/aif-c01-study-notes

# 2) 문제 은행 인덱스 빌드 (첫 실행 시 1회 필요)
python3 questions/system/build_bank.py
# → ✅ Built 400 questions → questions/system/bank.json

# 3) 퀴즈 시작 (전체 400문항 랜덤)
python3 questions/system/quiz.py

# 4) 세션 중 특수 키
#    - 'q' 입력: 퀴즈 종료 (진도는 저장됨)
#    - 's' 입력: 현재 문항 스킵 (진도에 기록 안 됨)
```

**첫 세션 추천 설정**: 10문항 정도로 시스템에 익숙해지기
```bash
python3 questions/system/quiz.py --limit 10 --lang bilingual
```

---

## 4. 파일 구조

```
questions/
├── MANUAL.md                                     ⬅️ 이 문서
├── README.md                                     # 400문항 전체 인덱스 + 진도표
├── SCHEMA.md                                     # 문항 형식 명세
│
├── domain-1-fundamentals-of-ai-ml/               # AI/ML 기초 (20%, 80문항)
│   ├── README.md
│   ├── 1.1-ai-concepts.md                        # Q001~Q030
│   ├── 1.2-use-cases.md                          # Q031~Q055
│   └── 1.3-ml-lifecycle.md                       # Q056~Q080
│
├── domain-2-fundamentals-of-genai/               # GenAI 기초 (24%, 96문항)
│   ├── README.md
│   ├── 2.1-genai-concepts.md                     # Q081~Q112
│   ├── 2.2-capabilities-limitations.md           # Q113~Q144
│   └── 2.3-aws-infrastructure.md                 # Q145~Q176
│
├── domain-3-applications-of-foundation-models/   # FM 응용 (28%, 112문항)
│   ├── README.md
│   ├── 3.1-design-considerations.md              # Q177~Q204
│   ├── 3.2-prompt-engineering.md                 # Q205~Q232
│   ├── 3.3-training-fine-tuning.md               # Q233~Q260
│   └── 3.4-evaluation.md                         # Q261~Q288
│
├── domain-4-responsible-ai/                      # 책임있는 AI (14%, 56문항)
│   ├── README.md
│   ├── 4.1-responsible-development.md            # Q289~Q316
│   └── 4.2-transparency-explainability.md        # Q317~Q344
│
├── domain-5-security-compliance-governance/      # 보안·거버넌스 (14%, 56문항)
│   ├── README.md
│   ├── 5.1-security.md                           # Q345~Q372
│   └── 5.2-governance-compliance.md              # Q373~Q400
│
└── system/                                       # 학습 시스템
    ├── README.md                                 # 시스템 개발자 참조 문서
    ├── build_bank.py                             # 빌더 (마크다운 → JSON)
    ├── quiz.py                                   # 대화형 퀴즈 러너
    ├── progress.json                             # 진도 상태 (자동 갱신)
    ├── wrong-log.md                              # 오답 노트 (자동 append)
    └── bank.json                                 # 빌드 산출물 (재생성 가능)
```

### 파일별 목적

| 파일 | 언제 손대나요? | 자동 갱신? |
|------|-----------------|-----------|
| `*.md` (문항 파일) | 문항 추가/수정할 때만 | ❌ 수동 |
| `bank.json` | 절대 손대지 마세요 | ✅ `build_bank.py` 실행 시 |
| `progress.json` | 진도 초기화하고 싶을 때 | ✅ 퀴즈 실행 시 |
| `wrong-log.md` | 오답 복습 시 읽기 | ✅ 오답 발생 시 append |

---

## 5. `quiz.py` 상세 사용법

### 5.1 기본 실행

```bash
python3 questions/system/quiz.py
```

옵션 없이 실행하면 **전체 400문항을 랜덤 순서로** 풀이합니다. `q` 입력 시 종료.

### 5.2 명령어 옵션 전체 목록

| 옵션 | 값 | 설명 | 예시 |
|------|-----|------|------|
| `--domain` | 1~5 | 특정 도메인만 | `--domain 3` |
| `--task` | 예: `1.1`, `3.2` | 특정 태스크만 | `--task 3.2` |
| `--wrong-only` | (없음) | 최근 오답만 재풀이 | `--wrong-only` |
| `--unseen` | (없음) | 아직 풀지 않은 문항만 | `--unseen` |
| `--limit` | 정수 | 세션당 최대 문항 수 | `--limit 20` |
| `--lang` | `bilingual` / `en` / `kr` | 표시 언어 | `--lang kr` |
| `--order` | `random` / `sequential` | 문항 순서 | `--order sequential` |
| `--stats` | (없음) | 통계만 표시 후 종료 | `--stats` |

### 5.3 옵션 조합 예시

```bash
# 예 1) Domain 3 (28% 비중 최대) 10문항 한글만
python3 questions/system/quiz.py --domain 3 --limit 10 --lang kr

# 예 2) 프롬프트 엔지니어링 (Task 3.2)만 순차 풀이
python3 questions/system/quiz.py --task 3.2 --order sequential

# 예 3) 미풀이 문항 5개만 랜덤 (매일 조금씩 진도)
python3 questions/system/quiz.py --unseen --limit 5

# 예 4) 오답 재풀이 (완전 정복)
python3 questions/system/quiz.py --wrong-only

# 예 5) 시험 직전 모의고사 (실제 시험 65문항)
python3 questions/system/quiz.py --limit 65 --order random --lang bilingual

# 예 6) 통계만 빠르게 확인
python3 questions/system/quiz.py --stats
```

### 5.4 대화형 세션 흐름

```
=== Q123 · Domain 2 · Task 2.2 · [medium] ===

🇰🇷 문제
[한글 문제 내용]

🇺🇸 Question
[영문 문제 내용]

보기 / Options
  A. [영문 보기 A]
     └ [한글 보기 A]
  B. [영문 보기 B]
     └ [한글 보기 B]
  C. [영문 보기 C]
     └ [한글 보기 C]
  D. [영문 보기 D]
     └ [한글 보기 D]

답 입력 (단일 선택) · 'q'=종료 · 's'=스킵 > B

✅ 정답! (Correct: B)

💡 해설 / Explanation
[한글]
[한글 해설]

[English]
[영문 해설]

🔗 관련 개념 / Related
  • 환각 (Hallucinations) → ../../README.md#L161
  • Bedrock Knowledge Bases → ../../README.md#L1016
```

### 5.5 입력 방식

| 상황 | 입력 |
|------|------|
| 단일 선택 문항 | `A`, `B`, `C`, 또는 `D` |
| 복수 선택 문항 (`type: multiple`) | 쉼표 또는 공백 구분: `A,C` 또는 `A C` |
| 세션 종료 | `q` (또는 `quit`, `exit`) |
| 현재 문항 스킵 | `s` (또는 `skip`) — 진도에 기록 안 됨 |
| 유효하지 않은 입력 | 재입력 요청 (반복 안전) |

### 5.6 세션 종료 후 표시

```
세션 결과: 8/10 (80.0%)

=== AIF-C01 학습 진도 ===
전체 진도: 47/400 (11.8%)
정답률(최근):   72.3% (34/47)
  Domain 1: 15/80 · 최근 정답률 80%
  Domain 2: 12/96 · 최근 정답률 75%
  Domain 3: 20/112 · 최근 정답률 65%
  ...
```

---

## 6. `build_bank.py` 사용법

### 언제 실행하나요?

- **처음 저장소를 클론한 후 1회** (bank.json 최초 생성)
- **문항 파일(`*.md`)을 수정·추가한 뒤**
- **오류 메시지가 나오면** 문항 스키마 위반 진단용

### 실행 방법

```bash
python3 questions/system/build_bank.py
```

### 정상 출력

```
✅ Built 400 questions → questions/system/bank.json
```

### 검증 실패 시 출력

```
❌ 3 validation error(s):
  [domain-3-.../3.2-prompt-engineering.md] Q210: missing field: question_kr
  [domain-3-.../3.2-prompt-engineering.md] Q215: duplicate id
  [domain-4-.../4.1-....md] Q290: at least one Related Concepts link required
```

이런 오류가 나오면:
1. 지목된 파일의 지목된 Q번호로 이동
2. [`SCHEMA.md`](SCHEMA.md) 확인
3. 필수 필드 채우고 다시 빌드

### 빌더가 검증하는 것

- ✅ 모든 `id`가 Q001~Q400 범위에서 **고유**한지
- ✅ 각 문항에 `question_en`, `question_kr`, `options`, `answer`, `explanation` 모두 존재하는지
- ✅ `related` 링크가 최소 1개 이상인지
- ✅ 옵션이 최소 2개 이상인지

---

## 7. 진도 관리

### 진도는 어디에 저장되나요?

`questions/system/progress.json` — 문항별로 다음이 기록됩니다:

```json
{
  "seen": {
    "Q001": {
      "attempts": 3,           // 총 풀이 횟수
      "correct": 2,            // 총 정답 횟수
      "last": "2026-07-03T12:34:56+00:00",  // 마지막 풀이 시각
      "last_result": "correct" // "correct" 또는 "wrong"
    },
    "Q002": { ... }
  }
}
```

### 진도 확인

```bash
python3 questions/system/quiz.py --stats
```

### 진도 초기화

전체 진도를 처음부터 다시 시작하고 싶다면:

```bash
# 방법 1) 백업 후 재생성
cp questions/system/progress.json questions/system/progress.backup.json
echo '{"seen": {}}' > questions/system/progress.json

# 방법 2) 그냥 파일 삭제 (다음 실행 시 자동 재생성)
rm questions/system/progress.json
```

### 특정 도메인만 초기화 (고급)

Python으로 원하는 도메인의 문항만 진도에서 제거:

```bash
python3 -c "
import json
p = json.load(open('questions/system/progress.json'))
# Domain 3 문항(Q177~Q288)만 진도에서 제거
p['seen'] = {k: v for k, v in p['seen'].items() if not ('Q177' <= k <= 'Q288')}
json.dump(p, open('questions/system/progress.json', 'w'), indent=2)
print('Domain 3 진도 초기화 완료')
"
```

---

## 8. 오답 노트 활용

### 자동 기록

오답이 발생하면 자동으로 [`questions/system/wrong-log.md`](system/wrong-log.md)에 append됩니다:

```markdown
### Q145 · 2026-07-03T12:34:56+00:00
- Domain 2 · Task 2.3 · [medium]
- 제출: `A` / 정답: `D`
- 태그: bedrock-vs-jumpstart, decision
- 관련: [Amazon Bedrock](../../README.md#L997)
```

### 오답만 재풀이

```bash
python3 questions/system/quiz.py --wrong-only
```

**동작 방식**: `progress.json`에서 `last_result == "wrong"`인 문항만 필터링해서 랜덤 풀이. 정답 처리하면 자동으로 오답 리스트에서 빠집니다.

### 오답 노트 초기화

```bash
# 오답 로그 초기화 (헤더만 남기고 비우기)
echo "# 오답 노트 (Wrong Answer Log)

> \`quiz.py\`가 오답을 자동으로 이곳에 append합니다." > questions/system/wrong-log.md
```

### 오답 노트를 다른 도구로 활용

`wrong-log.md`는 표준 마크다운이므로:
- **Notion**에 붙여넣어 태그별 정리
- **Anki**로 옮겨 간격 반복 학습 카드로 변환
- **Obsidian**에서 그래프 뷰로 개념 연결 시각화

---

## 9. 학습 전략

### 9.1 시험 대비 커리큘럼 (권장, 2주 계획)

| 일차 | 학습 내용 | 명령어 |
|------|----------|--------|
| **1~2일** | Domain 1 (AI/ML 기초, 80문항) 전 범위 1회독 | `--domain 1 --order sequential` |
| **3~4일** | Domain 2 (GenAI 기초, 96문항) 1회독 | `--domain 2 --order sequential` |
| **5~7일** | Domain 3 (FM 응용, 112문항, 최대 비중) 1회독 | `--domain 3 --order sequential` |
| **8일** | Domain 4 (책임있는 AI, 56문항) 1회독 | `--domain 4 --order sequential` |
| **9일** | Domain 5 (보안·거버넌스, 56문항) 1회독 | `--domain 5 --order sequential` |
| **10일** | 오답 전면 재풀이 | `--wrong-only` |
| **11일** | 모의고사 65문항 세션 × 2회 | `--limit 65 --order random` |
| **12일** | 오답 재풀이 + 낮은 도메인 재학습 | `--wrong-only`, `--domain N` |
| **13일** | 모의고사 65문항 × 2회 (실전 시뮬레이션) | `--limit 65` |
| **14일** | 시험 전날: [메인 README.md](../README.md)의 Study Sheets 표 리뷰 | (문서 리뷰) |

### 9.2 매일 30분 학습 (직장인/학생용)

```bash
# 아침 15분: 새 문항 5개
python3 questions/system/quiz.py --unseen --limit 5

# 저녁 15분: 오답 재풀이 5개
python3 questions/system/quiz.py --wrong-only --limit 5
```

400문항을 하루 5개씩 풀면 약 80일. 오답 반복까지 포함하면 ~3개월 마스터 코스.

### 9.3 도메인별 집중 학습 (약점 보완)

```bash
# 통계로 낮은 정답률 도메인 확인
python3 questions/system/quiz.py --stats

# 약점 도메인 집중 (예: Domain 4가 65%로 낮으면)
python3 questions/system/quiz.py --domain 4 --limit 15 --lang kr

# 약점 태스크 집중 (예: 프롬프트 엔지니어링)
python3 questions/system/quiz.py --task 3.2 --limit 10
```

### 9.4 시험 직전 최종 점검 (D-1)

```bash
# 1) 전체 통계 확인
python3 questions/system/quiz.py --stats

# 2) 오답 전면 재풀이
python3 questions/system/quiz.py --wrong-only

# 3) 실전 모의고사 65문항 (실제 시험과 동일 규모)
python3 questions/system/quiz.py --limit 65 --order random --lang bilingual

# 4) 낮은 도메인 최종 리뷰
python3 questions/system/quiz.py --domain 3 --limit 10  # 최대 비중 도메인
```

### 9.5 언어 모드 선택 가이드

| 상황 | 권장 언어 |
|------|-----------|
| 첫 학습 (개념 이해 우선) | `--lang bilingual` (한/영 병기) |
| 개념 완성 후 실전 대비 | `--lang en` (실제 시험과 동일) |
| 급하게 한글로 개념만 훑기 | `--lang kr` (한글만) |
| 영어 어휘 부담 없이 이해 | `--lang bilingual` |

---

## 10. 문항 편집·추가

### 10.1 기존 문항 수정

1. 해당 태스크 파일 열기 (예: `domain-3-.../3.2-prompt-engineering.md`)
2. `Q번호`로 검색 → 필요한 부분 수정
3. 저장 후 빌드:
   ```bash
   python3 questions/system/build_bank.py
   ```

### 10.2 새 문항 추가

문항 형식은 [`SCHEMA.md`](SCHEMA.md)에 정의되어 있습니다. 최소 구조:

```markdown
---
id: Q401
domain: 3
task: 3.2
difficulty: medium
type: single
tags: [prompt-engineering, custom-tag]
---

## Q401

### 🇺🇸 Question (English)
[영문 시나리오 질문]

### 🇰🇷 문제 (한글)
[한글 시나리오 질문]

### Options / 보기
- **A.** [영문 보기 A]
  - 한글: [한글 보기 A]
- **B.** [영문 보기 B]
  - 한글: [한글 보기 B]
- **C.** [영문 보기 C]
  - 한글: [한글 보기 C]
- **D.** [영문 보기 D]
  - 한글: [한글 보기 D]

### ✅ Correct Answer / 정답
**B**

### 💡 Explanation / 해설

**English**:
[영문 해설 - 왜 B가 정답이고 A, C, D가 오답인지]

**한글**:
[한글 해설]

### 🔗 Related Concepts / 관련 개념
- [관련 개념 이름](../../README.md#L앵커)

---
```

### 10.3 필수 규칙

- ✅ `id`는 **전역 고유** (기존 문항과 중복 금지)
- ✅ `difficulty`: `easy` / `medium` / `hard` 중 하나
- ✅ `type`: `single` (단일 정답) 또는 `multiple` (복수 정답)
- ✅ 옵션은 **최소 2개**, 각 옵션에 한/영 모두 포함
- ✅ `Correct Answer`는 옵션 키(`A`, `B` 등)만 사용. 복수 정답은 `A, C` 형식
- ✅ `Related Concepts` 링크 **최소 1개** 필수
- ✅ 문항 간 구분자 `---` (마크다운 hr) 필수

### 10.4 검증

수정·추가 후 반드시 빌드로 검증:

```bash
python3 questions/system/build_bank.py
# ✅ Built N questions → questions/system/bank.json
```

오류가 나면 어느 파일 어느 Q번호에서 어떤 필드가 문제인지 정확히 알려줍니다.

---

## 11. 자주 묻는 질문 (FAQ)

<details>
<summary><b>Q. 400문항을 언제까지 다 풀어야 하나요?</b></summary>

시험 대비 기간에 따라 다릅니다:
- **2주 벼락치기**: [권장 커리큘럼](#91-시험-대비-커리큘럼-권장-2주-계획) 참조
- **1개월 여유**: 하루 15문항 + 주말 오답 재풀이
- **3개월 마스터**: 하루 5문항 + 매일 오답 5문항

핵심은 **1회독보다 오답 재풀이가 2~3배 중요**합니다.
</details>

<details>
<summary><b>Q. 정답률이 몇 %면 시험 준비된 건가요?</b></summary>

경험적 가이드:
- **전체 정답률 80% 이상** + **각 도메인 75% 이상** → 실전 준비 완료
- **전체 70~80%** → 오답 재풀이 1~2회 추가 권장
- **60~70%** → 취약 도메인 집중 학습 필요
- **60% 미만** → 문항 풀이 전 [메인 README](../README.md) 학습부터

문제 은행이 실제 시험보다 다소 어렵게 구성되어 있으므로, 80% 정도면 실전에서는 여유가 있는 편입니다.
</details>

<details>
<summary><b>Q. 한글로만 학습해도 되나요?</b></summary>

**초기 학습에는 한글 위주도 OK**이지만, 실제 시험은 영어(또는 부정확한 한국어 번역)로 출제됩니다. 다음 순서를 권장합니다:

1. **1회독**: `--lang kr` 또는 `--lang bilingual`로 개념 이해
2. **2회독**: `--lang bilingual`로 영어 표현에 익숙해지기
3. **모의고사**: `--lang en`으로 실전 감각 훈련

특히 **영문 용어**(예: "context window", "grounding", "provisioned throughput" 등)는 반드시 원문으로 기억해 두세요.
</details>

<details>
<summary><b>Q. `bank.json`을 직접 편집해도 되나요?</b></summary>

**절대 안 됩니다.** `bank.json`은 마크다운 파일에서 자동 생성되는 산출물입니다. 직접 편집해도:
- 다음 `build_bank.py` 실행 시 덮어씌워짐
- 마크다운과 동기화가 깨져 이후 편집이 혼란스러워짐

문항 수정은 **반드시 `.md` 파일**에서 하고 `build_bank.py`로 빌드하세요.
</details>

<details>
<summary><b>Q. Windows에서도 쓸 수 있나요?</b></summary>

가능합니다:
- **WSL2 (권장)**: Ubuntu 등에서 macOS/Linux와 동일하게 사용
- **PowerShell**: `python3` → `python`으로 바꾸면 대부분 동작. ANSI 컬러는 Windows Terminal에서 정상 출력
- **cmd.exe**: 컬러가 깨질 수 있지만 기능은 동작

Windows에서 컬러가 이상하면:
```powershell
# Windows Terminal 사용 권장
python quiz.py
```
</details>

<details>
<summary><b>Q. 오답 노트가 너무 길어졌어요.</b></summary>

`wrong-log.md`는 시간 순으로 append만 되므로 길어지는 게 정상입니다. 정리하려면:

```bash
# 초기화
echo "# 오답 노트" > questions/system/wrong-log.md

# 또는 백업 후 초기화
mv questions/system/wrong-log.md questions/system/wrong-log-$(date +%Y%m%d).md
echo "# 오답 노트" > questions/system/wrong-log.md
```

오답 **재풀이**는 로그 파일이 아닌 `progress.json` 기반이므로 로그를 지워도 재풀이는 정상 동작합니다.
</details>

<details>
<summary><b>Q. 문항이 실제 시험과 얼마나 비슷한가요?</b></summary>

이 문제 은행은 **공식 [AIF-C01 Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Exam-Guide.pdf)의 공개된 도메인·태스크 명세**를 기반으로 새로 작성된 학습용 문항입니다. AWS 시험 문제나 덤프의 재현물이 아닙니다.

- ✅ **개념 커버리지**: 공식 시험 목표(Task Statements)를 모두 반영
- ✅ **문항 스타일**: 실전 시나리오 기반 4지선다
- ✅ **난이도**: 실제 시험보다 약간 어렵게 설계 (여유 마진 확보)
- ⚠️ **정확히 같은 문항**은 아닙니다 (그래서도 안 되고 그럴 필요도 없음)

목적은 **개념 이해와 유즈 케이스 매칭 훈련**이며, 이 은행에서 80%를 편안하게 넘기면 실전에서 여유롭게 통과할 확률이 높습니다.
</details>

<details>
<summary><b>Q. 시험 등록·응시 관련 정보는 어디서?</b></summary>

이 저장소는 학습 자료만 제공합니다. 등록·응시는:
- [공식 시험 페이지 (AWS Certification)](https://aws.amazon.com/certification/certified-ai-practitioner/)
- [Pearson VUE 예약](https://home.pearsonvue.com/aws) (온라인 감독 또는 시험장)

시험료·재응시 정책·유효 기간 등은 AWS 공식 페이지를 확인하세요.
</details>

---

## 12. 트러블슈팅

### 12.1 `bank.json 이 없습니다` 오류

```
❌ bank.json 이 없습니다. 먼저 `python questions/system/build_bank.py` 를 실행하세요.
```

**해결**:
```bash
python3 questions/system/build_bank.py
```

### 12.2 `python3: command not found` (macOS/Linux)

Python 3을 설치하거나, 실제 명령어 이름을 확인:
```bash
python --version    # 3.x 이면 python 사용
python3 --version   # 3.x 이면 python3 사용
```

macOS에서 Python 3 설치:
```bash
# Homebrew 사용
brew install python@3.12
```

### 12.3 컬러가 이상하게 표시됨

```
[1m[36m=== Q001 ...[0m
```

터미널이 ANSI 컬러 이스케이프를 처리 못 하는 경우입니다.
- **macOS Terminal**: 기본 지원
- **iTerm2**: 기본 지원
- **VS Code 통합 터미널**: 기본 지원
- **Windows cmd**: Windows Terminal로 변경 권장

임시 방편으로 컬러 비활성화(패치 필요):
```python
# quiz.py 상단의 RESET = "\033[0m" 등 모든 색상 상수를 ""로 변경
```

### 12.4 문항이 필터에 안 잡혀요

```
필터 조건에 맞는 문제가 없습니다.
```

원인별 해결:
| 원인 | 해결 |
|------|------|
| `--wrong-only`인데 오답이 없음 | 정상. 완벽 상태 축하합니다 |
| `--unseen`인데 모두 풀었음 | 정상. `--stats`로 100% 확인 |
| `--task 3.5` 같은 존재하지 않는 태스크 | 유효 태스크는 `1.1`~`5.2` |
| `--domain 6` | 유효 도메인은 `1`~`5` |
| 문항 파일 편집 후 아직 빌드 안 함 | `python3 questions/system/build_bank.py` |

### 12.5 진도가 저장 안 됨

**증상**: 종료 후 재실행하면 통계가 0으로 리셋

**원인**:
1. `system/` 디렉토리 쓰기 권한 없음 → `chmod +w questions/system/`
2. `q` 없이 강제 종료(Ctrl+C) → 세션 도중 종료는 저장 안 됨. 반드시 `q` 입력
3. 스킵(`s`)한 문항은 진도에 기록되지 않는 게 **의도된 동작**

### 12.6 빌드 오류 대응 표

| 오류 메시지 | 원인 | 해결 |
|------------|------|------|
| `missing field: question_kr` | 한글 문제 섹션 없음 | 해당 Q에 `### 🇰🇷 문제 (한글)` 섹션 추가 |
| `duplicate id` | 같은 Q번호 중복 | 새 Q번호로 변경 |
| `options must have at least 2 entries` | 보기 <2개 또는 형식 오류 | 옵션 형식이 `- **A.** ...`인지 확인 |
| `at least one Related Concepts link required` | 관련 개념 링크 없음 | `- [이름](../../README.md#L앵커)` 최소 1개 추가 |
| `KeyError: 'answer'` | 정답 파싱 실패 | `### ✅ Correct Answer / 정답\n**A**` 형식 준수 |

---

## 📚 관련 문서

- [메인 학습 노트 (한/영 이중언어 README)](../README.md) — AIF-C01 전 범위 개념 정리
- [문항 은행 개요 (`questions/README.md`)](README.md) — 도메인·태스크 배분과 진도표
- [문항 스키마 (`SCHEMA.md`)](SCHEMA.md) — 새 문항 작성 시 반드시 참조
- [시스템 개발자 문서 (`system/README.md`)](system/README.md) — 스크립트 내부 참조

## 🎯 학습 성공 팁 (요약)

1. **1회독보다 오답 재풀이가 중요** — `--wrong-only` 반복 활용
2. **개념→문항→개념 순환** — 오답 발생 시 반드시 README 딥링크 클릭하여 개념 재확인
3. **매일 조금씩** — 벼락치기보다 하루 15문항 × 2~4주가 훨씬 효과적
4. **모의고사 실전 감각** — 시험 직전 `--limit 65 --lang en` 최소 3회
5. **취약 도메인 집중** — `--stats`로 낮은 도메인 발견하면 `--domain N`으로 파고들기
6. **영문 용어 암기** — 실제 시험은 영어. 개념 매핑을 원문 용어로 익힐 것

건투를 빕니다! 🚀
