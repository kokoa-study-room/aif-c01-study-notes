# 문항 스키마 (Question Schema)

## 파일 형식

각 태스크 스테이트먼트별로 하나의 마크다운 파일에 여러 문항을 담습니다.
- 예: `domain-1-fundamentals-of-ai-ml/1.1-ai-concepts.md`

## 문항 필수 필드

### 마크다운 표현 (사람이 읽는 용도)

```markdown
---
id: Q001
domain: 1
task: 1.1
difficulty: easy | medium | hard
type: single | multiple
tags: [foundation-models, bedrock, ...]
---

## Q001

### 🇺🇸 Question (English)
[영어 원문 시나리오]

### 🇰🇷 문제 (한글)
[한글 번역 시나리오]

### Options / 보기
- **A.** [EN option A]
  - 한글: [KR option A]
- **B.** [EN option B]
  - 한글: [KR option B]
- **C.** [EN option C]
  - 한글: [KR option C]
- **D.** [EN option D]
  - 한글: [KR option D]

### ✅ Correct Answer / 정답
**A**

### 💡 Explanation / 해설

**English**:
[영어 해설: 왜 A가 정답이고 B, C, D가 오답인지 각각 설명]

**한글**:
[한글 해설: 동일한 내용을 한글로]

### 🔗 Related Concepts / 관련 개념
- [README - 관련 섹션 이름](../../README.md#앵커)

---
```

## 필드 설명

| 필드 | 필수 | 설명 |
|------|------|------|
| `id` | ✅ | Q001~Q400 (전역 고유 번호) |
| `domain` | ✅ | 1~5 |
| `task` | ✅ | 1.1, 1.2, ..., 5.2 |
| `difficulty` | ✅ | `easy`(기초 용어), `medium`(개념 응용), `hard`(다중 서비스 시나리오) |
| `type` | ✅ | `single`(단일 정답), `multiple`(복수 정답, e.g. "다음 중 2개 선택") |
| `tags` | ✅ | 태그 배열 - 필터링·검색용 |
| Question EN | ✅ | 시나리오 기반 실전 스타일 영어 원문 |
| 문제 한글 | ✅ | 자연스러운 한글 번역 |
| Options | ✅ | 4지선다(A~D) 또는 5지선다(A~E), 한/영 모두 |
| Correct Answer | ✅ | 정답 문자 |
| Explanation | ✅ | 정답 근거 + 오답 이유(각 보기별) 한/영 |
| Related Concepts | ✅ | README.md의 관련 섹션 링크 (최소 1개) |

## 난이도 기준

- **easy**: 용어 정의, 서비스 매칭 등 기초 사실 확인
  - 예: "OCR을 담당하는 AWS 서비스는?"
- **medium**: 개념 이해와 적용 필요
  - 예: "환각을 줄이려는 팀에 가장 적합한 방법은?"
- **hard**: 여러 서비스·개념을 결합한 실전 시나리오
  - 예: "실시간 예측 + 비용 최적화 + 낮은 지연 요구 시 SageMaker 배포 방식은?"

## 태그 규칙

일관성을 위해 미리 정의된 태그를 사용합니다:

**서비스 태그**: `bedrock`, `sagemaker`, `comprehend`, `rekognition`, `textract`, `polly`, `lex`, `transcribe`, `translate`, `kendra`, `personalize`, `forecast`, `q-business`, `glue`, `s3`, `macie`

**개념 태그**: `foundation-models`, `rag`, `fine-tuning`, `prompt-engineering`, `embeddings`, `hallucinations`, `vector-db`, `ml-pipeline`, `hyperparameters`, `metrics`, `overfitting`, `responsible-ai`, `bias`, `explainability`, `security`, `iam`, `compliance`, `governance`

**시험 스타일 태그**: `scenario`, `service-matching`, `terminology`, `troubleshooting`, `best-practice`

## JSON 미러 (스크립트 소비용)

퀴즈 스크립트가 소비하는 [`system/bank.json`](system/bank.json)에는 동일 데이터가 다음 스키마로 저장됩니다:

```json
{
  "id": "Q001",
  "domain": 1,
  "task": "1.1",
  "difficulty": "easy",
  "type": "single",
  "tags": ["terminology", "foundation-models"],
  "question_en": "...",
  "question_kr": "...",
  "options": [
    {"key": "A", "en": "...", "kr": "..."},
    {"key": "B", "en": "...", "kr": "..."},
    {"key": "C", "en": "...", "kr": "..."},
    {"key": "D", "en": "...", "kr": "..."}
  ],
  "answer": ["A"],
  "explanation_en": "...",
  "explanation_kr": "...",
  "related": [
    {"label": "General AI", "path": "../../README.md#L64"}
  ],
  "source_file": "domain-1-fundamentals-of-ai-ml/1.1-ai-concepts.md"
}
```

마크다운을 편집한 뒤 `python system/build_bank.py`로 JSON을 재생성합니다.
