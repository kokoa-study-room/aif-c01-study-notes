# AWS Certified AI Practitioner (AIF-C01) — 한글 번역본

> 📚 **이 문서는 [vicsz/aif-c01-study-notes](https://github.com/vicsz/aif-c01-study-notes) 저장소를 fork하여 한글로 번역한 학습 자료입니다.**
> 각 항목은 **한글 번역이 먼저** 표시되며, **원문(영어)이 인용문 형태로 함께** 제공됩니다. 원문의 모든 내용은 빠짐없이 보존되었습니다.
>
> This is a Korean translation forked from [vicsz/aif-c01-study-notes](https://github.com/vicsz/aif-c01-study-notes). Korean translations are presented first, and the original English content follows in blockquotes. All original content is preserved without omission.

---

### 시험 학습 노트 및 준비 가이드
### Exam Study Notes & Prep Guidance

이 문서는 **AWS Certified AI Practitioner (AIF-C01)** 시험에 대한 저자의 개인 학습 노트입니다.

> These are my personal study notes for the **AWS Certified AI Practitioner (AIF-C01)** exam.

**AWS Certified Cloud Practitioner (CLF-C02)** 시험과 난이도가 비슷한 **기초 수준(foundational-level) 인증**이지만, **AWS 환경의 AI, ML, 생성형 AI**에 특화되어 있습니다.

> This is a **foundational-level certification**, comparable in difficulty to **AWS Certified Cloud Practitioner (CLF-C02)** — but focused specifically on **AI, ML, and Generative AI on AWS**.

시험은 다음과 같은 내용을 **개념적·고수준으로** 다룹니다:

- 핵심 AI 및 GenAI(생성형 AI) 용어
- 책임 있는 AI(Responsible AI)의 기본 원칙
- AWS AI/ML 서비스의 개념적 이해
- 간단한 유즈 케이스(use-case) 매칭

> The exam is **high-level and conceptual**, covering:
>
> - Core AI and GenAI terminology
> - Responsible AI basics
> - AWS AI/ML services at a conceptual level
> - Simple use-case matching

## 학습 시간 (Study Time)

기본적인 AWS 사용 경험이 있다면, 현실적으로 **주말 하루 정도 집중해서 학습하면 충분히 대비**할 수 있습니다.

> If you already have basic AWS familiarity, this is realistically **one focused weekend of study**.

## 준비 방법 (Preparation)

다음 정도만 준비해도 합격에는 충분합니다:

- 무료 **AWS Skill Builder 강의** (~약 15시간 — 1.25x~1.5x 배속으로 보면 더 빠르게 완료 가능)
- 무료 공식 **AWS 연습 문제** (실제 시험보다 약간 어렵게 느껴짐)

깊은 기술적 경험이나 고급 아키텍처 지식은 필요하지 않습니다.

> The following is sufficient to pass:
>
> - The free **AWS Skill Builder course** (~15 hours — easily completed faster at 1.25x–1.5x speed)
> - The free official **AWS practice questions** (which felt slightly harder than the real exam)
>
> No deep technical experience or advanced architecture knowledge is required.

## 유용한 링크 (Useful Links)
- [공식 시험 가이드 / Official Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Exam-Guide.pdf)
- [공식 시험 준비 강의 - Amazon Skill Builder / Official Exam Prep - Amazon Skill Builder](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/19554/exam-prep-standard-course-aws-certified-ai-practitioner-aif-c01) - 1.5x 배속으로 시청 권장
- [공식 시험 연습 문제 / Official Exam Practice Questions](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/19790/exam-prep-official-practice-question-set-aws-certified-ai-practitioner-aif-c01-english) - 실제 시험과 비슷한 수준

## 개요 (Overview)

### 범용 AI (General AI)
- **정의**: 인간이 수행할 수 있는 모든 지적 작업을 수행할 수 있는 시스템 구축을 목표로 하는, 인공지능의 더 넓은 개념을 의미합니다. 매우 자율적이고 유연한 AI 시스템을 만들려는 장기적 목표를 설명할 때 자주 사용됩니다.
- **핵심 개념**: 특화된 AI 시스템과 달리, 여러 도메인에 걸쳐 다양한 작업을 수행할 수 있는 광범위한 능력을 가진 AI.
- **예시**: **전문가 시스템(Expert Systems)**, **규칙 엔진(Rules Engines)** (예: MYCIN) — 사전에 정의된 로직과 규칙으로 의사결정을 수행합니다.

> - **Definition**: Refers to a broader concept of artificial intelligence, aiming to build systems that can perform any intellectual task that a human can. It's often used to describe long-term goals of creating highly autonomous, flexible AI systems.
> - **Key Concept**: AI with a broad ability to perform multiple tasks across domains, unlike specialized AI systems.
> - **Examples**: **Expert Systems**, **Rules Engines** (e.g., MYCIN), which use predefined logic and rules to make decisions.

### 머신러닝 (Machine Learning, ML)
- **정의**: 명시적인 프로그래밍이나 규칙 없이도, 데이터로부터 학습하여 예측이나 의사결정을 수행할 수 있게 해 주는 AI의 하위 분야.
- **핵심 개념**: 명시적으로 코딩된 지시가 아닌, 데이터 패턴과 학습(training)을 통해 동작하는 AI.
- **예시**: **선형 회귀(Linear Regression)**, **의사결정 트리(Decision Trees)**, **서포트 벡터 머신(Support Vector Machines)** — 예측 작업에 사용되는 지도학습 알고리즘.

> - **Definition**: A subset of AI that enables systems to learn from data and make predictions or decisions without explicit programming or rules.
> - **Key Concept**: AI that operates through data patterns and training, rather than explicitly coded instructions.
> - **Examples**: **Linear Regression**, **Decision Trees**, **Support Vector Machines**—supervised learning algorithms used for predictive tasks.

### 딥러닝 (Deep Learning)
- **정의**: 복잡한 데이터 패턴을 모델링하기 위해 여러 층(layer)의 신경망(그래서 이름이 "deep")을 사용하는 머신러닝의 하위 분야.
- **핵심 개념**: 이미지 인식, 자연어 처리, 자율 시스템과 같은 작업에 효과적입니다.
- **예시**: 이미지 처리를 위한 **합성곱 신경망(CNN, Convolutional Neural Networks)**, 시계열이나 언어 모델과 같은 순차 데이터를 위한 **순환 신경망(RNN, Recurrent Neural Networks)**.

> - **Definition**: A subset of machine learning that uses neural networks with multiple layers (hence "deep") to model complex patterns in data.
> - **Key Concept**: Effective for tasks like image recognition, natural language processing, and autonomous systems.
> - **Examples**: **Convolutional Neural Networks (CNNs)** for image processing, **Recurrent Neural Networks (RNNs)** for sequential data like time-series or language models.

### 생성형 AI (Generative AI)
- **정의**: 학습한 데이터를 기반으로 새로운 콘텐츠(텍스트, 이미지, 음악 등)를 생성하는 데 초점을 둔 딥러닝의 하위 분야. 생성형 AI 모델은 일반적으로 **파운데이션 모델(foundation models)**을 기반으로 하는데, 이는 다양한 작업에 적응(fine-tune)시킬 수 있는 대규모 사전 학습(pre-trained) 모델입니다.
- **핵심 개념**: 학습 중에 배운 패턴을 기반으로 새로운 출력을 생성하는 AI 시스템. 파운데이션 모델은 특정 작업에 맞게 파인튜닝할 수 있는 범용성을 제공합니다.
- **예시**: 텍스트 생성용 **ChatGPT**, 이미지 생성용 **DALL·E**, 예술적 시각 생성용 **DeepDream**.

> - **Definition**: A subset of deep learning focused on creating new content (such as text, images, or music) from learned data. Generative AI models are generally based on **foundation models**, which are large, pre-trained models that can be adapted to a wide range of tasks.
> - **Key Concept**: AI systems that generate novel outputs based on patterns learned during training. Foundation models provide the versatility needed for fine-tuning on specific tasks.
> - **Examples**: **ChatGPT** for text generation, **DALL·E** for image generation, **DeepDream** for artistic visual generation.

### 대규모 언어 모델 (Large Language Models, LLMs)
- **정의**: 인간과 유사한 텍스트를 이해하고 생성하는 데 특화된 **생성형 AI**의 한 유형. LLM은 방대한 텍스트 데이터로 학습하여 언어 패턴, 문법, 문맥을 배웁니다.
- **핵심 개념**: LLM은 입력 프롬프트(prompt)를 기반으로 일관성 있고 고품질의 텍스트를 생성하며, 요약·번역·질의응답 같은 작업을 수행할 수 있습니다.
- **예시**: **GPT-4**, **BERT**, **T5**, **Claude 2** — 텍스트 생성, 감정 분석, 요약, 자연어 이해 등에 사용됩니다.

> - **Definition**: A type of **Generative AI** focused on understanding and generating human-like text. LLMs are trained on vast amounts of text data to learn language patterns, grammar, and context.
> - **Key Concept**: LLMs generate coherent and high-quality text based on input prompts and are capable of performing tasks like summarization, translation, and question answering.
> - **Examples**: **GPT-4**, **BERT**, **T5**, **Claude 2**—used for tasks like text generation, sentiment analysis, summarization, and natural language understanding.

---

## 개념 (Concepts)

### 인컨텍스트 러닝 (In-Context Learning)
- **정의**: 프롬프트(prompt)에 추가 데이터와 예시를 넣어 생성형 AI 모델을 강화하는 방법으로, 모델이 작업을 더 효과적으로 해결하도록 도와줍니다.

> - **Definition**: A method of enhancing generative AI models by adding additional data and examples to the prompt, helping the model solve tasks more effectively.

### 프롬프트 유형 (Prompt Types)
- **Few-Shot Prompt (퓨샷 프롬프트)**: 모델의 동작을 안내하기 위해 프롬프트에 몇 개의 예시를 제공하는 방법.
- **Zero-Shot Prompt (제로샷 프롬프트)**: 프롬프트에 예시를 제공하지 않고, 안내 없이 작업을 수행하도록 모델에 요청하는 방법.
- **One-Shot Prompt (원샷 프롬프트)**: 모델의 동작을 안내하기 위해 정확히 하나의 예시만 제공하는 방법.
- **Prompt Template (프롬프트 템플릿)**: AI 모델과의 상호작용을 표준화하고 개선하기 위한, 사전에 정의된 프롬프트 형식이나 구조.
- **Chain-of-Thought Prompting (사고 사슬 프롬프팅)**: 모델이 추론 과정을 단계별로 나누어 진행하도록 유도하는 프롬프팅 방법.
- **Prompt Tuning (프롬프트 튜닝)**: 특정 작업에서 모델 성능을 개선하기 위해 프롬프트를 조정하는 과정.

> - **Few-Shot Prompt**: Providing a few examples in the prompt to guide the model's behavior.
> - **Zero-Shot Prompt**: Providing no examples in the prompt, asking the model to perform the task without guidance.
> - **One-Shot Prompt**: Providing exactly one example to guide the model's behavior.
> - **Prompt Template**: A pre-defined format or structure for prompts to standardize and improve the interaction with AI models.
> - **Chain-of-Thought Prompting**: A method where the prompt encourages the model to break down reasoning into steps.
> - **Prompt Tuning**: The process of adjusting prompts to improve model performance for specific tasks.

### 잠재 공간 (Latent Space)
- **정의**: 대규모 언어 모델(LLM)이 데이터 간의 관계를 저장하기 위해 포착한, 인코딩된 지식이나 패턴.
- **용도**: AI 모델이 출력을 생성할 때 사용하는, 언어 또는 데이터에 대한 내부적 이해를 표현합니다.

> - **Definition**: The encoded knowledge or patterns captured by large language models (LLMs) that store relationships between data.
> - **Usage**: It represents the internal understanding of language or data that AI models use to generate outputs.

### 임베딩 (Embeddings)
- **정의**: 토큰(단어, 구 등)의 의미(semantic meaning)를 포착한, 수치화된 벡터 표현.
- **활용 사례**: 시맨틱 검색(semantic search)처럼 단어나 토큰의 의미가 중요한 작업에 사용됩니다.
- **저장**: 효율적인 검색과 조회를 위해 벡터 데이터베이스(vector database)에 저장할 수 있습니다.

> - **Definition**: Numerical, vectorized representations of tokens (words, phrases, etc.) that capture their semantic meaning.
> - **Use Case**: Used for tasks like semantic search, where the meaning of a word or token is important.
> - **Storage**: Can be stored in a vector database for efficient search and retrieval.

### 토큰 (Tokens)
- **정의**: 언어 모델이 처리하는 텍스트의 기본 단위(예: 단어, 서브워드, 문자 등). LLM에서는 입력(제공된 텍스트)과 출력(생성된 텍스트) 모두를 표현하는 데 토큰을 사용합니다.

> - **Definition**: The basic units of text (e.g., words, subwords, or characters) that are processed by language models. In the context of LLMs, tokens are used to represent both inputs (text provided) and outputs (text generated).

### 컨텍스트 윈도우 (Context-Window)
- **정의**: LLM 모델이 한 번에 처리할 수 있는 최대 토큰 수로, 입력 프롬프트와 모델이 생성한 출력을 모두 포함합니다. 토큰 수가 모델의 컨텍스트 윈도우를 초과하면, 텍스트의 앞부분이 잘려나갈 수 있습니다.
- **용도**: 컨텍스트 윈도우는 한 번에 모델에 얼마나 많은 정보를 넣을 수 있는지 결정하는 핵심 요소이며, 장문 생성·문서 분석·다중 턴 대화 같은 작업에 영향을 줍니다.

> - **Definition**: The maximum amount of tokens an LLM model can process at once, including both the input prompt and the output generated by the model. If the number of tokens exceeds the model's context-window, earlier parts of the text may be truncated.
> - **Usage**: The context-window is a key factor in determining how much information can be fed into the model at one time and affects tasks like long-form text generation, document analysis, or multi-turn conversations.

### 환각 (Hallucinations)
- **정의**: 환각(hallucination)은 언어 모델이 그럴듯하게 들리지만 실제 데이터나 제공된 입력에 근거하지 않는, 부정확하거나 말이 안 되는 정보를 생성할 때 발생합니다.
- **완화 방법**:
  - **검색 증강 생성(RAG, Retrieval Augmented Generation)**: 생성 과정에서 관련 있는 외부 데이터를 검색하여, 정확한 정보를 기반으로 응답을 생성하도록 함으로써 환각을 완화합니다.
  - **파인튜닝(Fine-Tuning)**: 더 관련성 있고 정확한 데이터로 모델을 학습시키면, 출력이 사실에 부합하도록 유도되어 환각을 줄일 수 있습니다.
  - **HITL(Human-in-the-Loop)**: 신뢰도가 낮은 영역에 사람의 검토를 개입시켜, 환각된 출력이 중요한 애플리케이션에 사용되는 것을 방지합니다.

> - **Definition**: Hallucinations occur when a language model generates incorrect or nonsensical information that may sound plausible but is not grounded in factual data or the provided input.
> - **Mitigations**:
>   - Retrieval Augmented Generation (RAG): Mitigates hallucinations by retrieving relevant external data during the generation process, ensuring the model generates responses based on accurate information.
>   - Fine-Tuning: Training the model on more relevant, accurate data can help reduce hallucinations by aligning the model's output with factual knowledge.
>   - Human-in-the-Loop (HITL): Incorporating human review in low-confidence areas can prevent hallucinated outputs from being used in critical applications.

### 멀티모달 모델 (Multi-Modal Models)
- **정의**: 여러 유형의 데이터를 다루는 모델로, 텍스트·이미지·오디오 등을 공유 공간에 임베딩합니다. 이러한 모델은 여러 유형의 입력을 활용하여 더 풍부하고 문맥을 잘 이해하는 출력을 생성하는 멀티모달 생성 작업(예: 이미지에 캡션 달기, 텍스트 설명으로부터 시각적 결과 생성)에 흔히 사용됩니다.

> - **Definition**: Models that work across multiple data types, embedding text, images, or even audio into a shared space. These models are commonly used for multimodal generation tasks, such as creating captions for images or generating visuals from textual descriptions, by leveraging different types of input to produce richer, more context-aware outputs.

---

### 검색 방식 (Search Methods)
- **Keyword Search (키워드 검색)**: 검색 쿼리의 정확한 용어를 매칭시킵니다.
- **Semantic Search (시맨틱 검색)**: 임베딩을 사용하여 검색 쿼리의 의미를 이해하며, 더 정확하고 의미 있는 결과를 반환할 수 있습니다.

> - **Keyword Search**: Matches exact terms in the search query.
> - **Semantic Search**: Uses embeddings to understand the meaning behind the search query, allowing for more accurate and meaningful results.

---

### 벡터 데이터베이스 (Vector Databases)
- **정의**: 벡터(임베딩)를 저장하고 조회하도록 설계된 데이터베이스 유형으로, 시맨틱 검색과 같은 작업에 유용합니다.

> - **Definition**: A type of database designed for storing and querying vectors (embeddings), which is useful for tasks like semantic search.

#### AWS의 벡터 데이터베이스 옵션 (Vector Database Options on AWS)
- **Amazon OpenSearch Service**: 벡터 데이터베이스를 위한 k-최근접 이웃(k-NN) 검색을 지원합니다. 로그 분석, 실시간 애플리케이션 모니터링, 검색에 유용합니다.
- **Amazon Aurora PostgreSQL-Compatible Edition & Amazon RDS for PostgreSQL**: __pgvector__ 확장을 지원하여, 임베딩의 효율적 저장과 유사도 검색을 가능하게 합니다.
- **Amazon Neptune ML**: 그래프 신경망(GNN, Graph Neural Networks)을 사용하여 그래프 데이터 기반의 예측을 수행하며, 그래프 데이터베이스의 벡터화된 데이터를 지원합니다.
- **Amazon MemoryDB**: 밀리초 단위 쿼리 시간과 초당 수만 건의 QPS(Queries Per Second)로 고속 벡터 저장 및 조회를 지원합니다.
- **Amazon DocumentDB**: MongoDB와 호환되는 벡터 검색을 지원하여, 수백만 개의 벡터를 밀리초 단위 응답 시간으로 저장·인덱싱·검색할 수 있습니다.

> - **Amazon OpenSearch Service**: Supports k-nearest neighbor (k-NN) search for vector databases. Useful for log analytics, real-time application monitoring, and search.
> - **Amazon Aurora PostgreSQL-Compatible Edition & Amazon RDS for PostgreSQL**: Supports the __pgvector__ extension, enabling efficient storage of embeddings and similarity searches.
> - **Amazon Neptune ML**: Uses Graph Neural Networks (GNNs) to make predictions based on graph data, supporting vectorized data in graph databases.
> - **Amazon MemoryDB**: Supports high-speed vector storage and retrieval with millisecond query times and tens of thousands of queries per second (QPS).
> - **Amazon DocumentDB**: Supports vector search with MongoDB compatibility, enabling storage, indexing, and search of millions of vectors with millisecond response times.

--- 

## 머신러닝(ML) 파이프라인 (The Machine Learning (ML) Pipeline)

ML 파이프라인은 머신러닝 모델을 구축·학습·배포하기 위해 사용되는 체계적인 프로세스입니다. 비즈니스 목표 정의부터 배포된 모델의 모니터링까지 각 단계가 적절히 관리되고 성능이 최적화되도록 보장합니다. 파이프라인의 전형적인 단계는 다음과 같습니다:

> The ML Pipeline is a systematic process used to build, train, and deploy machine learning models. It ensures that each stage, from identifying business goals to monitoring deployed models, is properly managed and optimized for performance. The typical steps in the pipeline are as follows:

**단계 (Steps):**
1. 비즈니스 목표 정의 (Identify Business Goal)
2. ML 문제 정의 (Frame ML Problem)
3. 데이터 수집 (Collect Data)
4. 데이터 전처리 (Pre-Process Data)
5. 피처 엔지니어링 (Engineer Features)
6. 학습·튜닝·평가 (Train, Tune, Evaluate)
7. 배포 (Deploy)
8. 모니터링 (Monitor)

---

### 1. 비즈니스 목표 정의 (Identify Business Goal)
- **설명**: ML 프로젝트가 비즈니스 목표를 충족하도록, 성공 기준을 정의하고 이해관계자와 방향을 정렬합니다.
- **주요 활동**:
  - 명확한 성공 지표를 수립합니다.
  - 조직 전반의 이해관계자와 협의·정렬합니다.

> - **Description**: Define success criteria and align stakeholders to ensure the ML project meets business objectives.
> - **Key Activities**:
>   - Establish clear success metrics.
>   - Align with stakeholders across the organization.

### 2. ML 문제 정의 (Frame the ML Problem)
- **설명**: 실현 가능성과 비용/편익 분석을 고려하면서, ML 문제와 입력·출력·지표를 정의합니다.
- **주요 활동**:
  - 입력, 출력, 요구사항, 성능 지표를 식별합니다.
  - 실현 가능성을 평가하기 위한 비용-편익 분석을 수행합니다.

- **모델 옵션**:
  - **AI/ML 호스팅 서비스** (예: AWS Comprehend, Forecast, Personalize): 학습이 필요 없음.
  - **사전 학습 모델** (예: Amazon Bedrock, SageMaker JumpStart): 자체 데이터로 파인튜닝하여 사용.
  - **완전 커스텀 모델**: 처음부터 직접 구축하고 학습.

> - **Description**: Define the ML problem, inputs, outputs, and metrics while considering feasibility and cost/benefit analysis.
> - **Key Activities**:
>   - Identify inputs, outputs, requirements, and performance metrics.
>   - Perform cost-benefit analysis to evaluate feasibility.
>
> - **Model Options**:
>   - **AI/ML Hosted Service** (e.g., AWS Comprehend, Forecast, Personalize): No training required.
>   - **Pre-trained Models** (e.g., Amazon Bedrock, SageMaker JumpStart): Fine-tune with your data.
>   - **Fully Custom Model**: Build and train from scratch.

### 3. 데이터 수집 (Collect Data)

- **설명**: 모델 학습에 필요한 데이터를 수집하고 준비합니다.

- **주요 활동**:
  - 데이터 소스(예: 데이터베이스, 데이터 레이크, 외부 API)를 식별합니다.
  - 데이터를 수집(ingest)하고 라벨링(label)합니다.

- **데이터 저장 위치**:
  - 머신러닝을 위해 수집된 데이터는 일반적으로 **Amazon S3**에 저장됩니다. 이는 내부 시스템에서 가져온 데이터뿐 아니라 **AWS Data Exchange**를 통해 접근한 서드파티 데이터셋에도 적용됩니다.

- **도구**:
  - **AWS Glue**: **ETL(Extract, Transform, Load)** 프로세스를 담당하며, **Amazon S3**에 저장하기 전에 데이터를 사용 가능한 형식으로 이동·변환합니다.
  - **SageMaker Ground Truth**: 애매한 데이터에 대해 사람이 라벨링할 수 있게 해 주며, 라벨링된 데이터는 **Amazon S3**에 저장됩니다.
  - **AWS Data Exchange**: 서드파티 데이터셋에 안전하게 접근할 수 있게 해 줍니다. 이 데이터셋은 학습 데이터의 추가 소스로 사용될 수 있으며, 수집된 데이터는 **Amazon S3**에 저장됩니다.
  - **Amazon S3**: 수집된 데이터가 처리 또는 학습에 사용되기 전에 안전하게 저장되는 주요 스토리지 서비스입니다.

> - **Description**: Collect and prepare the necessary data for training the model.
>
> - **Key Activities**:
>   - Identify data sources (e.g., databases, data lakes, external APIs).
>   - Ingest and label data.
>
> - **Where Data is Stored**:
>   - Data collected for machine learning is typically stored in **Amazon S3**. This applies to both data sourced from internal systems and third-party datasets accessed via **AWS Data Exchange**.
>
> - **Tools**:
>   - **AWS Glue**: For **ETL (Extract, Transform, Load)** processes, moving and transforming data into a usable format before storage in **Amazon S3**.
>   - **SageMaker Ground Truth**: For human labeling of ambiguous data, with labeled data stored in **Amazon S3**.
>   - **AWS Data Exchange**: Allows secure access to third-party datasets. These datasets can be used as additional sources of training data, and the ingested data is stored in **Amazon S3**.
>   - **Amazon S3**: Primary storage service where collected data is securely stored before being processed or used for training.

### 4. 데이터 전처리 (Pre-Process Data)

- **설명**: 학습에 적합하도록 데이터를 정제하고 준비합니다.

- **주요 활동**:
  - **탐색적 데이터 분석(EDA, Exploratory Data Analysis)**을 수행합니다.
  - 중복 제거, 결측치 채우기, **PII(개인식별정보)** 익명화 등 데이터를 정제합니다.
  - 데이터는 흔히 **학습(training, 80%)**, **검증(validation, 10%)**, **테스트(test, 10%)** 셋으로 분할됩니다.

- **데이터 정제 방법**:
  - **AWS Glue 변환(Transformations)**: Glue는 중복 제거·결측치 채우기 등의 작업을 위한 내장 변환을 제공하며, Python이나 Spark를 사용한 커스텀 변환도 허용합니다.
  - **PII를 위한 Macie**: AWS Macie는 **PII** 데이터를 탐지하고 익명화하며, **Amazon S3**와 연동하여 민감 정보를 스캔·마스킹합니다.
  - **AWS Glue DataBrew**: 시각적 인터페이스를 통해 데이터 준비와 정제를 가능하게 합니다. 결측치 채우기 같은 **데이터 품질 규칙**을 적용할 수 있고, 이 변환들을 재사용 가능한 **레시피(recipes)**로 저장할 수 있습니다.
  - **SageMaker Canvas**: 깊은 기술 지식 없이도 데이터 임포트·변환·시각화를 지원합니다. 학습을 위한 데이터를 단계별로 준비하는 내장 변환을 사용하며, 각 단계는 시각적으로 흐름(flow)을 추적할 수 있습니다.

- **도구**:
  - **AWS Glue**: 데이터 정제를 위한 내장 변환을 갖춘 ETL 서비스입니다.
  - **AWS Glue DataBrew**: 변환 규칙(**레시피**)을 정의·적용할 수 있는 시각적 데이터 준비 도구이며, 내장 데이터 품질 검사를 지원합니다.
  - **SageMaker Canvas**: 시각적 노코드(no-code) 인터페이스로 데이터 임포트·준비·변환을 도와주는 도구입니다. 각 변환 단계가 명확한 워크플로의 일부이므로, 데이터 준비가 더 접근하기 쉬워집니다.

> - **Description**: Clean and prepare the data, ensuring it is suitable for training.
>
> - **Key Activities**:
>   - Perform **Exploratory Data Analysis (EDA)**.
>   - Clean the data, removing duplicates, filling missing values, and anonymizing **PII**.
>   - Split data is often split into ratios of **training (80%)**, **validation (10%)**, and **test (10%)** sets.
>
> - **How to Clean Data**:
>   - **AWS Glue Transformations**: Glue has built-in transformations for tasks like removing duplicates or filling missing values, and allows custom transformations using Python or Spark.
>   - **Macie for PII**: AWS Macie detects and anonymizes **PII** data, working with **Amazon S3** to scan and mask sensitive information.
>   - **AWS Glue DataBrew**: Enables data preparation and cleaning through a visual interface. You can apply **data quality rules**, such as filling missing values, and save these transformations as **recipes** for reuse.
>   - **SageMaker Canvas**: Facilitates data import, transformation, and visualization without requiring deep technical knowledge. It uses built-in transformations that are added step-by-step to prepare data for training, and each step can be visually tracked in the flow.
>
> - **Tools**:
>   - **AWS Glue**: An ETL service with built-in transformations for data cleaning.
>   - **AWS Glue DataBrew**: A visual data preparation tool where you can define and apply transformation rules (called **recipes**), with built-in data quality checks.
>   - **SageMaker Canvas**: A tool for importing, preparing, and transforming data with a visual, no-code interface. Each transformation step is part of a clear workflow, making data preparation more accessible.

### 5. 피처 엔지니어링 (Engineer Features)
- **설명**: 모델 성능을 향상시킬 피처(features)를 선정하고 설계합니다.
- **주요 활동**:
  - **피처 선택(Feature Selection)**: 도메인 지식을 기반으로 데이터셋에서 가장 관련성 높은 피처를 식별하여, 차원을 줄이고 모델 효율성을 향상시킵니다.
  - **피처 생성(Feature Creation)**: 원시 데이터를 새로운 피처로 변환합니다 (예: 스케일링, 범주형 변수 인코딩, 기존 피처로부터 새로운 지표 도출).
  - **피처 변환(Feature Transformation)**: 모델 수렴과 성능을 개선하기 위해 수학적·통계적 변환(예: 정규화, 표준화)을 적용합니다.
- **자동화된 피처 엔지니어링**: SageMaker Autopilot을 고려해 볼 수 있으며, 이는 모델 성능을 개선할 수 있는 피처를 자동으로 생성하고 순위화합니다.
- **차원 축소(Dimensionality Reduction)**: 주성분 분석(PCA, Principal Component Analysis) 같은 기법을 사용하여, 가장 중요한 정보는 유지하면서 피처 수를 줄일 수 있습니다.
- **피처 스케일링(Feature Scaling)**: AWS Glue나 SageMaker DataBrew 같은 도구로 스케일링 기법(예: 정규화, 표준화)을 적용하여, 각 피처가 모델 학습에 동등하게 기여하도록 만들 수 있습니다.
- **범주형 인코딩(Categorical Encoding)**: SageMaker Data Wrangler나 AWS Glue를 사용하여 원-핫 인코딩(one-hot encoding)이나 타깃 인코딩(target encoding) 같은 기법으로 범주형 변수를 수치값으로 변환합니다.

- **도구**:
  - **SageMaker Feature Store**: 피처를 단일 정보원(single source of truth)으로 저장·관리합니다.

> - **Description**: Select and engineer features that will enhance model performance.
> - **Key Activities**:
>   - Feature Selection: Identifying the most relevant features from your dataset based on domain knowledge, reducing dimensionality and improving model efficiency.
>   - Feature Creation: Transforming raw data into new features (e.g., scaling, encoding categorical variables, and deriving new metrics from existing ones).
>   - Feature Transformation: Applying mathematical or statistical transformations (e.g., normalization, standardization) to improve model convergence and performance.
> - Automated Feature Engineering: Consider using SageMaker Autopilot, which can automatically generate and rank features that could improve model performance.
> - Dimensionality Reduction: Techniques like Principal Component Analysis (PCA) can be applied to reduce the number of features while retaining the most important information.
> - Feature Scaling: Tools like AWS Glue or SageMaker DataBrew can be used to apply scaling techniques (e.g., normalization or standardization), ensuring that features contribute equally to model training.
> - Categorical Encoding: Convert categorical variables into numerical values using techniques like one-hot encoding or target encoding using SageMaker Data Wrangler or AWS Glue.
>
> - **Tools**:
>   - **SageMaker Feature Store**: Store and manage features as a single source of truth.

### 6. 모델 학습·튜닝·평가 (Train, Tune, and Evaluate the Model)
- **설명**: 모델을 학습시키고, 튜닝하며, 성능을 평가합니다.
- **주요 활동**:
  - 모델을 반복적으로 학습시키고 파라미터를 세밀하게 조정합니다.
  - 하이퍼파라미터(예: epoch, 배치 크기, 학습률)를 튜닝하고 실험을 수행합니다.
  - 지표를 이용해 모델을 평가하고 성능을 비교합니다.

- **파라미터**:
  - **추론 파라미터 (Inference Parameters)** (Amazon Bedrock 지원):
    - **무작위성과 다양성 (Randomness and Diversity)**:
      - Temperature (온도):
        - 무작위성을 제어합니다. 값이 클수록 다양하고 창의적인 출력이 나오고, 값이 낮을수록 더 예측 가능하고 결정론적인 결과가 나옵니다.
      - Top K:
        - 모델이 상위 K개의 가장 확률이 높은 토큰 중에서만 선택하도록 제한합니다. K가 작을수록 더 안전하고 예측 가능한 선택이 됩니다.
        - Top K는 그리 유용한 파라미터가 아닙니다 — 대신 Temperature나 Top-P를 사용하세요.
      - Top P:
        - 누적 확률을 사용하여 토큰을 선택합니다. 확률 합이 P가 되는 가장 작은 토큰 집합에 초점을 맞추어, 무작위성과 다양성의 균형을 맞춥니다.
        - Top P 값이 클수록(1에 가까울수록) 토큰 풀이 가장 확률이 높은 것들로만 제한되어 무작위성이 줄어듭니다.
      - Top-K vs Top-P: Top K는 고려할 토큰 수를 고정시키는 반면, Top P는 토큰의 누적 확률에 따라 가변적인 개수를 사용합니다. 이 때문에 Top P가 무작위성 조절에 있어 더 적응적이고 유연합니다.
      - Temperature vs. Top P: Temperature는 확률 값을 스케일링하여 전체적인 무작위성을 조절하며, 모든 가능한 토큰에 걸쳐 무작위성을 더 크게 하거나 작게 할 수 있습니다. Top P는 누적하여 특정 확률 임계값에 도달하는 토큰들로만 선택지를 좁혀, 무작위성과 정확성 사이의 균형을 맞춥니다.
      - 활용 사례:
        - 적응적인 다양성을 원하지만 좀 더 가능성이 높은 결과에 머무르고 싶다면 Top-P를 사용하세요.
        - 전반적으로 일관된 무작위성 제어가 필요하다면 Temperature를 사용하세요.
    - Response length (응답 길이):
      - 생성 출력의 최대 길이를 지정합니다. 응답이 얼마나 자세하거나 간결할지에 영향을 줍니다.
    - Penalties (페널티):
      - 반복되는 토큰이나 시퀀스에 페널티를 적용하여, 생성된 텍스트에 다양성을 유도합니다.
    - Stop sequences (중지 시퀀스):
      - 모델이 텍스트 생성을 중지할 특정 시퀀스를 정의하여, 출력 길이나 형식을 제어합니다.
  - **모델 학습 파라미터 (Hyperparameters)**:
    - **Epoch**: 전체 데이터셋을 통과하는 반복 횟수.
      - Epoch를 늘리면 일반적으로 모델의 학습이 개선되지만, 너무 많으면 오버피팅(overfitting)으로 이어질 수 있습니다. Epoch가 많을수록 모델이 더 잘 학습하지만, 특정 지점을 넘으면 수확 체감(diminishing returns)이 발생할 수도 있습니다.
    - **Batch Size (배치 크기)**: 모델 파라미터를 업데이트하기 전에 처리하는 샘플 수.
      - 작은 배치 크기는 더 빈번한 업데이트를 제공하여 빠른 수렴에 도움이 될 수 있지만, 노이즈가 더 많이 들어올 수 있습니다. 큰 배치 크기는 더 안정적이지만 더 많은 연산과 메모리를 요구할 수 있습니다.
    - **Learning Rate (학습률)**: 모델이 얼마나 빠르게 학습하는지를 제어합니다.
      - 학습률이 높으면 학습이 빨라지지만 최적 해를 지나쳐 버릴 수 있습니다. 학습률이 낮으면 수렴이 더 느리지만 정밀해지며, 대신 지역 최솟값(local minima)에 갇힐 위험이 있습니다.

> - **Description**: Train the model, tune it, and evaluate performance.
> - **Key Activities**:
>   - Train the model iteratively and fine-tune parameters.
>   - Tune hyperparameters (e.g., epoch, batch size, learning rate) and run experiments.
>   - Evaluate the model using metrics and compare performance.
>
> - **Parameters**:
>   - **Inference Parameters** (supported by Amazon Bedrock):
>     - **Randomness and Diversity**:
>       - Temperature:
>         - Controls randomness—higher values lead to more diverse, creative outputs; lower values produce more predictable, deterministic results.
>       - Top K:
>         - Limits the model to selecting from the top K most probable tokens; smaller K values result in safer, more predictable choices.
>         - Top K is not a terribly useful parameter - use Temperature or Top-P instead.
>       - Top P:
>         - Uses cumulative probability to choose tokens, focusing on the smallest set of tokens with a combined probability of P, balancing randomness and diversity.
>         - Higher Top P values (closer to 1) reduce randomness by restricting the token pool to only the most probable choices.
>       - Top-K vs Top-P: Top K fixes the number of tokens considered, while Top P uses a variable number of tokens based on their combined probability, making Top P more adaptive and flexible in balancing randomness.
>       - Temperature vs. Top P: Temperature adjusts the overall randomness by scaling probabilities, allowing more or less randomness across all possible tokens. Top P narrows the token choices to those that collectively add up to a certain probability threshold, balancing randomness with accuracy.
>       - Use Cases:
>         - Use Top-P when you want adaptive diversity but want to stay closer to more likely outcomes.
>         - Use Temperature when you need consistent randomness control across the board.
>     - Response length:
>       - Specifies the maximum length of generated output, affecting how verbose or concise the response is.
>     - Penalties:
>       - Applies penalties to repeated tokens or sequences to encourage variety in the generated text.
>     - Stop sequences:
>       - Defines specific sequences where the model will stop generating text, ensuring controlled output length or format.
>   - **Model Training Parameters** (Hyperparameters):
>     - **Epoch**: The number of iterations through the entire dataset.
>       - Increasing epochs generally improves the model's learning but can lead to overfitting if too high. More epochs help the model learn better but might also result in diminishing returns after a certain point.
>     - **Batch Size**: Number of samples before updating model parameters.
>       - Smaller batch sizes provide more frequent updates, which can help in converging quickly but can introduce more noise. Larger batch sizes are more stable but may require more computation and memory.
>     - **Learning Rate**: Controls how fast the model learns.
>       - A high learning rate speeds up training but may skip optimal solutions, while a low learning rate leads to slower but more precise convergence, though it risks getting stuck in local minima.
        
- **오차 지표 (Error Metrics)**:

  - **MSE (Mean Squared Error, 평균 제곱 오차)**: 모델 평가 시, MSE는 예측값과 실제값 사이의 차이의 제곱을 평균 낸 값으로, 큰 오차에 더 많은 가중치를 부여합니다. MSE가 낮을수록 성능이 좋다는 뜻이며, 서로 다른 모델을 비교하거나 하이퍼파라미터를 튜닝할 때 유용합니다.
    - **활용 사례**: 주택 가격이나 주가 예측 같은 회귀 문제에 유용합니다.
    - **경험 법칙**: 낮을수록 좋습니다 — 모델의 예측이 실제값에 더 가깝다는 의미이기 때문입니다.

  - **RMSE (Root Mean Squared Error, 평균 제곱근 오차)**: RMSE는 MSE의 제곱근으로, 예측값과 같은 단위로 오차를 표현하기 때문에 해석이 더 쉽습니다. RMSE는 예측당 예상되는 오차의 크기를 확인하는 데 사용됩니다.
    - **활용 사례**: 해석의 용이성을 위해 MSE와 함께 회귀 문제에서 자주 사용됩니다.
    - **경험 법칙**: RMSE가 낮을수록 모델 성능이 좋습니다.

  - **Perplexity (당혹도)**: Perplexity는 모델이 토큰(예: 단어) 시퀀스를 얼마나 잘 예측하는지 측정합니다. Perplexity가 낮을수록 성능이 좋다는 뜻이며, 이는 모델이 시퀀스에서 다음 단어를 더 잘 예측한다는 것을 의미합니다.
    - **활용 사례**: 언어 모델에서 흔히 사용됩니다. 예를 들어 모델이 문장에서 다음 단어를 얼마나 잘 예측하는지 평가할 때 씁니다.
    - **경험 법칙**: Perplexity가 낮을수록 예측 성능이 더 좋습니다.

  - **Precision (정밀도)**: 정밀도는 실제 양성(true positive)의 수를 모든 양성 예측(true positive + false positive)으로 나눈 비율입니다. 거짓 양성(false positive)을 최소화하는 것이 중요할 때 사용합니다.
    - **활용 사례**: 스팸 탐지처럼 거짓 양성을 피하는 것이 중요한 분류 작업에서 자주 사용됩니다.
    - **경험 법칙**: 거짓 양성의 비용이 높을 때는 정밀도가 높을수록 좋습니다.

  - **Recall (TPR, 재현율)**: Recall(진짜 양성률, True Positive Rate)은 실제 양성 전체(true positive + false negative) 중 실제로 양성으로 예측된 것의 비율입니다. 거짓 음성(false negative)을 최소화하는 것이 중요할 때 사용합니다.
    - **활용 사례**: 의료 검사(예: 질병 스크리닝)에서 양성 사례를 놓치지 않기 위해 자주 사용됩니다.
    - **경험 법칙**: 양성 사례를 놓치는 비용이 클 때는 재현율이 높을수록 좋습니다.

  - **False Positive Rate (FPR, 위양성률)**: FPR은 실제 음성 전체(false positive + true negative) 중 거짓 양성(false positive)의 비율입니다. 잘못된 양성 예측이 얼마나 자주 일어나는지 측정합니다.
    - **활용 사례**: 사기 탐지나 경보 등 보안 애플리케이션에서 거짓 양성을 최소화해야 할 때 자주 사용됩니다.
    - **경험 법칙**: FPR이 낮을수록 좋습니다 — 잘못된 경보가 더 적다는 뜻입니다.

  - **Specificity (TNR, 특이도)**: Specificity(진짜 음성률, True Negative Rate)는 실제 음성 전체(true negative + false positive) 중 실제로 음성으로 예측된 것의 비율입니다. 모델이 음성 사례를 얼마나 잘 식별하는지 측정합니다.
    - **활용 사례**: 의료 검사에서 비질환자를 정확히 식별하기 위해 사용됩니다.
    - **경험 법칙**: 진짜 음성 식별이 중요할 때는 특이도가 높을수록 좋습니다.

  - **Accuracy (정확도)**: 정확도는 올바른 예측(진짜 양성 + 진짜 음성)의 수를 전체 예측 수로 나눈 비율입니다. 양성 예측과 음성 예측이 동등하게 중요할 때 사용합니다.
    - **활용 사례**: 이미지 분류처럼 균형 잡힌 분류 작업에서 흔히 사용됩니다.
    - **경험 법칙**: 전반적인 정답률 관점에서 정확도가 높을수록 좋습니다.

  - **F1 Score**: F1 Score는 정밀도와 재현율의 조화평균으로, 정밀도와 재현율 사이의 균형이 필요할 때 사용합니다.
    - **활용 사례**: 문서 분류 등 거짓 양성과 거짓 음성이 모두 중요한 작업에서 사용됩니다.
    - **경험 법칙**: F1 점수가 높을수록 정밀도와 재현율의 균형이 잘 잡혔다는 뜻입니다.

  - **ROC Curve (수신자 조작 특성 곡선)**: ROC(Receiver Operating Characteristic) 곡선은 다양한 임계값에서 진짜 양성률(recall)과 위양성률을 그래프로 표현한 것입니다. 민감도와 특이도 사이의 트레이드오프를 평가할 때 사용합니다.
    - **활용 사례**: 이진 분류 문제에서 다양한 임계값에 걸친 모델 성능을 시각화하는 데 흔히 사용됩니다.
    - **경험 법칙**: ROC 곡선 아래 면적(AUC)이 클수록 모델 성능이 좋습니다.

> - **Error Metrics**:
>
>   - **MSE (Mean Squared Error)**: During model evaluation, MSE calculates the average squared difference between predicted values and actual values, giving more weight to larger errors. A lower MSE indicates better performance, making it useful for comparing different models or tuning hyperparameters.
>     - **Use Case**: Useful in regression problems like predicting house prices or stock values.
>     - **Rule of Thumb**: Lower is better, as it means the model's predictions are closer to the actual values.
>
>   - **RMSE (Root Mean Squared Error)**: RMSE is the square root of MSE and gives an error measure in the same unit as the predicted values, making it more interpretable. RMSE is used to see how much error is expected per prediction.
>     - **Use Case**: Often used alongside MSE in regression problems for easier interpretability.
>     - **Rule of Thumb**: Lower RMSE means better model performance.
>
>   - **Perplexity**: Perplexity measures how well a model predicts a sequence of tokens (e.g., words). Lower perplexity indicates better performance, as it means the model is better at predicting the next word in a sequence.
>     - **Use Case**: Commonly used for language models, such as evaluating how well a model predicts the next word in a sentence.
>     - **Rule of Thumb**: Lower perplexity means better predictive performance.
>
>   - **Precision**: Precision is the ratio of true positives to the total number of positive predictions (true positives + false positives). It is used when minimizing false positives is important.
>     - **Use Case**: Often used in classification tasks like spam detection, where avoiding false positives is critical.
>     - **Rule of Thumb**: Higher precision is better when the cost of false positives is high.
>
>   - **Recall (TPR)**: Recall (True Positive Rate) is the ratio of true positives to the total actual positives (true positives + false negatives). It is used when minimizing false negatives is crucial.
>     - **Use Case**: Commonly used in medical testing (e.g., disease screenings) to avoid missing positive cases.
>     - **Rule of Thumb**: Higher recall is better when missing positive cases is costly.
>
>   - **False Positive Rate (FPR)**: FPR is the ratio of false positives to the total number of negatives (false positives + true negatives). It is used to measure how often incorrect positive predictions are made.
>     - **Use Case**: Often used in security applications, like fraud detection or alarms, where false positives should be minimized.
>     - **Rule of Thumb**: Lower FPR is better, as it means fewer false alarms.
>
>   - **Specificity (TNR)**: Specificity (True Negative Rate) is the ratio of true negatives to the total actual negatives (true negatives + false positives). It measures how well the model identifies negative instances.
>     - **Use Case**: Used in medical testing to correctly identify non-diseased patients.
>     - **Rule of Thumb**: Higher specificity is better when identifying true negatives is important.
>
>   - **Accuracy**: Accuracy is the ratio of correct predictions (both true positives and true negatives) to the total number of predictions. It is used when both positive and negative predictions are equally important.
>     - **Use Case**: Typically used in balanced classification tasks like image classification.
>     - **Rule of Thumb**: Higher accuracy is better for overall correctness.
>
>   - **F1 Score**: The F1 Score is the harmonic mean of precision and recall, used when there is a need for a balance between precision and recall.
>     - **Use Case**: Used in document classification or tasks where both false positives and false negatives matter.
>     - **Rule of Thumb**: Higher F1 score means better balance between precision and recall.
>
>   - **ROC Curve**: The ROC (Receiver Operating Characteristic) curve plots the true positive rate (recall) against the false positive rate at various threshold levels. It is used to evaluate the trade-off between sensitivity and specificity.
>     - **Use Case**: Commonly used in binary classification problems to visualize the model's performance across different thresholds.
>     - **Rule of Thumb**: A higher area under the ROC curve (AUC) indicates better model performance.

- **모델 학습 시 발생하는 문제 (Model Training Issues)**:
  - **오버피팅(Overfitting, 과적합)**: 동일한 데이터로 지나치게 학습하여 모델이 지나치게 특수화되는 현상.
    - 해결책: 학습 중에 더 다양한 데이터를 사용합니다.
  - **언더피팅(Underfitting, 과소적합)**: 모델이 데이터로부터 충분한 패턴을 학습하지 못하는 현상.
    - 해결책: 모델을 더 많은 epoch 또는 더 많은 데이터로 학습시킵니다.
  - **편향과 공정성(Bias and Fairness)**: 학습 데이터의 다양성 부족으로 편향된 예측이 발생하는 문제.
    - 해결책: 다양하고 대표성 있는 학습 데이터를 확보하고, 공정성 제약(fairness constraints)을 포함시킵니다.

> - **Model Training Issues**:
>   - **Overfitting**: Too much training on the same data, causing the model to be overly specific.
>     - Solution: Use more diverse data during training.
>   - **Underfitting**: The model doesn't learn enough patterns from the data.
>     - Solution: Train the model for more epochs or with more data.
>   - **Bias and Fairness**: Lack of diversity in training data leading to biased predictions.
>     - Solution: Ensure diverse and representative training data; include fairness constraints.

- **파인튜닝 (Fine-Tuning)** (Bedrock 및 SageMaker):
  - 사전 학습된 모델의 가중치를, 자신의 특정 _라벨링된(labelled)_ 데이터로 조정하여 새로운 작업에 적응시키는 방법입니다.
  - 단일 작업만을 위한 지시(instruction)만 제공하면, 모델이 더 일반적인 목적의 능력을 잃고 _파국적 망각(catastrophic forgetting)_을 겪을 수 있음에 유의하세요.
  - **도메인 적응 파인튜닝(Domain adaptation fine-tuning)** (SageMaker): 사전 학습된 파운데이션 모델을 소량의 도메인 특화 데이터로 특정 도메인(예: 법률, 의료)에 맞게 조정합니다. 이는 해당 도메인 관련 작업에서 모델이 더 잘 수행하도록 도와줍니다.
  - **지시 기반 파인튜닝(Instruction-based fine-tuning)** (SageMaker): 특정 작업(예: 요약, 분류)의 라벨링된 예시를 제공하여 그 작업에서의 모델 성능을 개선하는 방식입니다. 정밀한 출력이 필요한 작업에서 모델을 향상시키는 데 유용합니다.

> - **Fine-Tuning** (BedRock and SageMaker):
>   - Adjust the weights of a pre-trained model with your specific and _labelled_ data to adapt it for new tasks.
>   - Be aware that if you only provide instructions for a single task, the model may lose its more general purpose capability and experience _catastrophic forgetting_.
>   - **Domain adaptation fine-tuning** (SageMaker): Tailors a pre-trained foundation model to a specific domain (e.g., legal, medical) using a small amount of domain-specific data. This helps the model perform better on tasks related to that particular domain.
>   - **Instruction-based fine-tuning** (SageMaker): Involves providing labeled examples of specific tasks (e.g., summarization, classification) to improve a model's performance on that particular task. This type of fine-tuning is useful for making the model better at tasks where precise outputs are needed.

- **지속적 사전학습 (Continued-Pretraining)** (Bedrock):
  - _라벨링되지 않은(unlabeled)_ 데이터를 사용하여, 특정 작업에 범위를 좁히지 않고 모델의 전반적인 지식을 확장하는 방법입니다.

> - **Continued-Pretraining** (BedRock):
>   - Using _unlabeled_ data to expand the model's overall knowledge without narrowing its scope to a specific task.

- **전이 학습 (Transfer Learning)**:
  - 일반적인 특징을 학습한 기존 모델을 파인튜닝하여 새로운 문제에 적용하는 방식입니다. 학습 속도를 높이고 정확도를 개선할 수 있습니다.

> - **Transfer Learning**:
>   - Fine-tuning an existing model that has learned general features and applying it to a new problem, speeding up training and improving accuracy.

- **도구**:
  - **SageMaker Training Jobs**: 학습 프로세스를 관리하며, 학습 데이터·하이퍼파라미터·컴퓨트 자원을 지정합니다.
  - **SageMaker Experiments**: 모델 실행과 하이퍼파라미터 튜닝을 추적합니다.
  - **Automatic Model Tuning (AMT)**: 지정된 지표를 사용하여 하이퍼파라미터를 자동으로 튜닝합니다.

> - **Tools**:
>   - **SageMaker Training Jobs**: Manage training processes, specify training data, hyperparameters, and compute resources.
>   - **SageMaker Experiments**: Track model runs and hyperparameter tuning.
>   - **Automatic Model Tuning (AMT)**: Automatically tune hyperparameters using the specified metric.

### 7. 모델 배포 (Deploy the Model)
- **설명**: 학습된 모델을 배포하여 예측을 수행할 수 있게 합니다.

- SageMaker 배포 옵션:
  - **실시간 추론(Real-Time Inference)**: 오토스케일링을 지원하는, 저지연·지속적 트래픽 예측용.
  - **배치 트랜스폼(Batch Transform)**: 대량의 데이터를 비동기적으로 처리하기 위한 방식.
  - **비동기 추론(Asynchronous Inference)**: 큰 페이로드가 있는 장시간 실행 추론 요청을, 즉각적인 응답 없이 처리하는 방식.
  - **서버리스 추론(Serverless Inference)**: 간헐적인 트래픽에서, 인프라 관리 없이 모델이 자동으로 스케일링되는 방식.
- Bedrock 배포 메커니즘:
  - **온디맨드 추론(On-Demand Inference)**: 입력/출력 토큰 수에 따라 요금이 부과되는 종량제 추론. 사용량이 적거나 산발적일 때 이상적입니다.
  - **프로비저닝된 처리량(Provisioned Throughput)**: 커스텀 또는 파인튜닝된 모델에 필수적이며, 일관되고 높은 처리량의 추론을 위한 보장된 용량을 제공합니다.
  - **Bedrock Agents**: 다단계 워크플로를 위한 에이전트를 배포하며, Amazon Kendra나 AWS Lambda 같은 도구와 모델을 통합하여 복잡한 작업을 처리합니다.

- **도구**:
  - **AWS API Gateway**: 애플리케이션과 통합할 수 있도록 모델을 API 엔드포인트로 노출합니다.

- **도구**:
  - **AWS API Gateway (선택 사항)**: 모델을 RESTful API로 노출하여, 다른 애플리케이션이나 마이크로서비스와의 원활한 통합을 가능하게 합니다. 선택 사항이며, 일반적으로 외부 애플리케이션이 여러분의 모델 엔드포인트와 상호작용해야 할 때 사용됩니다.
  - SageMaker 배포: 모델은 Amazon ECR에 저장된 Docker 이미지로 배포되며, 유즈 케이스에 따라 Lambda(서버리스 추론용), EC2, EKS(Elastic Kubernetes Service), ECS(Elastic Container Service)로 배포됩니다.
  - 인스턴스 유형:
    - Inf1: AWS Inferentia 칩을 사용한 비용 효율적이고 고성능의 딥러닝 추론에 최적화되어 있습니다.
    - P4: NVIDIA A100 GPU 기반으로, 매우 낮은 지연 시간의 대규모 고성능 추론에 이상적입니다.
    - G5: GPU 기반 워크로드용으로 설계되었으며, NVIDIA GPU를 이용한 그래픽 및 머신러닝 추론에 최적화되어 있습니다.
    - Graviton2 (C6g, M6g): 범용 머신러닝 추론 작업을 위한 에너지 효율적인 ARM 기반 인스턴스입니다.
  - SageMaker Endpoints: 배포 후, 모델은 실시간 추론이나 배치 트랜스폼 작업을 위해 SageMaker Endpoints로 서빙됩니다.
  - Bedrock 배포:
    - AWS Lambda: 다단계 워크플로의 자동화를 위해 Bedrock Agents와 함께 자주 통합됩니다.
    - Amazon Kendra: Bedrock Agents를 배포할 때, Amazon Kendra는 문서 검색 및 지식 기반 작업에 자주 사용됩니다.
    - Provisioned Throughput 도구: AWS Management Console이나 Bedrock API를 통해 고처리량 애플리케이션을 위한 추론 용량을 프로비저닝합니다.

> - **Description**: Deploy the trained model to make predictions.
>
> - SageMaker Deployment Options:
>   - **Real-Time Inference**: For low-latency, sustained traffic predictions with auto-scaling capabilities.
>   - **Batch Transform**: For processing large batches of data asynchronously.
>   - **Asynchronous Inference**: For long-running inference requests with large payloads, handled without immediate responses.
>   - **Serverless Inference**: For intermittent traffic, where the model scales automatically without infrastructure management.
> - Bedrock Deployment Mechanisms:
>   - **On-Demand Inference**: Pay-per-use inference based on the number of input/output tokens. Ideal for low or sporadic usage.
>   - **Provisioned Throughput**: Required for custom or fine-tuned models, providing guaranteed capacity for consistent, high-throughput inference.
>   - **BedRock Agent**s: Deploy agents for multi-step workflows, integrating models with tools like Amazon Kendra and AWS Lambda to handle complex tasks.
>
> - **Tools**:
>   - **AWS API Gateway**: Expose model as an API endpoint for integration with applications.
>
> - **Tools**:
>   - **AWS API Gateway (Optional)**: Used to expose models as RESTful APIs, enabling seamless integration with other applications or microservices. It's optional and typically used when you want external applications to interact with your model endpoint.
>   - SageMaker Deployment: Models are deployed via Docker images stored in Amazon ECR and deployed to Lambda (for Serverless Inference), EC2, EKS (Elastic Kubernetes Service), or ECS (Elastic Container Service), depending on use cases.
>   - Instance Types:
>     - Inf1: Optimized for cost-effective, high-performance deep learning inference using AWS Inferentia chips.
>     - P4: Powered by NVIDIA A100 GPUs, ideal for large-scale, high-performance inference with very low latency.
>     - G5: Designed for GPU-based workloads, optimized for graphics and machine learning inference with NVIDIA GPUs.
>     - Graviton2 (C6g, M6g): Energy-efficient, ARM-based instances for general-purpose machine learning inference tasks.
>   - SageMaker Endpoints: After deployment, models are served via SageMaker Endpoints for real-time inference or batch transform jobs.
>   - Bedrock Deployment:
>     - AWS Lambda: Often integrated with Bedrock for Bedrock Agents to enable automation in multi-step workflows.
>     - Amazon Kendra: When deploying Bedrock Agents, Amazon Kendra is often used for document search and knowledge-based tasks.
>     - Provisioned Throughput Tools: Provisioning inference capacity for high-throughput applications via AWS Management Console or Bedrock API.

### 8. 모델 모니터링 (Monitor the Model)
- **설명**: 모델의 성능을 지속적으로 모니터링하고, 데이터 또는 개념 드리프트를 감지합니다.
- **주요 활동**:
  - 데이터 및 개념 드리프트에 대해 모델을 실시간으로 모니터링합니다.
  - 알림을 설정하고, 성능이 저하되면 자동으로 대응 조치를 취합니다.

- **드리프트 유형**:
  - **데이터 드리프트(Data Drift)**: 입력 데이터가 변하지만 입력과 출력 사이의 관계는 그대로 유지되는 경우 (예: 인구 통계 분포가 달라짐).
  - **개념 드리프트(Concept Drift)**: 입력과 출력 사이의 관계 자체가 변하는 경우로, 모델이 학습한 패턴이 더 이상 통하지 않게 됨을 의미합니다 (예: 모델이 학습하지 못한 새로운 유형의 사기 패턴).

- **도구**:
  - **SageMaker Model Monitor**: 데이터 드리프트를 스케줄링하고 모니터링하며, 결과를 CloudWatch로 보내고, 대응 조치를 자동화합니다.

> - **Description**: Continuously monitor the model's performance and detect any data or concept drift.
> - **Key Activities**:
>   - Monitor model in real-time for data and concept drift.
>   - Set alerts and automate corrective actions if performance degrades.
>
> - **Types of Drift**:
>   - Data Drift: The input data changes, but the relationship between inputs and outputs remains the same (e.g., a different demographic).
>   - Concept Drift: The relationship between inputs and outputs changes, meaning the model's learned patterns no longer apply (e.g., new patterns of fraud that the model wasn't trained on).
>
> - **Tools**:
>   - **SageMaker Model Monitor**: Schedule and monitor data drift, send results to CloudWatch, and automate corrective measures.

---

### MLOps 및 자동화 (MLOps and Automation)
- **설명**: 머신러닝 모델의 전체 라이프사이클을 관리하기 위해 DevOps 원칙을 적용하며, 자동화·버전 관리·모니터링에 초점을 둡니다.
- **주요 활동**:
  - 모델의 배포·모니터링·재학습을 자동화합니다.
  - 모델 업데이트에 대한 지속적 통합/배포(CI/CD)를 보장합니다.
  - 여러 모델 버전을 관리하기 위한 버전 관리를 구현합니다.
- **도구**:
  - **SageMaker Pipelines**: ML 워크플로를 엔드투엔드로 자동화하고 관리합니다.
  - **AWS CodePipeline**: 모델의 빌드·테스트·배포 단계를 자동화합니다.
  - **SageMaker Model Registry**: 모델 버전과 메타데이터를 관리·추적합니다.
  - **Amazon S3**: SageMaker와 Bedrock 모두에서 학습 후 학습된 모델 아티팩트를 저장하는 데 사용됩니다. 가중치를 포함한 모델 출력물과 아티팩트를 S3로 내보내어 배포·평가 시 쉽게 접근할 수 있습니다.

> - **Description**: Apply DevOps principles to manage machine learning models throughout their lifecycle, focusing on automation, version control, and monitoring.
> - **Key Activities**:
>   - Automate deployment, monitoring, and retraining of models.
>   - Ensure continuous integration and delivery (CI/CD) for model updates.
>   - Implement version control to manage multiple model versions.
> - **Tools**:
>   - **SageMaker Pipelines**: Automate and manage the ML workflow end-to-end.
>   - **AWS CodePipeline**: Automate the build, test, and deploy phases for models.
>   - **SageMaker Model Registry**: Manage and track model versions and metadata.
>   - **Amazon S3**: Used to store trained model artifacts after training for both SageMaker and Bedrock. Model outputs, including weights and artifacts, are exported to S3 for easy access during deployment and evaluation.

---

### 모델 거버넌스와 설명 가능성 (Model Governance and Explainability)
- **설명**: ML 모델의 투명성, 책임성, 규제 준수를 보장하는 동시에, 모델의 동작을 이해관계자에게 설명 가능하게 만듭니다.
- **주요 활동**:
  - 모델 사용과 계보(lineage)를 추적하기 위한 거버넌스 프레임워크를 구현합니다.
  - 편향을 감지·완화하고, 공정성을 보장하며, 예측을 설명하기 위한 도구를 사용합니다.
  - 감사(audits)를 위해 모델 이력과 성능에 대한 명확한 문서를 제공합니다.
- **도구**:
  - **SageMaker Clarify**: _편향을 감지_하고, 모델 예측을 설명하며, 투명성을 높입니다.
  - **SageMaker Model Cards**: 학습된 모델에 대한 문서(성능 지표, 의도된 사용처 등)를 생성합니다.
  - **ML Governance from SageMaker**: ML 모델에 대한 더 강력한 통제와 가시성을 위한 도구를 제공하며, 모델 정보를 추적하고 편향과 같은 동작을 모니터링하는 데 도움을 줍니다.
  - **SageMaker ML Lineage Tracking**: 전체 워크플로를 캡처하여 재현성과 거버넌스를 위한 모델 계보를 추적합니다.
  - **Glue DataBrew**: 시각적 데이터 준비와 품질 규칙으로 데이터 거버넌스를 단순화합니다.
  - **AWS Audit Manager**: AWS 서비스의 감사를 자동화하여, 산업 규제에 대한 지속적인 컴플라이언스와 감사 준비 상태를 보장합니다.
  - **AWS Artifact**: 컴플라이언스 보고서와 계약서에 대한 온디맨드 접근을 제공하여, 조직이 컴플라이언스 요구사항을 충족하는 데 도움을 줍니다.
  - **AWS AI Service Cards**: AI 서비스와 모델에 대한 유즈 케이스, 제한 사항, 책임 있는 AI 관행, 성능 모범 사례 정보를 제공하여 투명성을 강화합니다.

> - **Description**: Ensure transparency, accountability, and regulatory compliance for ML models, while making their behavior interpretable to stakeholders.
> - **Key Activities**:
>   - Implement governance frameworks for tracking model usage and lineage.
>   - Use tools to detect and mitigate bias, ensure fairness, and explain predictions.
>   - Provide clear documentation of model history and performance for audits.
> - **Tools**:
>   - **SageMaker Clarify**: _Detect bias_, explain model predictions, and increase transparency.
>   - **SageMaker Model Cards**: Create documentation for trained models, including performance metrics and intended use.
>   - **ML Governance from SageMaker**: Provides tools for tighter control and visibility over ML models, helping track model information and monitor behavior like bias.
>   - **SageMaker ML Lineage Tracking**: Capture the entire workflow, tracking model lineage for reproducibility and governance.
>   - **Glue DataBrew**: Simplify data governance with visual data preparation and quality rules.
>   - **AWS Audit Manager**: Automates the auditing of AWS services, ensuring continuous compliance and audit readiness for industry regulations.
>   - **AWS Artifact**: Provides on-demand access to compliance reports and agreements, helping organizations meet compliance requirements.
>   - **AWS AI Service Cards**: Enhance transparency by providing information on use cases, limitations, responsible AI practices, and performance best practices for AI services and models.

---

### 비용 및 성능 최적화 (Cost and Performance Optimization)
- **설명**: 비용을 부풀리지 않으면서 자원 사용과 모델 성능을 최적화합니다.
- **주요 활동**:
  - 학습 비용을 낮추기 위해 관리형 스팟 학습(managed spot training)을 사용합니다.
  - 작업에 적합한 인스턴스 유형을 선택하고 오토스케일링 기능을 활용합니다.
  - 자원 활용의 비효율을 감지하기 위해 자원 모니터링을 사용합니다.
- **도구**:
  - **AWS Trusted Advisor**: 비용 및 성능 개선을 위한 권장 사항을 제공합니다.
  - **SageMaker Managed Spot Training**: 여유 AWS EC2 용량을 활용하여 학습 비용을 절감합니다.
  - **SageMaker Profiler**: 모델 학습 시 비효율적인 자원 사용을 식별합니다.
  - **Amazon Inspector**: ML 애플리케이션의 보안 평가를 자동화하며, 성능 저하나 보안 이슈로 이어질 수 있는 취약점을 식별합니다.

> - **Description**: Optimize resource usage and model performance without inflating costs.
> - **Key Activities**:
>   - Use managed spot training for lower-cost training jobs.
>   - Select appropriate instance types for the job and leverage auto-scaling capabilities.
>   - Use resource monitoring to detect inefficiencies in resource utilization.
> - **Tools**:
>   - **AWS Trusted Advisor**: Provides recommendations for cost and performance improvements.
>   - **SageMaker Managed Spot Training**: Reduce training costs by utilizing spare AWS EC2 capacity.
>   - **SageMaker Profiler**: Identify inefficient resource use during model training.
>   - **Amazon Inspector**: Automates security assessments of ML applications, identifying vulnerabilities that can lead to performance degradation or security issues.

---

### 지속 학습 및 재학습 (Continual Learning and Retraining)
- **설명**: 새로운 데이터와 변화하는 환경에 대응하기 위해 모델을 지속적으로 재학습시켜, 성능 저하를 방지합니다.
- **주요 활동**:
  - 새로운 데이터를 기반으로 정기적인 모델 재학습을 스케줄링합니다.
  - 성능 하락을 감지하고 자동 재학습 워크플로를 시작할 수 있는 도구를 사용합니다.
  - 개념 및 데이터 드리프트를 모니터링하여 모델 드리프트에 대응합니다.
- **도구**:
  - **SageMaker Model Monitor**: 데이터 드리프트를 감지하고 재학습 워크플로를 트리거합니다.
  - **SageMaker Pipelines**: 재학습 프로세스를 엔드투엔드로 자동화합니다.

> - **Description**: Continuously retrain models to account for new data and changing conditions, preventing performance degradation.
> - **Key Activities**:
>   - Schedule regular model retraining based on new data.
>   - Use tools to detect performance drops and initiate automatic retraining workflows.
>   - Handle model drift by monitoring for concept and data drift.
> - **Tools**:
>   - **SageMaker Model Monitor**: Detect data drift and trigger retraining workflows.
>   - **SageMaker Pipelines**: Automate retraining processes end-to-end.

---

### 보안 (Security)
- **설명**: 머신러닝 모델, 데이터, 관련 인프라를 보호하기 위한 보안 모범 사례를 구현합니다.

- **주요 활동**:
  - **최소 권한 원칙(Least Privilege Principle)**: IAM 역할과 정책이 특정 작업이나 기능에 필요한 권한만 부여하도록 보장합니다.
  - **PrivateLink 및 VPC 엔드포인트**: **SageMaker**를 인터넷 노출로부터 차단합니다. **PrivateLink**와 **VPC 엔드포인트**를 사용하여 프라이빗 네트워크 내에서 리소스에 안전하게 접근합니다.
  - **저장 및 전송 중 암호화(Encryption at Rest and in Transit)**: 기본적으로 **SageMaker**는 **KMS**(Key Management Service)를 사용하여 저장 및 전송 중인 데이터를 암호화합니다.
  - **IAM 역할 및 정책**: 모델 데이터와 리소스에 대한 안전한 접근을 보장하기 위해 IAM 역할과 정책을 생성·관리합니다.
  - **S3 Block Public Access**: **S3 Block Public Access** 설정이 잠재적 퍼블릭 접근을 무효화하도록 하여, 모델 데이터가 노출되는 것을 방지합니다.
  - **AWS IAM Identity Center**: ID 관리(identity management)를 중앙집중화하여 여러 AWS 계정에 접근할 수 있도록 하고, Active Directory와 통합합니다.

- **도구**:
  - **AWS Config**: AWS 리소스 전반의 구성 변경 사항을 지속적으로 모니터링·기록하여 컴플라이언스와 보안을 보장합니다.
  - **AWS CloudTrail**: API 호출을 로깅하고 사용자 활동을 추적하여 감사 및 컴플라이언스에 활용합니다.
  - **Amazon Inspector**: 머신러닝 환경의 취약점을 자동으로 스캔하여 배포된 모델의 보안을 보장합니다.
  - **AWS Audit Manager**: 감사를 자동화하고 감사 보고서를 생성하여 산업 규제 준수를 검증합니다.
  - **AWS Artifact**: ML 환경이 보안 및 규제 표준을 충족하도록 컴플라이언스 문서와 보안 보고서에 대한 접근을 제공합니다.
  - **SageMaker Role Manager**: SageMaker 리소스와 서비스에 대한 권한 및 역할 관리를 단순화합니다.

> - **Description**: Implement best security practices to safeguard machine learning models, data, and related infrastructure.
>
> - **Key Activities**:
>   - **Least Privilege Principle**: Ensure that IAM roles and policies grant only the permissions required for specific jobs or functions.
>   - **PrivateLink and VPC Endpoints**: Lock down **SageMaker** to prevent exposure to the internet. Use **PrivateLink** and **VPC endpoints** to securely access resources within your private network.
>   - **Encryption at Rest and in Transit**: By default, **SageMaker** encrypts data at rest and in transit using **KMS** (Key Management Service).
>   - **IAM Roles and Policies**: Create and manage IAM roles and policies to ensure secure access to model data and resources.
>   - **S3 Block Public Access**: Prevent model data from being exposed by ensuring **S3 Block Public Access** settings override any potential public access.
>   - **AWS IAM Identity Center**: Centralize identity management, allowing access to multiple AWS accounts, and integrate with Active Directory for identity management.
>
> - **Tools**:
>   - **AWS Config**: Continuously monitors and records configuration changes across AWS resources to ensure compliance and security.
>   - **AWS CloudTrail**: Logs API calls and tracks user activity for auditing and compliance.
>   - **Amazon Inspector**: Automatically scans for vulnerabilities in machine learning environments to ensure that deployed models are secure.
>   - **AWS Audit Manager**: Automates auditing and ensures compliance with industry regulations by generating audit reports for validation.
>   - **AWS Artifact**: Provides access to compliance documents and security reports to ensure that your ML environments meet security and regulatory standards.
>   - **SageMaker Role Manager**: Simplifies the management of permissions and roles for SageMaker resources and services.

---

## 서비스 (Services)

### AWS 관리형 AI 서비스 (AWS Managed AI Services)

AWS는 애플리케이션에 쉽게 통합될 수 있도록 설계된 다양한 관리형 AI 서비스를 제공하며, 이를 통해 깊은 머신러닝 전문 지식 없이도 강력한 AI 기능을 사용할 수 있습니다. 다음은 주요 서비스에 대한 개요입니다:

> AWS offers a range of managed AI services designed to be easily integrated into applications, providing powerful AI capabilities without the need for deep machine learning expertise. Here's an overview of key services:

#### 컴퓨터 비전 (Computer Vision)
- **AWS Rekognition**
  - 얼굴 비교 및 분석, 객체 및 텍스트 감지, 콘텐츠 검열. 폭력적이거나 부적절한 자료를 식별하는 _콘텐츠 스크리닝_에 유용합니다.

> - **AWS Rekognition**
>   - Facial comparison and analysis, object and text detection, content moderation. Good for _screening content_ such as identifying violent or inappropriate material.

#### 텍스트 및 문서 분석 (Text and Document Analysis)
- **AWS Textract** (OCR)
  - 스캔된 이미지를 텍스트로 변환하여 디지털 콘텐츠 관리를 가능하게 합니다.
- **Amazon Comprehend** (NLP)
  - 텍스트에서 핵심 문구, 엔터티(entity), 감정(sentiment)을 추출합니다. _피드백의 감정 분석_ 및 _PII 데이터 감지_에 유용합니다.
- **AWS Intelligent Document Processing** (IDP)
  - 다양한 문서 유형에서 데이터 추출·분류·처리를 자동화하는 AWS 서비스 모음입니다. 광학 문자 인식(OCR), 자연어 처리(NLP), 머신러닝(ML) 같은 AI 기술을 활용하여 PDF, 청구서, 법률 계약서 같은 문서의 비정형 데이터를 처리합니다.

> - **AWS Textract** (OCR)
>   - Converts scanned images to text, enabling digital content management.
> - **Amazon Comprehend** (NLP)
>   - Extracts key phrases, entities, and sentiment from text. Useful for analyzing _sentiment of feedback_ and detecting _PII data_.
> - **AWS Intelligent Document Processing** (IDP)
>   - A group of AWS services that together automate the extraction, classification, and processing of data from various document types. It leverages AI technologies such as Optical Character Recognition (OCR), Natural Language Processing (NLP), and Machine Learning (ML) to handle unstructured data found in documents like PDFs, invoices, and legal contracts.

#### 언어 AI (Language AI)
- **Amazon Lex**
  - 음성과 텍스트 모두를 위한 대화형 인터페이스를 구축하며, _챗봇_ 생성에 이상적입니다.
- **Amazon Transcribe**
  - 음성-텍스트 변환(Speech-to-Text) 서비스로, _오디오용 자막(captions) 생성_에 완벽합니다.
- **Amazon Polly**
  - 텍스트를 실감 나는 음성으로 변환하여, 음성을 통한 사용자 참여를 향상시킵니다.

> - **Amazon Lex**
>   - Builds conversational interfaces for both voice and text, ideal for creating _chatbots_.
> - **Amazon Transcribe**
>   - Speech to text service, perfect for creating _captions for audio_.
> - **Amazon Polly**
>   - Converts text into lifelike speech, enhancing user engagement through voice.

#### 고객 경험 (Customer Experience)
- **Amazon Kendra**
  - 지능형 문서 검색 기능을 제공합니다.
- **Amazon Personalize**
  - 개인화된 상품 추천 기능을 제공하며, "이 상품도 좋아하실 것 같아요" 같은 기능과 유사합니다.
- **Amazon Translate**
  - 언어 번역을 지원하여 글로벌 사용자와의 상호작용을 돕습니다.

> - **Amazon Kendra**
>   - Provides intelligent document search capabilities.
> - **Amazon Personalize**
>   - Offers personalized product recommendations, akin to "you may also like" features.
> - **Amazon Translate**
>   - Facilitates language translation, supporting global user interaction.

#### 비즈니스 지표 (Business Metrics)
- **Amazon Forecast**
  - _재고 수준_처럼 시계열 데이터의 미래 지점을 예측합니다.
- **Amazon Fraud Detection**
  - 온라인 거래와 신규 계정 생성 등 다양한 시나리오에서 잠재적 사기(fraud)를 감지합니다.

> - **Amazon Forecast**
>   - Predicts future points in time-series data, such as _inventory levels_.
> - **Amazon Fraud Detection**
>   - Detects potential fraud in various scenarios including online transactions and new account creations.

#### Amazon Q

- **Amazon Q Business**
  - S3, SharePoint, Salesforce 같은 엔터프라이즈 데이터 소스에 접근하여, 질문 답변·콘텐츠 생성·워크플로 자동화 등의 작업을 지원하는 생성형 AI 기반 어시스턴트입니다.
- **Amazon Q Developer**
  - 개발자를 위한 도구로, 코드 생성과 보안 스캔 같은 기능을 포함하여 개발 및 테스트 관련 작업 자동화를 지원합니다.
- **Amazon Q in QuickSight**
  - Amazon QuickSight와 통합되어 자연어 쿼리를 지원합니다. 사용자가 BI 관련 질문을 하면 QuickSight 데이터에서 AI를 이용해 인사이트를 생성해 줍니다.
- **Amazon Q in Connect**
  - Amazon Connect와 통합되어, 자연어 AI로 고객 문의에 답변하고 응답을 자동화하며 티켓을 관리하는 등 고객 서비스 향상에 도움을 줍니다.
- **Amazon Q in AWS Supply Chain**
  - AWS Supply Chain에 통합되어, 공급망 데이터에서 인사이트를 생성하고 재고 관리를 간소화하며 수요를 예측하는 등 공급망 관리의 최적화·자동화를 지원합니다.

> - **Amazon Q Business**
>   - A generative AI-powered assistant that helps with tasks like answering questions, generating content, and automating workflows by accessing enterprise data sources like S3, SharePoint, and Salesforce.
> - **Amazon Q Developer**
>   - A tool for developers that includes features like code generation and security scanning to help automate tasks related to development and testing.
> - **Amazon Q in QuickSight**
>   - Integrated with Amazon QuickSight for natural language querying, allowing users to ask business intelligence-related questions and generate insights from their QuickSight data with AI.
> - **Amazon Q in Connect**
>   - Integrated with Amazon Connect, Amazon Q helps improve customer service by answering customer inquiries, automating responses, and managing tickets using natural language AI.
> - **Amazon Q in AWS Supply Chain**
>   - Integrated into AWS Supply Chain, Amazon Q assists in optimizing and automating supply chain management by generating insights from supply chain data, streamlining inventory management, and forecasting demand.

---

### Amazon SageMaker

Amazon SageMaker는 개발자와 데이터 과학자가 머신러닝 모델을 대규모로 구축·학습·배포할 수 있게 해 주는 통합 머신러닝 서비스입니다. 사용자는 처음부터 커스텀 모델을 만들거나, SageMaker JumpStart를 통해 기존 모델을 사용하고 파인튜닝할 수 있습니다. 이 플랫폼은 AWS Rekognition 같은 고수준 AI 서비스보다 더 많은 제어권을 제공하여, 특정 프로젝트 요구사항에 맞는 세밀한 커스터마이징과 최적화가 가능합니다.

> Amazon SageMaker is an integrated machine learning service that enables developers and data scientists to build, train, and deploy machine learning models at scale. Users can create custom models from scratch or use and fine-tune existing ones through SageMaker JumpStart. This platform offers more control than high-level AI services like AWS Rekognition, allowing for detailed customization and optimization to meet specific project requirements.

#### SageMaker Studio

SageMaker Studio는 머신러닝을 위한 통합 개발 환경(IDE)으로, 데이터 준비·모델 구축·학습·튜닝·배포를 하나의 인터페이스에서 수행할 수 있게 해 줍니다. 코드 개발용 Jupyter 노트북, 통합 디버깅 도구, 실험 관리 같은 기능을 협업 가능한 클라우드 기반 환경 안에서 제공합니다. Studio는 또한 실시간 협업을 지원하고, 모델 모니터링과 데이터 준비를 포함한 다양한 SageMaker 기능에 쉽게 접근할 수 있게 해 줍니다.

> SageMaker Studio is an integrated development environment (IDE) for machine learning, providing a single interface for preparing data, building models, training, tuning, and deploying them. It offers features like Jupyter notebooks for code development, integrated debugging tools, and experiment management, all within a collaborative, cloud-based environment. Studio also supports real-time collaboration and easy access to various SageMaker capabilities, including model monitoring and data preparation.

#### 학습 프로세스 (Training Process)

일반적인 SageMaker 학습 프로세스는 학습 작업을 구성·관리하는 데 도움이 되는 여러 핵심 요소를 포함합니다:

- **학습 데이터 위치(Training Data Locations)**: 데이터는 일반적으로 Amazon S3에 저장되며, S3 URL을 통해 접근합니다.
- **ML 컴퓨트 인스턴스(ML Compute Instances)**: SageMaker는 확장 가능한 컴퓨팅 성능을 위해 EC2 인스턴스(ECR 인스턴스)를 활용합니다.
- **학습 이미지(Training Images)**: 학습 프로세스는 머신러닝을 위해 특별히 설계된 Docker 컨테이너 이미지를 사용하여 실행됩니다.
- **하이퍼파라미터(Hyperparameters)**: 학습 프로세스를 이끄는 파라미터(예: 학습률, 배치 크기).
- **S3 출력 버킷(S3 Output Bucket)**: 학습된 모델 아티팩트는 나중에 사용될 수 있도록 S3 버킷에 저장됩니다.

> The typical SageMaker training process includes several key elements that help configure and manage the training jobs:
>
> - **Training Data Locations**: Data is typically stored in Amazon S3 and accessed via S3 URLs.
> - **ML Compute Instances**: SageMaker leverages EC2 instances (ECR instances) for scalable compute power.
> - **Training Images**: The training process is run using Docker container images specifically designed for machine learning.
> - **Hyperparameters**: Parameters that guide the learning process (e.g., learning rate, batch size).
> - **S3 Output Bucket**: The trained model artifacts are stored in an S3 bucket for later use.

#### 기능 (Features)
- **SageMaker Feature Store**
  - 머신러닝 피처를 저장·검색·공유하기 위한 중앙 저장소.
- **SageMaker Model Registry**
  - 모델의 다양한 버전과 메타데이터를 관리합니다.
- **SageMaker Pipelines**
  - 반복 가능한 워크플로로 모델을 구축·학습·배포하기 위한 워크플로 오케스트레이션 서비스를 제공합니다.
- **SageMaker Model Monitor**
  - 내장 규칙을 활용해 데이터 드리프트를 감지하거나 커스텀 규칙을 생성할 수 있으며, 모니터링 결과를 CloudWatch로 전송하고 대응 조치를 자동화합니다.
- **SageMaker Ground Truth**
  - 실제 사람이 데이터를 라벨링하도록 하여, 고품질 학습 데이터셋을 보장합니다.
- **SageMaker Canvas**
  - 기술 전문성이 부족해도 자신의 데이터로 모델을 만들 수 있도록 해 주는 시각적 노코드(no-code) 도구.
- **SageMaker JumpStart**
  - 사전 학습된 모델에 접근할 수 있는 허브로, 머신러닝 솔루션을 쉽게 배포할 수 있게 해 줍니다.
- **SageMaker Clarify**
  - 편향을 감지하고 예측을 설명하여 투명성을 높이는 데 도움을 주는 도구.
- **SageMaker Role Manager**
  - SageMaker 리소스와 서비스에 대한 권한을 관리합니다.
- **SageMaker Model Cards**
  - 학습된 모델에 대한 투명한 문서를 생성합니다.
- **SageMaker ML Lineage Tracking**
  - ML 모델의 계보(lineage)를 추적하여, 모델 거버넌스를 확립하고 워크플로를 재현하며 작업 이력을 유지합니다.
- **SageMaker Model Dashboard**
  - 모든 모델 관련 활동을 관리·모니터링할 수 있는 통합 인터페이스를 제공합니다.
- **SageMaker Data Wrangler**
  - 머신러닝을 위한 데이터 준비 과정을 단순화하여, 빠르고 쉬운 데이터 정제·변환·시각화를 가능하게 합니다.
- **SageMaker Experiments (현재는 MLflow with Amazon SageMaker로 명명됨)**
  - 반복적인 ML 실험을 추적·정리·조회·분석·비교합니다.
- **SageMaker Autopilot**
  - 프로세스에 대한 완전한 가시성과 제어권을 제공하면서, 머신러닝 모델을 자동으로 구축·학습·튜닝합니다.
- **Amazon Augmented AI (A2I)**
  - 신뢰도가 낮은 예측이나 무작위 샘플에 대해 사람의 검토를 추가하여, 더 정확한 결과를 보장합니다.
- **SageMaker Managed Spot Training**
  - 여유 AWS EC2 용량을 사용하여 모델 학습 비용을 절감합니다.
- **SageMaker Profiler**
  - 학습 작업에서 자원의 비효율을 식별하여, 속도나 정확도를 희생하지 않고 비용을 최소화합니다.

> - **SageMaker Feature Store**
>   - Central repository for storing, retrieving, and sharing machine learning features.
> - **SageMaker Model Registry**
>   - Manages different versions of models and their metadata.
> - **SageMaker Pipelines**
>   - Provides a workflow orchestration service for building, training, and deploying models with repeatable workflows.
> - **SageMaker Model Monitor**
>   - Utilizes built-in rules to detect data drift or create custom rules, monitoring results can be sent to CloudWatch, and automates corrective measures.
> - **SageMaker Ground Truth**
>   - Leverages actual humans for labeling data, ensuring high-quality training datasets.
> - **SageMaker Canvas**
>   - A visual, no-code tool that allows users to build models based on their data with less technical expertise.
> - **SageMaker JumpStart**
>   - Access to PreTrained Models and a hub for easily deploying machine learning solutions.
> - **SageMaker Clarify**
>   - Tools to help detect biases and explain predictions to increase transparency.
> - **SageMaker Role Manager**
>   - Manages permissions for SageMaker resources and services.
> - **SageMaker Model Cards**
>   - Create transparent documentation for trained models.
> - **SageMaker ML Lineage Tracking**
>   - Tracks the lineage of ML models to establish model governance, reproduce workflows, and maintain work history.
> - **SageMaker Model Dashboard**
>   - Provides a unified interface to manage and monitor all model-related activities.
> - **SageMaker Data Wrangler**
>   - Simplifies the process of data preparation for machine learning, enabling quick and easy data cleaning, transformation, and visualization.
> - **SageMaker Experiments (Now called MLflow with Amazon SageMaker)**
>   - Tracks, organizes, views, analyzes, and compares iterative ML experimentation.
> - **SageMaker Autopilot**
>   - Automatically builds, trains, and tunes machine learning models while giving you full visibility and control over the process.
> - **Amazon Augmented AI (A2I)**
>   - Allows you to add human review for low-confidence predictions or random samples, ensuring more accurate results.
> - **SageMaker Managed Spot Training**
>   - Reduces the cost of training models by using spare AWS EC2 capacity.
> - **SageMaker Profiler**
>   - Identifies resource inefficiencies in training jobs to minimize cost without sacrificing speed or accuracy.

---

### Amazon Bedrock

Amazon Bedrock은 단일 API를 통해 주요 AI 기업의 고성능 파운데이션 모델(FM, Foundation Models)에 접근할 수 있게 해 주는 완전 관리형·서버리스 서비스입니다. 보안, 프라이버시, 책임 있는 AI를 우선시하며, 생성형 AI 애플리케이션 개발을 손쉽게 해 주도록 설계되었습니다.

> Amazon Bedrock is a fully managed, serverless service that provides access to high-performing foundation models (FMs) from leading AI companies through a single API. It is designed to facilitate the creation of generative AI applications, prioritizing security, privacy, and responsible AI.

#### 가격 (Pricing)
- **Pay-as-you-go (사용한 만큼 지불)**: Amazon Bedrock은 추론 중 사용된 **입력 및 출력 토큰**의 수에 따라 요금을 부과합니다. 즉, 파운데이션 모델을 사용할 때 처리된 토큰에 대해서만 비용을 지불합니다.
- **파인튜닝된 모델(Fine-tuned models)**: **커스텀 또는 파인튜닝된 모델**을 사용하는 경우, **Provisioned Throughput**에 대한 추가 요금이 적용됩니다. 이는 일관된 성능과 추론용 예약 용량을 보장합니다.

> - **Pay-as-you-go**: Amazon Bedrock charges based on the number of **input and output tokens** used during inference. This means you only pay for the tokens processed when using the foundation models.
> - **Fine-tuned models**: If you are using a **custom or fine-tuned model**, additional charges apply for **Provisioned Throughput**, which guarantees consistent performance and reserved capacity for inference.

#### 기능 (Features)
- **모델 선택(Model Choice)**
  - AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, Amazon 등 다양한 파운데이션 모델에 접근할 수 있어, 특정 애플리케이션 요구사항에 따라 최적의 모델을 선택할 수 있습니다.
  - Amazon Titan Models
    - Amazon Bedrock 전용인 Amazon Titan 모델은 AWS가 만든 사전 학습된 고성능 파운데이션 모델로, 책임 있는 AI 관행에 기반한 광범위한 유즈 케이스를 위해 설계되었습니다.
- **커스터마이징(Customization)**
  - 파인튜닝과 검색 증강 생성(RAG, Retrieval Augmented Generation) 같은 기법을 사용하여, 자신의 데이터로 파운데이션 모델을 비공개로 커스터마이징함으로써 관련성과 정확성을 향상시킬 수 있습니다.
- **파운데이션 모델 평가(Foundation Model Evaluation)**
  - Amazon Bedrock의 모델 평가 기능을 사용하면, 특정 유즈 케이스에 가장 적합한 파운데이션 모델을 평가·비교·선택할 수 있습니다. 정확도, 견고성(robustness), 유해성(toxicity)과 같은 커스텀 지표로 모델을 평가하여 성능 요구사항을 충족하는지 확인할 수 있습니다. Amazon SageMaker Clarify와 fmeval과의 통합은 편향 및 설명 가능성 검사를 통해 모델 평가를 추가로 지원합니다.
- **Bedrock Knowledge Bases**
  - 검색 증강 생성(RAG)을 사용하여 프라이빗 소스에서 데이터를 가져와, 더 관련성 있고 정확한 응답을 제공합니다. 데이터 수집, 검색, 프롬프트 증강까지 RAG 워크플로 전체를 지원합니다.
  - 관련 있는 외부 지식을 생성 모델에 가져오는 검색 프로세스를 통합하여 출력을 강화합니다.
- **Bedrock Agents**
  - 회사 시스템과 데이터 소스를 사용하여 다단계 작업을 계획하고 실행할 수 있는 에이전트를 생성합니다. 고객 문의, 주문 처리와 같은 복잡한 작업을 간소화합니다.
- **서버리스(Serverless)**
  - 인프라 관리가 필요하지 않아, AI 기능의 배포와 확장을 단순화합니다.
- **보안 및 프라이버시 가드레일(Security and Privacy Guardrails)**
  - AI 출력을 제한하는 강력한 통제 기능을 제공하여, 부적절한 콘텐츠 생성을 방지하고 금융 추천 같은 민감한 조언을 제한함으로써 윤리적이고 규정을 준수하는 AI 사용을 보장합니다.
- **PartyRock**
  - Amazon Bedrock으로 구동되는 실습형 AI 앱 빌딩 놀이터로, 사용자가 코드를 작성하지 않고도 생성형 AI 앱을 빠르게 만들고 모델을 실험해 볼 수 있습니다.

> - **Model Choice**
>   - Access a variety of foundation models from AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon, allowing for optimal model selection based on specific application needs.
>   - Amazon Titan Models
>     - Exclusive to Amazon Bedrock, Amazon Titan models are pretrained, high-performing foundation models created by AWS, designed for a wide range of use cases with responsible AI practices.
> - **Customization**
>   - Customize foundation models privately with your data using techniques such as fine-tuning and Retrieval Augmented Generation (RAG), enhancing the model's relevance and accuracy.
> - **Foundation Model Evaluation**
>   - Model Evaluation on Amazon Bedrock allows you to evaluate, compare, and select the best foundation models for your specific use case. You can assess models based on custom metrics such as accuracy, robustness, and toxicity, ensuring they meet your performance requirements. Integration with Amazon SageMaker Clarify and fmeval further supports model evaluation by checking for bias and explainability.
> - **Bedrock Knowledge Bases**
>   - Uses Retrieval Augmented Generation (RAG) to fetch data from private sources, delivering more relevant and accurate responses with full support for the RAG workflow—handling data ingestion, retrieval, and prompt augmentation.
>   - Enhances outputs by integrating retrieval processes that pull relevant external knowledge into the generative model.
> - **Bedrock Agents**
>   - Create agents capable of planning and executing multistep tasks using company systems and data sources—streamlining complex tasks such as customer inquiries and order processing.
> - **Serverless**
>   - Eliminates the need for infrastructure management, simplifying the deployment and scaling of AI capabilities.
> - **Security and Privacy Guardrails**
>   - Features robust controls to restrict AI outputs, preventing the generation of inappropriate content and restricting sensitive advice like financial recommendations, ensuring ethical and compliant AI usage.
> - **PartyRock**
>   - A hands-on AI app-building playground powered by Amazon Bedrock, where users can quickly build generative AI apps and experiment with models without writing code.

---

### AWS Glue

AWS Glue는 완전 관리형·클라우드 최적화 ETL(Extract, Transform, Load) 서비스로, 분석 및 AI 모델을 위한 데이터를 준비하고 로드하는 데 도움을 줍니다.

> AWS Glue is a fully managed, cloud-optimized ETL (Extract, Transform, Load) service that helps prepare and load data for analytics and AI models.

#### 기능 (Features)

- **AWS Glue ETL 서비스**
  - 중복 제거, 결측치 채우기 같은 내장 변환을 갖춘 클라우드 기반 ETL 데이터 준비 서비스입니다.
  - 예시 워크플로: AWS Kinesis Data Streams → AWS Glue ETL Job → CSV to Parquet → S3 Data Lake.
- **AWS Glue Data Catalog**
  - ETL 작업을 관리·모니터링하기 위한 중앙 저장소이며, 내장 분류기(classifiers)와 함께 메타데이터(데이터가 아닌 스키마)를 저장합니다.
- **AWS Glue Databrew**
  - 데이터 준비, 데이터 품질 규칙 정의, 변환을 "레시피(recipes)"로 저장할 수 있는 시각적 도구입니다.
- **AWS Glue Data Quality**
  - 이상치를 감지하고 데이터 품질 규칙을 추천하여, AI 모델을 위한 깨끗하고 고품질의 데이터를 보장합니다.

> - **AWS Glue ETL Service**
>   - Cloud-based ETL service for data preparation with built-in transformations like dropping duplicates and filling missing values.
>   - Example Workflow: AWS Kinesis Data Streams -> AWS Glue ETL Job -> CSV to Parquet -> S3 Data Lake.
> - **AWS Glue Data Catalog**
>   - Centralized repository for managing and monitoring ETL jobs, storing metadata (schemas, not data) with built-in classifiers.
> - **AWS Glue Databrew**
>   - Visual tool for data preparation, defining data quality rules, and saving transformations as "recipes."
> - **AWS Glue Data Quality**
>   - Detects anomalies and recommends data quality rules for ensuring clean, high-quality data for AI models.
---

## 표 (Tables)

### 전통적 ML vs 딥러닝 (Traditional ML vs Deep Learning)

**[한글]**

| 카테고리          | 전통적 ML                                    | 딥러닝                                          |
|-------------------|-----------------------------------------------|-------------------------------------------------|
| **작업 복잡도**   | 잘 정의된 작업                                 | 복잡한 작업                                     |
| **데이터 유형**   | 정형/라벨링된 데이터                           | 비정형 데이터 (이미지, 비디오, 텍스트)          |
| **방법론**        | 통계와 수학을 통해 문제 해결                    | 신경망을 활용                                    |
| **피처 처리**     | 피처를 수동으로 선택·추출                       | 모델이 피처를 자동으로 학습                       |
| **비용**          | 상대적으로 낮은 비용                           | 연산 요구량이 크므로 비용이 높음                  |

**[English]**

| Category          | Traditional ML                                      | Deep Learning                                 |
|-------------------|-----------------------------------------------------|-----------------------------------------------|
| **Task Complexity** | Well-defined tasks                                  | Complex tasks                                 |
| **Data Type**      | Structured / Labeled Data                           | Unstructured Data (Images, Video, Text)       |
| **Methodology**    | Solves problems through statistics and mathematics  | Utilizes neural networks                      |
| **Feature Handling** | Manually select and extract features                | Features are learned automatically by the model |
| **Cost**           | Less costly                                         | Higher costs due to computational demands     |


### 머신러닝의 유형 (Types of Machine Learning)

**[한글]**

| 학습 유형             | 설명                                           | 도전 과제                              | AWS 도구                | 흔한 활용 사례                                        |
|-----------------------|------------------------------------------------|----------------------------------------|-------------------------|------------------------------------------------------|
| **지도학습(Supervised)** | 사전 라벨링된 데이터로 모델을 학습.             | 데이터 라벨링이 어려울 수 있음.         | SageMaker Ground Truth  | 이미지 분류, 스팸 탐지                                |
| **비지도학습(Unsupervised)** | 라벨링되지 않은 데이터에서 패턴을 찾음.     | 패턴을 해석하는 방법이 필요함.          | 특정 도구 없음           | 클러스터링, 이상 탐지, LLM 초기 학습 단계             |
| **강화학습(Reinforcement)** | 시행착오를 통해 보상을 극대화하며 학습.       | 에이전트가 상호작용할 환경이 필요함.    | AWS DeepRacer           | 게임, 로보틱스, 실시간 의사결정                       |

**[English]**

| Learning Type         | Description                                          | Challenges                            | AWS Tools              | Common Use Cases                   |
|-----------------------|------------------------------------------------------|---------------------------------------|------------------------|------------------------------------|
| **Supervised Learning** | Uses pre-labeled data to train models.               | Labelling the data can be challenging. | SageMaker Ground Truth | Image classification, spam detection |
| **Unsupervised Learning** | Works with unlabeled data to find patterns.         | Requires methods to interpret patterns.| None specific          | Clustering, anomaly detection, LLMs for initial training phases |
| **Reinforcement Learning** | Learns through trial and error to maximize rewards. | Requires environment for agent interaction. | AWS DeepRacer      | Gaming, robotics, real-time decisions |


### 확산 모델의 유형 (Types of Diffusion Models)

**[한글]**

| 확산 모델 유형           | 설명                                                | 사용 시점                                   | 비고                    |
|--------------------------|-----------------------------------------------------|---------------------------------------------|-------------------------|
| **순방향 확산(Forward)** | 데이터에 점진적으로 노이즈를 추가.                    | 자주 사용되지 않음 (노이즈를 추가하는 방식)  |                         |
| **역방향 확산(Reverse)** | 노이즈로부터 원본 데이터를 복원.                      | 왜곡된 입력으로부터 상세한 이미지 생성.       | 이미지 복원 도구        |
| **Stable Diffusion**     | 픽셀 자체가 아닌 축소된 잠재 공간(latent space)에서 동작. | 역방향 확산보다 우수                          | Midjourney, DALL-E      |

**[English]**

| Diffusion Model Type | Description                                          | When to Use                                  | Notes                 |
|----------------------|------------------------------------------------------|----------------------------------------------|--------------------------|
| **Forward Diffusion**| Adds noise to data progressively.                    | Not often used (it adds noise)    |   |
| **Reverse Diffusion**| Reconstructs original data from noise.               | Creating detailed images from distorted inputs. | Image restoration tools |
| **Stable Diffusion** | Works in reduced latent space, not directly in pixels. | Better then Reverse Diffusion | Midjourney, DALL-E       |


### Amazon SageMaker 추론 방식 (Amazon SageMaker Inference Methods)

**[한글]**

| 추론 유형              | 배포 대상            | 특징                                                                         |
|------------------------|----------------------|------------------------------------------------------------------------------|
| **배치(Batch)**        | EC2                  | 대규모 작업을 드물게 수행할 때 비용 효율적                                     |
| **비동기(Asynchronous)** | EC2                | 시간에 민감하지 않고 페이로드가 큰 애플리케이션에 적합                          |
| **서버리스(Serverless)** | Lambda              | 간헐적 트래픽, 무트래픽 구간, 기본으로 오토스케일링 제공                        |
| **실시간(Real-Time)**    | EC2                  | 라이브 예측, 지속적 트래픽, 저지연, 일관된 성능                                   |

**[English]**

| Inference Type     | Deployed To         | Characteristics                                                         |
|--------------------|---------------------|-------------------------------------------------------------------------|
| **Batch**          | EC2                 | Cost-effective for infrequent, large jobs                               |
| **Asynchronous**   | EC2                 | Suitable for non-time-sensitive applications and large payload          |
| **Serverless**     | Lambda              | Intermittent traffic, periods of no traffic, auto-scaling out of the box|
| **Real-Time**      | EC2                 | Live predictions, sustained traffic, low latency, consistent performance|


### 머신러닝/AI를 위한 학습 데이터 유형 (Types of Training Data for Machine Learning/AI)

**[한글]**

| 데이터 유형          | AWS 데이터 소스 예시                              | 실제 예시                                     |
|----------------------|---------------------------------------------------|-----------------------------------------------|
| **정형(Structured)** | RDS에 저장 후 S3로 이동된 SQL 데이터              | 관계형 테이블의 고객 정보                     |
| **반정형(Semi-Structured)** | DynamoDB나 DocumentDB에 있다가 S3로 이동된 데이터 | 사용자 활동의 JSON 로그                       |
| **비정형(Unstructured)** | S3에 직접 저장된 객체 및 파일                    | 이미지, 비디오, PDF 문서                       |
| **시계열(Time-Series)** | S3에 저장된 타임스탬프 데이터                     | IoT 디바이스 데이터, 주식 시장 데이터          |

**[English]**

| Data Type       | AWS Data Source Example                | Actual Example                           |
|-----------------|----------------------------------------|------------------------------------------|
| **Structured**  | SQL data stored in RDS then moved to S3| Customer information in relational tables|
| **Semi-Structured** | Data in DynamoDB or DocumentDB then moved to S3 | JSON logs of user activity           |
| **Unstructured**| Objects and files stored directly in S3| Images, videos, and PDF documents        |
| **Time-Series** | Time-stamped data stored in S3         | IoT device data, stock market data       |

### 생성형 AI 성능 지표 (Generative AI performance metrics)

**[한글]**

| 지표명                                                                | 설명                                                                              |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **ROUGE (Recall Oriented Understudy for Gisting Evaluation)**          | 생성 텍스트와 참조 텍스트 사이의 중복도를 측정하며, 요약 평가에 적합.                |
| **BLEU (Bilingual Evaluation Understudy)**                             | 출력과 참조 사이의 n-그램을 비교하여 번역의 정확도를 평가.                            |
| **GLUE (General Language Understanding Evaluation)**                   | 여러 자연어 이해 작업에 대한 모델 성능을 평가.                                       |
| **HELM (Holistic Evaluation of Language Models)**                      | 언어 모델 능력에 대해 광범위하고 작업 특화된 평가를 제공.                              |
| **MMLU (Massive Multitask Language Understanding)**                    | 다양한 도메인과 주제에 걸친 모델 지식을 테스트.                                     |
| **BIG-bench (Beyond the Imitation Game Benchmark)**                    | 표준 벤치마크로는 커버되지 않는, 창의적이고 어려운 AI 작업에 대해 모델을 평가.        |
| **Perplexity (당혹도)**                                                | 모델이 다음 토큰이나 단어의 가능성을 얼마나 잘 예측하는지를 측정.                       |

**[English]**

| Metric Name                                         | Explanation                                                             |
|-----------------------------------------------------|-------------------------------------------------------------------------|
| **Recall Oriented Understudy for Gisting Evaluation (ROUGE)** | Measures overlap between generated and reference text, good for summaries. |
| **Bilingual Evaluation Understudy (BLEU)**           | Evaluates translation accuracy by comparing n-grams between outputs and references. |
| **General Language Understanding Evaluation (GLUE)** | Assesses model performance on multiple natural language understanding tasks. |
| **Holistic Evaluation of Language Models (HELM)**    | Provides broad, task-specific evaluation of language model capabilities.  |
| **Massive Multitask Language Understanding (MMLU)**  | Tests model knowledge across a variety of domains and topics.            |
| **Beyond the Imitation Game Benchmark (BIG-bench)**  | Evaluates models on creative and difficult AI tasks not covered by standard benchmarks. |
| **Perplexity**                                       | Measures how well a model predicts the likelihood of the next token or word. |

### 생성형 AI 모델 (Generative AI Models)

**[한글]**

| 생성형 AI 모델                                    | 예시                                    | 활용 사례 / 잘하는 것                                       |
|---------------------------------------------------|-----------------------------------------|------------------------------------------------------------|
| **GAN (Generative Adversarial Networks)**          | StyleGAN, CycleGAN, ProGAN              | 이미지 생성, 얼굴 합성, 영상 생성                             |
| **VAE (Variational Autoencoders)**                 | Kingma & Welling VAE, Beta-VAE          | 이미지 노이즈 제거, 이상 탐지, 이미지 압축                    |
| **Transformers (트랜스포머)**                      | GPT-4, BERT, T5                         | 텍스트 생성, 언어 번역, 콘텐츠 생성                           |
| **RNN (Recurrent Neural Networks)**                | LSTMs, GRUs                             | 순차 데이터, 시계열 예측, 언어 모델                            |
| **생성 작업용 강화학습(Reinforcement Learning)**   | AlphaGo, DQN, OpenAI Five               | 게임 AI, 자율 제어, 생성 작업 최적화                          |
| **확산(Diffusion)**                                | Stable Diffusion, DALL·E 2, Imagen      | 이미지 생성 및 텍스트-이미지 변환                             |
| **플로우 기반 모델(Flow-Based Models)**            | Glow, RealNVP                           | 고품질 이미지 생성, 밀도 추정                                 |

**[English]**

| Generative AI Model                            | Examples                               | Use Case/What It's Good For                              |
|------------------------------------------------|----------------------------------------|----------------------------------------------------------|
| **Generative Adversarial Networks (GANs)**     | StyleGAN, CycleGAN, ProGAN             | Image generation, face synthesis, video creation          |
| **Variational Autoencoders (VAEs)**            | Kingma & Welling VAE, Beta-VAE         | Image denoising, anomaly detection, image compression     |
| **Transformers**                               | GPT-4, BERT, T5                        | Text generation, language translation, content generation |
| **Recurrent Neural Networks (RNNs)**           | LSTMs, GRUs                            | Sequential data, time series forecasting, language models |
| **Reinforcement Learning for Generative Tasks** | AlphaGo, DQN, OpenAI Five              | Game AI, autonomous control, optimizing generative tasks  |
| **Diffusion**                                  | Stable Diffusion, DALL·E 2, Imagen     | Image and text-to-image generation                        |
| **Flow-Based Models**                          | Glow, RealNVP                          | High-quality image generation, density estimation         |

### 학습 시트 (Study Sheets)

**[한글 정리]**

| **용어/개념**                                     | **설명**                                                                                                                                     |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Top-P**                                         | 0에서 1 사이 값 — 누적 확률로, 무작위성과 정확성의 균형을 맞춤. 1에 가까울수록 무작위성이 가장 낮음.                                            |
| **Temperature (온도)**                            | 무작위성을 제어함 — 값이 클수록 다양하고 창의적인 출력, 낮을수록 결정론적 결과.                                                                 |
| **Epochs**                                        | 모델 학습 시 반복 횟수 — 일반적으로 많을수록 좋으나, 너무 많으면 오버피팅으로 이어질 수 있음.                                                    |
| **AWS Rekognition**                               | 컴퓨터 비전/이미지 인식 — 객체 감지, 얼굴 분석, 콘텐츠 검열에 사용.                                                                              |
| **AWS Textract**                                  | **OCR** 서비스 — 스캔 이미지를 텍스트로 변환하고, 문서에서 정형 데이터 추출.                                                                    |
| **Amazon Comprehend**                             | 텍스트에서 핵심 문구, 엔터티, 감정, PII 데이터를 추출.                                                                                          |
| **AWS Intelligent Document Processing (IDP)**     | Textract, Comprehend, A2I를 활용하여 비정형 문서(예: PDF, 청구서) 처리를 자동화.                                                                |
| **Amazon Lex**                                    | 자연스러운 대화 텍스트 또는 음성 인터페이스로 **챗봇을 구축**하는 서비스.                                                                       |
| **Amazon Transcribe**                             | 오디오 자막 생성을 포함한 **음성-텍스트 변환(Speech-to-text)** 서비스.                                                                          |
| **Amazon Polly**                                  | 작성된 텍스트를 음성으로 변환하는 **텍스트-음성 변환(Text-to-speech)** 서비스.                                                                  |
| **Amazon Kendra**                                 | 시맨틱 이해 기능을 갖춘 지능형 문서 검색 엔진.                                                                                                  |
| **Amazon Personalize**                            | **개인화된 상품 추천** 서비스.                                                                                                                |
| **Amazon Translate**                              | **언어 번역** 서비스.                                                                                                                        |
| **Amazon Forecast**                               | 시계열 **예측(forecasting)** 제공. 예: 재고 수준 예측.                                                                                        |
| **Amazon Fraud Detection**                        | 온라인 거래와 계정 탈취를 포함한 사기 활동을 감지.                                                                                             |
| **Amazon Q Business**                             | 엔터프라이즈 데이터 처리와 작업을 위한 생성형 AI 기반 어시스턴트.                                                                                |
| **Amazon Macie**                                  | 데이터 보안을 위한 **PII 데이터** 감지 및 익명화 서비스.                                                                                       |
| **SageMaker Clarify**                             | 머신러닝 모델을 위한 **편향 감지(Bias detection)**와 설명 가능성.                                                                              |
| **SageMaker Ground Truth**                        | **모델 학습**용 데이터셋에 대한 **사람에 의한 라벨링(human labeling)** 제공.                                                                    |
| **Amazon Augmented AI (A2I)**                     | **추론(inference)** 시 신뢰도가 낮은 예측에 대한 **사람의 검토(Human review)**.                                                                |
| **AWS Data Exchange**                             | **서드파티 데이터셋**에 안전하게 접근.                                                                                                        |
| **AWS Glue Transformations**                      | 중복 제거, 결측치 채우기 같은 ETL 변환.                                                                                                        |
| **Amazon SageMaker JumpStart**                    | 사전 학습된 모델과 원클릭 배포가 있는 허브.                                                                                                    |
| **Amazon SageMaker Canvas**                       | 머신러닝 모델을 구축·학습하는 노코드 도구.                                                                                                     |
| **Fine-Tuning (파인튜닝)**                        | **라벨링된 데이터**를 사용해 **모델 가중치를 조정**하여 작업 성능을 개선.                                                                        |
| **Domain adaptation fine-tuning**                 | 소규모 데이터셋을 사용해 법률, 의료 같은 **특정 도메인**에 맞게 모델을 조정.                                                                    |
| **Instruction-based fine-tuning**                 | 예: 분류 등 **특정 작업에서 성능을 개선**하기 위한 파인튜닝.                                                                                    |
| **Continued-Pretraining**                        | **라벨링되지 않은 데이터**를 사용해 **모델의 지식 기반을 확장**.                                                                                |
| **Automatic Model Tuning (AMT)**                  | 모델 성능 개선을 위해 하이퍼파라미터를 자동으로 튜닝.                                                                                           |
| **Data-Drift (데이터 드리프트)**                  | 입력 데이터가 변하지만, 입력과 출력의 관계는 유지됨 (예: 새로운 인구 통계).                                                                     |
| **Concept-Drift (개념 드리프트)**                 | 입력과 출력의 관계가 변하여, 모델이 학습한 패턴이 더 이상 유효하지 않음 (예: 새로운 사기 패턴).                                                  |
| **AWS Trusted Advisor**                           | 비용, 성능, 보안 개선을 위한 권장 사항 제공.                                                                                                    |
| **Amazon Inspector**                              | 애플리케이션 워크로드에 대한 자동 보안 평가.                                                                                                    |
| **AWS PrivateLink**                               | VPC와 AWS 서비스 사이의 안전한 프라이빗 연결.                                                                                                  |
| **AWS Config**                                    | 컴플라이언스를 위해 AWS 구성 변경 사항을 모니터링·기록.                                                                                        |
| **AWS CloudTrail**                                | 감사(auditing)를 위해 AWS API 호출을 로깅·추적.                                                                                              |
| **BedRock GuardRails**                            | 부적절한 파운데이션 모델 출력을 방지하고 위험한 콘텐츠를 제한.                                                                                  |
| **Postgres (Aurora or RDS)**                      | 유사도 검색을 위한 벡터 데이터베이스 지원을 갖춘 SQL 데이터베이스.                                                                              |
| **Amazon DocumentDB**                             | MongoDB 호환 JSON 저장소로, 벡터 데이터베이스 지원.                                                                                            |
| **Amazon Neptune**                                | 벡터 검색 기능을 갖춘 그래프 데이터베이스.                                                                                                    |
| **Amazon Neptune ML**                             | 그래프 신경망(GNN)을 사용해 그래프 데이터로부터 결과를 예측.                                                                                    |
| **Amazon MemoryDB**                               | 빠른 벡터 검색 기능을 갖춘 인메모리 데이터베이스.                                                                                              |
| **Amazon OpenSearch Service**                     | 유사도 검색을 위한 벡터 데이터베이스 지원을 갖춘 검색 서비스.                                                                                    |
| **MSE (Mean Squared Error, 평균 제곱 오차)**      | 예측값과 실제값 사이 차이의 제곱을 평균 낸 값. MSE가 낮을수록 모델 성능이 좋음.                                                                  |
| **RMSE (Root Mean Squared Error, 평균 제곱근 오차)** | MSE의 제곱근으로, 해석이 더 쉬움. RMSE가 낮을수록 좋음.                                                                                       |

**[English]**

| **Term/Concept**                    | **Description**                                                                                                                                                      |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Top-P**                           | 0 to 1 value — cumulative probability, balances randomness and accuracy, 1 is least random.                                                                          |
| **Temperature**                     | Controls randomness—higher values lead to diverse, creative outputs; lower values make results more deterministic.                                                    |
| **Epochs**                          | Number of iterations on training a model—more is generally better, but too many can lead to overfitting.                                                             |
| **AWS Rekognition**                 | Computer vision/image recognition, used for object detection, facial analysis, and content moderation.                                                               |
| **AWS Textract**                    | **OCR** service — converts scanned images into text, structured data extraction from documents.                                                                           |
| **Amazon Comprehend**               | Extracts key phrases, entities, sentiment, and PII data from text.                                                                                                   |
| **AWS Intelligent Document Processing (IDP)** | Automates the processing of unstructured documents (e.g., PDFs, invoices) using Textract, Comprehend, and A2I.                                                  |
| **Amazon Lex**                      | Service for **building chatbots** with natural conversational text or voice interfaces.                                                                                  |
| **Amazon Transcribe**               | **Speech-to-text** service, including audio captioning.                                                                                                                  |
| **Amazon Polly**                    | **Text-to-speech** service for converting written text into spoken words.                                                                                                |
| **Amazon Kendra**                   | Intelligent document search engine with semantic understanding.                                                                                                      |
| **Amazon Personalize**              | Service for **personalized product recommendations**.                                                                                                                    |
| **Amazon Translate**                | **Language translation** service.                                                                                                                                       |
| **Amazon Forecast**                 | Provides time-series **forecasting**, e.g., inventory levels prediction.                                                                                                |
| **Amazon Fraud Detection**          | Detects fraudulent activity, including online transactions and account takeovers.                                                                                    |
| **Amazon Q Business**               | Generative AI-powered assistant for enterprise data processing and tasks.                                                                                            |
| **Amazon Macie**                    | **PII data** detection and anonymization service for data security.                                                                                                      |
| **SageMaker Clarify**               | **Bias detection** and explainability for machine learning models.                                                                                                       |
| **SageMaker Ground Truth**          | Provides **human labeling** for **model training** datasets.                                                                                                                 |
| **Amazon Augmented AI (A2I)**       | **Human review** for low-confidence predictions during **inference**.                                                                                                        |
| **AWS Data Exchange**               | Access **third-party datasets** securely.                                                                                                                                |
| **AWS Glue Transformations**        | ETL transformations like removing duplicates and filling missing values.                                                                                             |
| **Amazon SageMaker JumpStart**      | Hub with pre-trained models and one-click deployments.                                                                                                               |
| **Amazon SageMaker Canvas**         | No-code tool for building and training machine learning models.                                                                                                      |
| **Fine-Tuning**                     | **Adjusting model weights** using **labeled data** to improve task performance.                                                                                              |
| **Domain adaptation fine-tuning**   | Tailor a model for a **specific domain** like legal or medical using small datasets.                                                                                      |
| **Instruction-based fine-tuning**   | Fine-tuning a model to **perform better on specific tasks**, e.g., classification.                                                                                       |
| **Continued-Pretraining**           | Using **unlabelled data** to **expand a model's knowledge base**.                                                                                                            |
| **Automatic Model Tuning (AMT)**    | Automatically tunes hyperparameters to improve model performance.                                                                                                    |
| **Data-Drift**                      | Input data changes, but the relationship between inputs and outputs stays the same (e.g., new demographic).                                                          |
| **Concept-Drift**                   | The relationship between inputs and outputs changes, meaning the model's learned patterns no longer apply (e.g., new fraud patterns).                                |
| **AWS Trusted Advisor**             | Provides recommendations for cost, performance, and security improvements.                                                                                           |
| **Amazon Inspector**                | Automated security assessments for application workloads.                                                                                                            |
| **AWS PrivateLink**                 | Secure private connections between VPCs and AWS services.                                                                                                            |
| **AWS Config**                      | Monitors and records AWS configuration changes for compliance.                                                                                                       |
| **AWS CloudTrail**                  | Logs and tracks AWS API calls for auditing.                                                                                                                          |
| **BedRock GuardRails**              | Prevents inappropriate foundation model outputs and restricts risky content.                                                                                         |
| **Postgres (Aurora or RDS)**        | SQL database with vector database support for similarity search.                                                                                                     |
| **Amazon DocumentDB**               | JSON store, MongoDB-compatible with vector database support.                                                                                                         |
| **Amazon Neptune**                  | Graph database with vector search capabilities.                                                                                                                      |
| **Amazon Neptune ML**               | Uses Graph Neural Networks (GNNs) to predict outcomes from graph data.                                                                                               |
| **Amazon MemoryDB**                 | In-memory database with fast vector search capabilities.                                                                                                             |
| **Amazon OpenSearch Service**       | Search service with vector database support for similarity search.                                                                                                   |
| **MSE (Mean Squared Error)**        | Average squared difference between predicted and actual values, lower MSE indicates better model performance.                                                        |
| **RMSE (Root Mean Squared Error)**  | Square root of MSE, more interpretable; lower RMSE is better.                                                                                                        |
