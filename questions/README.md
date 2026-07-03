# AIF-C01 문제 은행 (Question Bank)

> **⚠️ 저작권 안내 / Copyright Notice**
> 이 문제 은행의 모든 문항은 **[공식 AWS AIF-C01 Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Exam-Guide.pdf)의 공개된 도메인·태스크 명세**를 기반으로, AWS 공개 문서를 참고하여 **새롭게 작성된 학습용 문항**입니다. AWS 시험 문제나 덤프의 재현물이 아닙니다.
>
> All questions in this bank are **originally authored** for learning purposes, based on the **publicly available domain and task statements** in the [Official AWS AIF-C01 Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Exam-Guide.pdf) and AWS public documentation. These are not reproductions of actual exam questions or dumps.

---

## 목표 (Goal)

- **총 400문항**, 한/영 이중언어, 실전 스타일 시나리오 기반 학습용 문제 은행
- 각 문항은 [메인 README.md](../README.md)의 관련 개념과 링크로 연결되어, 문제 → 개념 복습 흐름을 매끄럽게 만듦
- 오답 노트, 진도 추적, 도메인별 정오답 통계 지원

## 도메인 배분 (Domain Distribution)

공식 Exam Guide의 도메인 비중을 그대로 반영합니다.

| 도메인 | 비중 | 문항 수 | 디렉토리 |
|--------|------|---------|----------|
| **Domain 1**: AI/ML 기초 (Fundamentals of AI and ML) | 20% | **80** | [`domain-1-fundamentals-of-ai-ml/`](domain-1-fundamentals-of-ai-ml/) |
| **Domain 2**: 생성형 AI 기초 (Fundamentals of Generative AI) | 24% | **96** | [`domain-2-fundamentals-of-genai/`](domain-2-fundamentals-of-genai/) |
| **Domain 3**: 파운데이션 모델 응용 (Applications of Foundation Models) | 28% | **112** | [`domain-3-applications-of-foundation-models/`](domain-3-applications-of-foundation-models/) |
| **Domain 4**: 책임 있는 AI (Guidelines for Responsible AI) | 14% | **56** | [`domain-4-responsible-ai/`](domain-4-responsible-ai/) |
| **Domain 5**: 보안/컴플라이언스/거버넌스 (Security, Compliance, Governance) | 14% | **56** | [`domain-5-security-compliance-governance/`](domain-5-security-compliance-governance/) |
| **합계** | 100% | **400** | |

## 태스크 스테이트먼트별 세부 배분 (Task Statement Breakdown)

### Domain 1: Fundamentals of AI and ML (80문항)
- **1.1** Explain basic AI concepts and terminologies — 30문항
- **1.2** Identify practical use cases for AI — 25문항
- **1.3** Describe the ML development lifecycle — 25문항

### Domain 2: Fundamentals of Generative AI (96문항)
- **2.1** Explain the basic concepts of generative AI — 32문항
- **2.2** Understand capabilities and limitations of GenAI for business — 32문항
- **2.3** Describe AWS infrastructure and technologies for GenAI apps — 32문항

### Domain 3: Applications of Foundation Models (112문항)
- **3.1** Design considerations for FM-based applications — 28문항
- **3.2** Effective prompt engineering techniques — 28문항
- **3.3** Training and fine-tuning process for FMs — 28문항
- **3.4** Methods to evaluate FM performance — 28문항

### Domain 4: Guidelines for Responsible AI (56문항)
- **4.1** Development of responsible AI systems — 28문항
- **4.2** Importance of transparent and explainable models — 28문항

### Domain 5: Security, Compliance, and Governance (56문항)
- **5.1** Methods to secure AI systems — 28문항
- **5.2** Governance and compliance regulations for AI — 28문항

## 문항 스키마 (Question Schema)

문항 형식과 필드 정의는 [SCHEMA.md](SCHEMA.md) 참고.

## 학습 시스템 사용법 (Study System Usage)

📖 **전체 사용 매뉴얼**: [`MANUAL.md`](MANUAL.md) — 빠른 시작, 명령어 옵션, 학습 전략, FAQ, 트러블슈팅

시스템 개발자 참조 문서: [`system/README.md`](system/README.md)

## 생성 진행 상황 (Generation Progress)

| Domain | Task | 생성 완료 | 목표 | 상태 |
|--------|------|-----------|------|------|
| 1 | 1.1 | 30 | 30 | ✅ 완료 |
| 1 | 1.2 | 25 | 25 | ✅ 완료 |
| 1 | 1.3 | 25 | 25 | ✅ 완료 |
| 2 | 2.1 | 32 | 32 | ✅ 완료 |
| 2 | 2.2 | 32 | 32 | ✅ 완료 |
| 2 | 2.3 | 32 | 32 | ✅ 완료 |
| 3 | 3.1 | 28 | 28 | ✅ 완료 |
| 3 | 3.2 | 28 | 28 | ✅ 완료 |
| 3 | 3.3 | 28 | 28 | ✅ 완료 |
| 3 | 3.4 | 28 | 28 | ✅ 완료 |
| 4 | 4.1 | 28 | 28 | ✅ 완료 |
| 4 | 4.2 | 28 | 28 | ✅ 완료 |
| 5 | 5.1 | 28 | 28 | ✅ 완료 |
| 5 | 5.2 | 28 | 28 | ✅ 완료 |
| **합계** | | **400** | **400** | **🎉 100%** |

### 정답 분포 (최종 400문항 기준)
- **A: 102 (25.5%)** · **B: 99 (24.75%)** · **C: 100 (25.0%)** · **D: 98 (24.5%)** · 복수정답(A,C): 1
- **완벽한 균등 분포** (편차 < 1%)
- Domain 1 (80): A=20, B=19, C=22, D=18, (A,C)=1
- Domain 2 (96): A=B=C=D=24 완전 균등
- Domain 3 (112): A=29, B=28, C=27, D=28
- Domain 4 (56): A=15, B=14, C=13, D=14
- Domain 5 (56): A=14, B=14, C=14, D=14

> **다음 배치 요청 방법**: "다음 배치" 또는 "Domain 2 시작" 같이 요청하시면 이어서 작성합니다.
