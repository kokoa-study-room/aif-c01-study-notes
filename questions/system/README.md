# 학습 시스템 (Study System)

문제 은행을 대화형 퀴즈로 실행하고, 진도·오답을 추적하는 도구 모음입니다.

## 요구 사항 (Requirements)

- Python 3.9+ (표준 라이브러리만 사용 — 외부 의존성 없음)
- macOS/Linux 터미널 (ANSI 컬러 지원)

## 파일 구성

| 파일 | 역할 |
|------|------|
| [`quiz.py`](quiz.py) | 대화형 퀴즈 실행기 (한/영 전환, 랜덤·순차·오답 재풀이 모드) |
| [`build_bank.py`](build_bank.py) | 마크다운 문항을 `bank.json`으로 통합 |
| [`progress.json`](progress.json) | 문항별 학습 상태 (풀이 횟수, 최근 정오답, 마지막 시각) |
| [`wrong-log.md`](wrong-log.md) | 오답 노트 (자동 append) |
| `bank.json` | 스크립트가 소비하는 통합 문항 데이터 (커밋 대상 아님) |

## 사용법 (Usage)

### 1. 문항 인덱스 빌드

마크다운 파일을 편집하거나 새 배치가 추가된 뒤 실행합니다:

```bash
python questions/system/build_bank.py
```

### 2. 퀴즈 실행

```bash
# 전체 문항 랜덤
python questions/system/quiz.py

# 특정 도메인만
python questions/system/quiz.py --domain 1

# 특정 태스크만
python questions/system/quiz.py --task 1.1

# 오답만 재풀이
python questions/system/quiz.py --wrong-only

# 미풀이 문항만
python questions/system/quiz.py --unseen

# 한 세션 문항 수 제한
python questions/system/quiz.py --limit 10

# 언어 모드: bilingual(기본) | en | kr
python questions/system/quiz.py --lang bilingual
```

### 3. 진도 확인

```bash
python questions/system/quiz.py --stats
```

출력 예시:
```
=== AIF-C01 학습 진도 ===
전체 진도: 45/400 (11.3%)
정답률:   72% (32/45)

도메인별:
  Domain 1: 20/80 (25%) — 정답률 80%
  Domain 2: 15/96 (16%) — 정답률 67%
  ...
```

## 문항 편집 워크플로

1. `domain-X-.../X.Y-....md` 파일 편집 (문항 추가/수정)
2. `python questions/system/build_bank.py` 실행 → `bank.json` 재생성
3. `python questions/system/quiz.py --task X.Y --unseen`로 새 문항만 풀이

## 파이프라인 무결성 (Integrity)

`build_bank.py`는 다음을 검증합니다:
- 모든 `id`가 Q001~Q400 범위에서 **고유**한지
- 각 문항에 `question_en`, `question_kr`, `options`, `answer`, `explanation` 모두 존재하는지
- `related` 링크가 최소 1개 이상인지
- 도메인/태스크 조합이 유효한지

실패 시 어느 파일 어느 문항에서 실패했는지 정확히 리포트합니다.
