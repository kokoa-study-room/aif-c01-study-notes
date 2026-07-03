# Domain 3 · 파운데이션 모델 응용 (Applications of Foundation Models)

**비중**: 28% (최대) · **문항 수**: 112

## Task Statements

| Task | 주제 | 파일 | 문항 수 |
|------|------|------|---------|
| **3.1** | FM 애플리케이션 설계 고려사항 | [`3.1-design-considerations.md`](3.1-design-considerations.md) | 28 |
| **3.2** | 효과적 프롬프트 엔지니어링 | [`3.2-prompt-engineering.md`](3.2-prompt-engineering.md) | 28 |
| **3.3** | FM 학습·파인튜닝 프로세스 | [`3.3-training-fine-tuning.md`](3.3-training-fine-tuning.md) | 28 |
| **3.4** | FM 성능 평가 방법 | [`3.4-evaluation.md`](3.4-evaluation.md) | 28 |

## Task 3.1 포함 개념
- 모델 선택 기준 (작업 적합성, 비용, 지연, 크기)
- 배포 토폴로지 (실시간 vs 배치 vs 스트리밍)
- 컨텍스트 윈도우 관리, 프롬프트 아키텍처 (system/user/context)
- 가드레일 배치, 재시도·페일오버·폴백 패턴
- 멀티모달 아키텍처, 캐싱, 레이트 리밋
- A/B 테스트, 모델 버전 관리, 리전/컴플라이언스

## Task 3.2 포함 개념
- 프롬프트 유형별 활용 (Zero/One/Few-shot, CoT, ReAct)
- System vs User 프롬프트, 역할·페르소나
- 구조화된 출력 (JSON, XML 태그, 구분자)
- 프롬프트 인젝션 방어, 반복 개선, 프롬프트 버저닝
- Self-consistency, 명확한 제약 명시

## Task 3.3 포함 개념
- Continued Pre-training vs Fine-tuning
- Domain adaptation vs Instruction fine-tuning
- 데이터 큐레이션·품질, catastrophic forgetting
- Bedrock 파인튜닝 vs SageMaker Training Jobs vs JumpStart
- 하이퍼파라미터 (LR, epoch, batch), 정규화, 조기 종료
- 학습 비용·시간 최적화 (spot, distillation, LoRA 개념)

## Task 3.4 포함 개념
- Bedrock Model Evaluation (Automatic vs Human)
- 지표: ROUGE/BLEU/BERTScore/Perplexity/MMLU/HELM/BIG-bench
- SageMaker Clarify (편향, 설명 가능성)
- 인적 평가 (관련성, 정확성, 유해성)
- A/B 테스트, 지속적 평가, 프롬프트-모델 상호작용 평가
