# Domain 2 · 생성형 AI 기초 (Fundamentals of Generative AI)

**비중**: 24% · **문항 수**: 96

## Task Statements

| Task | 주제 | 파일 | 문항 수 |
|------|------|------|---------|
| **2.1** | 생성형 AI 기본 개념 (Basic concepts of generative AI) | [`2.1-genai-concepts.md`](2.1-genai-concepts.md) | 32 |
| **2.2** | GenAI 역량·한계와 비즈니스 적용 | [`2.2-capabilities-limitations.md`](2.2-capabilities-limitations.md) | 32 |
| **2.3** | AWS GenAI 인프라·기술 | [`2.3-aws-infrastructure.md`](2.3-aws-infrastructure.md) | 32 |

## Task 2.1 포함 개념
- 파운데이션 모델의 정의·특성·라이프사이클
- 프롬프트 유형: Zero/One/Few-shot, Chain-of-Thought, Prompt Template/Tuning, In-context Learning
- 추론 파라미터: Temperature, Top-K, Top-P, Response length, Penalties, Stop sequences
- 생성형 AI 모델 종류: Transformer, GAN, VAE, Diffusion, RNN, Flow-based
- Amazon Bedrock 개요: 모델 선택, Titan, Knowledge Bases, Agents, Guardrails, PartyRock
- GenAI 성능 지표: ROUGE, BLEU, GLUE, HELM, MMLU, BIG-bench

## Task 2.2 포함 개념
- GenAI 적합/부적합 유즈 케이스
- GenAI의 한계(환각·비결정성·최신 지식 부재·비용·데이터 프라이버시)
- 비즈니스 ROI, 성공 지표, 컴플라이언스 고려
- Human-in-the-loop, 검증 전략

## Task 2.3 포함 개념
- Bedrock vs SageMaker JumpStart vs 커스텀 모델 결정
- On-Demand vs Provisioned Throughput
- Serverless 아키텍처, 스케일링
- Bedrock API, IAM, PrivateLink, VPC endpoints
- Knowledge Base + 벡터 DB(OpenSearch, Aurora pgvector, etc.) 조합
