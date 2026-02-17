# AWS Certified AI Practitioner (AIF-C01)  
### Exam Study Notes & Prep Guidance

These are my personal study notes for the **AWS Certified AI Practitioner (AIF-C01)** exam.

This is a **foundational-level certification**, comparable in difficulty to **AWS Certified Cloud Practitioner (CLF-C02)** — but focused specifically on **AI, ML, and Generative AI on AWS**.

The exam is **high-level and conceptual**, covering:

- Core AI and GenAI terminology  
- Responsible AI basics  
- AWS AI/ML services at a conceptual level  
- Simple use-case matching  

## Study Time

If you already have basic AWS familiarity, this is realistically **one focused weekend of study**.

## Preparation

The following is sufficient to pass:

- The free **AWS Skill Builder course** (~15 hours — easily completed faster at 1.25x–1.5x speed)
- The free official **AWS practice questions** (which felt slightly harder than the real exam)

No deep technical experience or advanced architecture knowledge is required.

## Useful Links
- [Official Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Exam-Guide.pdf)
- [Official Exam Prep - Amazon Skill Builder](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/19554/exam-prep-standard-course-aws-certified-ai-practitioner-aif-c01) - recommend watching in 1.5x
- [Official Exam Practice Questions](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/19790/exam-prep-official-practice-question-set-aws-certified-ai-practitioner-aif-c01-english) - About the level of real exam .   

## Overview

### General AI
- **Definition**: Refers to a broader concept of artificial intelligence, aiming to build systems that can perform any intellectual task that a human can. It’s often used to describe long-term goals of creating highly autonomous, flexible AI systems.
- **Key Concept**: AI with a broad ability to perform multiple tasks across domains, unlike specialized AI systems.
- **Examples**: **Expert Systems**, **Rules Engines** (e.g., MYCIN), which use predefined logic and rules to make decisions.

### Machine Learning (ML)
- **Definition**: A subset of AI that enables systems to learn from data and make predictions or decisions without explicit programming or rules.
- **Key Concept**: AI that operates through data patterns and training, rather than explicitly coded instructions.
- **Examples**: **Linear Regression**, **Decision Trees**, **Support Vector Machines**—supervised learning algorithms used for predictive tasks.

### Deep Learning
- **Definition**: A subset of machine learning that uses neural networks with multiple layers (hence "deep") to model complex patterns in data.
- **Key Concept**: Effective for tasks like image recognition, natural language processing, and autonomous systems.
- **Examples**: **Convolutional Neural Networks (CNNs)** for image processing, **Recurrent Neural Networks (RNNs)** for sequential data like time-series or language models.

### Generative AI
- **Definition**: A subset of deep learning focused on creating new content (such as text, images, or music) from learned data. Generative AI models are generally based on **foundation models**, which are large, pre-trained models that can be adapted to a wide range of tasks.
- **Key Concept**: AI systems that generate novel outputs based on patterns learned during training. Foundation models provide the versatility needed for fine-tuning on specific tasks.
- **Examples**: **ChatGPT** for text generation, **DALL·E** for image generation, **DeepDream** for artistic visual generation.

### Large Language Models (LLMs)
- **Definition**: A type of **Generative AI** focused on understanding and generating human-like text. LLMs are trained on vast amounts of text data to learn language patterns, grammar, and context.
- **Key Concept**: LLMs generate coherent and high-quality text based on input prompts and are capable of performing tasks like summarization, translation, and question answering.
- **Examples**: **GPT-4**, **BERT**, **T5**, **Claude 2**—used for tasks like text generation, sentiment analysis, summarization, and natural language understanding.

---

## Concepts

### In-Context Learning
- **Definition**: A method of enhancing generative AI models by adding additional data and examples to the prompt, helping the model solve tasks more effectively.

### Prompt Types
- **Few-Shot Prompt**: Providing a few examples in the prompt to guide the model’s behavior.
- **Zero-Shot Prompt**: Providing no examples in the prompt, asking the model to perform the task without guidance.
- **One-Shot Prompt**: Providing exactly one example to guide the model’s behavior.
- **Prompt Template**: A pre-defined format or structure for prompts to standardize and improve the interaction with AI models.
- **Chain-of-Thought Prompting**: A method where the prompt encourages the model to break down reasoning into steps.
- **Prompt Tuning**: The process of adjusting prompts to improve model performance for specific tasks.

### Latent Space
- **Definition**: The encoded knowledge or patterns captured by large language models (LLMs) that store relationships between data.
- **Usage**: It represents the internal understanding of language or data that AI models use to generate outputs.

### Embeddings
- **Definition**: Numerical, vectorized representations of tokens (words, phrases, etc.) that capture their semantic meaning.
- **Use Case**: Used for tasks like semantic search, where the meaning of a word or token is important.
- **Storage**: Can be stored in a vector database for efficient search and retrieval.

### Tokens
- **Definition**: The basic units of text (e.g., words, subwords, or characters) that are processed by language models. In the context of LLMs, tokens are used to represent both inputs (text provided) and outputs (text generated).

### Context-Window
- **Definition**: The maximum amount of tokens an LLM model can process at once, including both the input prompt and the output generated by the model. If the number of tokens exceeds the model’s context-window, earlier parts of the text may be truncated.
- **Usage**: The context-window is a key factor in determining how much information can be fed into the model at one time and affects tasks like long-form text generation, document analysis, or multi-turn conversations.

### Hallucinations
- **Definition**: Hallucinations occur when a language model generates incorrect or nonsensical information that may sound plausible but is not grounded in factual data or the provided input.
- **Mitigations**: 
  - Retrieval Augmented Generation (RAG): Mitigates hallucinations by retrieving relevant external data during the generation process, ensuring the model generates responses based on accurate information.
  - Fine-Tuning: Training the model on more relevant, accurate data can help reduce hallucinations by aligning the model’s output with factual knowledge.
  - Human-in-the-Loop (HITL): Incorporating human review in low-confidence areas can prevent hallucinated outputs from being used in critical applications.

### Multi-Modal Models
- **Definition**: Models that work across multiple data types, embedding text, images, or even audio into a shared space. These models are commonly used for multimodal generation tasks, such as creating captions for images or generating visuals from textual descriptions, by leveraging different types of input to produce richer, more context-aware outputs.
  
---

### Search Methods
- **Keyword Search**: Matches exact terms in the search query.
- **Semantic Search**: Uses embeddings to understand the meaning behind the search query, allowing for more accurate and meaningful results.

---

### Vector Databases
- **Definition**: A type of database designed for storing and querying vectors (embeddings), which is useful for tasks like semantic search.

#### Vector Database Options on AWS
- **Amazon OpenSearch Service**: Supports k-nearest neighbor (k-NN) search for vector databases. Useful for log analytics, real-time application monitoring, and search.
- **Amazon Aurora PostgreSQL-Compatible Edition & Amazon RDS for PostgreSQL**: Supports the __pgvector__ extension, enabling efficient storage of embeddings and similarity searches.
- **Amazon Neptune ML**: Uses Graph Neural Networks (GNNs) to make predictions based on graph data, supporting vectorized data in graph databases.
- **Amazon MemoryDB**: Supports high-speed vector storage and retrieval with millisecond query times and tens of thousands of queries per second (QPS).
- **Amazon DocumentDB**: Supports vector search with MongoDB compatibility, enabling storage, indexing, and search of millions of vectors with millisecond response times.

--- 

## The Machine Learning (ML) Pipeline

The ML Pipeline is a systematic process used to build, train, and deploy machine learning models. It ensures that each stage, from identifying business goals to monitoring deployed models, is properly managed and optimized for performance. The typical steps in the pipeline are as follows:

**Steps:**
1. Identify Business Goal
2. Frame ML Problem
3. Collect Data
4. Pre-Process Data
5. Engineer Features
6. Train, Tune, Evaluate
7. Deploy
8. Monitor

---

### 1. Identify Business Goal
- **Description**: Define success criteria and align stakeholders to ensure the ML project meets business objectives.
- **Key Activities**:
  - Establish clear success metrics.
  - Align with stakeholders across the organization.

### 2. Frame the ML Problem
- **Description**: Define the ML problem, inputs, outputs, and metrics while considering feasibility and cost/benefit analysis.
- **Key Activities**:
  - Identify inputs, outputs, requirements, and performance metrics.
  - Perform cost-benefit analysis to evaluate feasibility.
  
- **Model Options**:
  - **AI/ML Hosted Service** (e.g., AWS Comprehend, Forecast, Personalize): No training required.
  - **Pre-trained Models** (e.g., Amazon Bedrock, SageMaker JumpStart): Fine-tune with your data.
  - **Fully Custom Model**: Build and train from scratch.

### 3. Collect Data

- **Description**: Collect and prepare the necessary data for training the model.

- **Key Activities**:
  - Identify data sources (e.g., databases, data lakes, external APIs).
  - Ingest and label data.

- **Where Data is Stored**:  
  - Data collected for machine learning is typically stored in **Amazon S3**. This applies to both data sourced from internal systems and third-party datasets accessed via **AWS Data Exchange**.

- **Tools**:
  - **AWS Glue**: For **ETL (Extract, Transform, Load)** processes, moving and transforming data into a usable format before storage in **Amazon S3**.
  - **SageMaker Ground Truth**: For human labeling of ambiguous data, with labeled data stored in **Amazon S3**.
  - **AWS Data Exchange**: Allows secure access to third-party datasets. These datasets can be used as additional sources of training data, and the ingested data is stored in **Amazon S3**.
  - **Amazon S3**: Primary storage service where collected data is securely stored before being processed or used for training.

### 4. Pre-Process Data

- **Description**: Clean and prepare the data, ensuring it is suitable for training.

- **Key Activities**:
  - Perform **Exploratory Data Analysis (EDA)**.
  - Clean the data, removing duplicates, filling missing values, and anonymizing **PII**.
  - Split data is often split into ratios of **training (80%)**, **validation (10%)**, and **test (10%)** sets.

- **How to Clean Data**:
  - **AWS Glue Transformations**: Glue has built-in transformations for tasks like removing duplicates or filling missing values, and allows custom transformations using Python or Spark.
  - **Macie for PII**: AWS Macie detects and anonymizes **PII** data, working with **Amazon S3** to scan and mask sensitive information.
  - **AWS Glue DataBrew**: Enables data preparation and cleaning through a visual interface. You can apply **data quality rules**, such as filling missing values, and save these transformations as **recipes** for reuse.
  - **SageMaker Canvas**: Facilitates data import, transformation, and visualization without requiring deep technical knowledge. It uses built-in transformations that are added step-by-step to prepare data for training, and each step can be visually tracked in the flow.

- **Tools**:
  - **AWS Glue**: An ETL service with built-in transformations for data cleaning.
  - **AWS Glue DataBrew**: A visual data preparation tool where you can define and apply transformation rules (called **recipes**), with built-in data quality checks.
  - **SageMaker Canvas**: A tool for importing, preparing, and transforming data with a visual, no-code interface. Each transformation step is part of a clear workflow, making data preparation more accessible.

### 5. Engineer Features
- **Description**: Select and engineer features that will enhance model performance.
- **Key Activities**:
  - Feature Selection: Identifying the most relevant features from your dataset based on domain knowledge, reducing dimensionality and improving model efficiency.
  - Feature Creation: Transforming raw data into new features (e.g., scaling, encoding categorical variables, and deriving new metrics from existing ones).
  - Feature Transformation: Applying mathematical or statistical transformations (e.g., normalization, standardization) to improve model convergence and performance.
- Automated Feature Engineering: Consider using SageMaker Autopilot, which can automatically generate and rank features that could improve model performance.
- Dimensionality Reduction: Techniques like Principal Component Analysis (PCA) can be applied to reduce the number of features while retaining the most important information.
- Feature Scaling: Tools like AWS Glue or SageMaker DataBrew can be used to apply scaling techniques (e.g., normalization or standardization), ensuring that features contribute equally to model training.
- Categorical Encoding: Convert categorical variables into numerical values using techniques like one-hot encoding or target encoding using SageMaker Data Wrangler or AWS Glue.
  
- **Tools**:
  - **SageMaker Feature Store**: Store and manage features as a single source of truth.

### 6. Train, Tune, and Evaluate the Model
- **Description**: Train the model, tune it, and evaluate performance.
- **Key Activities**:
  - Train the model iteratively and fine-tune parameters.
  - Tune hyperparameters (e.g., epoch, batch size, learning rate) and run experiments.
  - Evaluate the model using metrics and compare performance.

- **Parameters**:
  - **Inference Parameters** (supported by Amazon Bedrock):
    - **Randomness and Diversity**:
      - Temperature:
        - Controls randomness—higher values lead to more diverse, creative outputs; lower values produce more predictable, deterministic results.
      - Top K:
        - Limits the model to selecting from the top K most probable tokens; smaller K values result in safer, more predictable choices.
        - Top K is not a terribly useful parameter - use Temperature or Top-P instead. 
      - Top P:
        - Uses cumulative probability to choose tokens, focusing on the smallest set of tokens with a combined probability of P, balancing randomness and diversity.
        - Higher Top P values (closer to 1) reduce randomness by restricting the token pool to only the most probable choices. 
      - Top-K vs Top-P: Top K fixes the number of tokens considered, while Top P uses a variable number of tokens based on their combined probability, making Top P more adaptive and flexible in balancing randomness.
      - Temperature vs. Top P: Temperature adjusts the overall randomness by scaling probabilities, allowing more or less randomness across all possible tokens. Top P narrows the token choices to those that collectively add up to a certain probability threshold, balancing randomness with accuracy.
      - Use Cases:
        - Use Top-P when you want adaptive diversity but want to stay closer to more likely outcomes.
        - Use Temperature when you need consistent randomness control across the board.  
    - Response length:
      - Specifies the maximum length of generated output, affecting how verbose or concise the response is.
    - Penalties:
      - Applies penalties to repeated tokens or sequences to encourage variety in the generated text.
    - Stop sequences:
      - Defines specific sequences where the model will stop generating text, ensuring controlled output length or format.
  - **Model Training Parameters** (Hyperparameters):
    - **Epoch**: The number of iterations through the entire dataset.
      - Increasing epochs generally improves the model's learning but can lead to overfitting if too high. More epochs help the model learn better but might also result in diminishing returns after a certain point.
    - **Batch Size**: Number of samples before updating model parameters.
      - Smaller batch sizes provide more frequent updates, which can help in converging quickly but can introduce more noise. Larger batch sizes are more stable but may require more computation and memory.
    - **Learning Rate**: Controls how fast the model learns.
      - A high learning rate speeds up training but may skip optimal solutions, while a low learning rate leads to slower but more precise convergence, though it risks getting stuck in local minima.
        
- **Error Metrics**:

  - **MSE (Mean Squared Error)**: During model evaluation, MSE calculates the average squared difference between predicted values and actual values, giving more weight to larger errors. A lower MSE indicates better performance, making it useful for comparing different models or tuning hyperparameters.
    - **Use Case**: Useful in regression problems like predicting house prices or stock values.
    - **Rule of Thumb**: Lower is better, as it means the model’s predictions are closer to the actual values.
    
  - **RMSE (Root Mean Squared Error)**: RMSE is the square root of MSE and gives an error measure in the same unit as the predicted values, making it more interpretable. RMSE is used to see how much error is expected per prediction.
    - **Use Case**: Often used alongside MSE in regression problems for easier interpretability.
    - **Rule of Thumb**: Lower RMSE means better model performance.
  
  - **Perplexity**: Perplexity measures how well a model predicts a sequence of tokens (e.g., words). Lower perplexity indicates better performance, as it means the model is better at predicting the next word in a sequence.
    - **Use Case**: Commonly used for language models, such as evaluating how well a model predicts the next word in a sentence.
    - **Rule of Thumb**: Lower perplexity means better predictive performance.
  
  - **Precision**: Precision is the ratio of true positives to the total number of positive predictions (true positives + false positives). It is used when minimizing false positives is important.
    - **Use Case**: Often used in classification tasks like spam detection, where avoiding false positives is critical.
    - **Rule of Thumb**: Higher precision is better when the cost of false positives is high.
  
  - **Recall (TPR)**: Recall (True Positive Rate) is the ratio of true positives to the total actual positives (true positives + false negatives). It is used when minimizing false negatives is crucial.
    - **Use Case**: Commonly used in medical testing (e.g., disease screenings) to avoid missing positive cases.
    - **Rule of Thumb**: Higher recall is better when missing positive cases is costly.
  
  - **False Positive Rate (FPR)**: FPR is the ratio of false positives to the total number of negatives (false positives + true negatives). It is used to measure how often incorrect positive predictions are made.
    - **Use Case**: Often used in security applications, like fraud detection or alarms, where false positives should be minimized.
    - **Rule of Thumb**: Lower FPR is better, as it means fewer false alarms.
  
  - **Specificity (TNR)**: Specificity (True Negative Rate) is the ratio of true negatives to the total actual negatives (true negatives + false positives). It measures how well the model identifies negative instances.
    - **Use Case**: Used in medical testing to correctly identify non-diseased patients.
    - **Rule of Thumb**: Higher specificity is better when identifying true negatives is important.
  
  - **Accuracy**: Accuracy is the ratio of correct predictions (both true positives and true negatives) to the total number of predictions. It is used when both positive and negative predictions are equally important.
    - **Use Case**: Typically used in balanced classification tasks like image classification.
    - **Rule of Thumb**: Higher accuracy is better for overall correctness.
  
  - **F1 Score**: The F1 Score is the harmonic mean of precision and recall, used when there is a need for a balance between precision and recall.
    - **Use Case**: Used in document classification or tasks where both false positives and false negatives matter.
    - **Rule of Thumb**: Higher F1 score means better balance between precision and recall.
  
  - **ROC Curve**: The ROC (Receiver Operating Characteristic) curve plots the true positive rate (recall) against the false positive rate at various threshold levels. It is used to evaluate the trade-off between sensitivity and specificity.
    - **Use Case**: Commonly used in binary classification problems to visualize the model’s performance across different thresholds.
    - **Rule of Thumb**: A higher area under the ROC curve (AUC) indicates better model performance.
  
- **Model Training Issues**:
  - **Overfitting**: Too much training on the same data, causing the model to be overly specific.
    - Solution: Use more diverse data during training.
  - **Underfitting**: The model doesn’t learn enough patterns from the data.
    - Solution: Train the model for more epochs or with more data.
  - **Bias and Fairness**: Lack of diversity in training data leading to biased predictions.
    - Solution: Ensure diverse and representative training data; include fairness constraints.

- **Fine-Tuning** (BedRock and SageMaker):
  - Adjust the weights of a pre-trained model with your specific and _labelled_ data to adapt it for new tasks. 
  - Be aware that if you only provide instructions for a single task, the model may lose its more general purpose capability and experience _catastrophic forgetting_.
  - **Domain adaptation fine-tuning** (SageMaker): Tailors a pre-trained foundation model to a specific domain (e.g., legal, medical) using a small amount of domain-specific data. This helps the model perform better on tasks related to that particular domain.
  - **Instruction-based fine-tuning** (SageMaker): Involves providing labeled examples of specific tasks (e.g., summarization, classification) to improve a model’s performance on that particular task. This type of fine-tuning is useful for making the model better at tasks where precise outputs are needed.
 
- **Continued-Pretraining** (BedRock):
  - Using _unlabeled_ data to expand the model's overall knowledge without narrowing its scope to a specific task.
 
- **Transfer Learning**:
  - Fine-tuning an existing model that has learned general features and applying it to a new problem, speeding up training and improving accuracy.
     
- **Tools**:
  - **SageMaker Training Jobs**: Manage training processes, specify training data, hyperparameters, and compute resources.
  - **SageMaker Experiments**: Track model runs and hyperparameter tuning.
  - **Automatic Model Tuning (AMT)**: Automatically tune hyperparameters using the specified metric.

### 7. Deploy the Model
- **Description**: Deploy the trained model to make predictions.
    
- SageMaker Deployment Options:
  - **Real-Time Inference**: For low-latency, sustained traffic predictions with auto-scaling capabilities.
  - **Batch Transform**: For processing large batches of data asynchronously.
  - **Asynchronous Inference**: For long-running inference requests with large payloads, handled without immediate responses.
  - **Serverless Inference**: For intermittent traffic, where the model scales automatically without infrastructure management.
- Bedrock Deployment Mechanisms:
  - **On-Demand Inference**: Pay-per-use inference based on the number of input/output tokens. Ideal for low or sporadic usage.
  - **Provisioned Throughput**: Required for custom or fine-tuned models, providing guaranteed capacity for consistent, high-throughput inference.
  - **BedRock Agent**s: Deploy agents for multi-step workflows, integrating models with tools like Amazon Kendra and AWS Lambda to handle complex tasks.
  
- **Tools**:
  - **AWS API Gateway**: Expose model as an API endpoint for integration with applications.

- **Tools**:
  - **AWS API Gateway (Optional)**: Used to expose models as RESTful APIs, enabling seamless integration with other applications or microservices. It’s optional and typically used when you want external applications to interact with your model endpoint.
  - SageMaker Deployment: Models are deployed via Docker images stored in Amazon ECR and deployed to Lambda (for Serverless Inference), EC2, EKS (Elastic Kubernetes Service), or ECS (Elastic Container Service), depending on use cases.
  - Instance Types:
    - Inf1: Optimized for cost-effective, high-performance deep learning inference using AWS Inferentia chips.
    - P4: Powered by NVIDIA A100 GPUs, ideal for large-scale, high-performance inference with very low latency.
    - G5: Designed for GPU-based workloads, optimized for graphics and machine learning inference with NVIDIA GPUs.
    - Graviton2 (C6g, M6g): Energy-efficient, ARM-based instances for general-purpose machine learning inference tasks.
  - SageMaker Endpoints: After deployment, models are served via SageMaker Endpoints for real-time inference or batch transform jobs.
  - Bedrock Deployment:
    - AWS Lambda: Often integrated with Bedrock for Bedrock Agents to enable automation in multi-step workflows.
    - Amazon Kendra: When deploying Bedrock Agents, Amazon Kendra is often used for document search and knowledge-based tasks.
    - Provisioned Throughput Tools: Provisioning inference capacity for high-throughput applications via AWS Management Console or Bedrock API.

### 8. Monitor the Model
- **Description**: Continuously monitor the model's performance and detect any data or concept drift.
- **Key Activities**:
  - Monitor model in real-time for data and concept drift.
  - Set alerts and automate corrective actions if performance degrades.

- **Types of Drift**:
  - Data Drift: The input data changes, but the relationship between inputs and outputs remains the same (e.g., a different demographic).
  - Concept Drift: The relationship between inputs and outputs changes, meaning the model's learned patterns no longer apply (e.g., new patterns of fraud that the model wasn't trained on).

- **Tools**:
  - **SageMaker Model Monitor**: Schedule and monitor data drift, send results to CloudWatch, and automate corrective measures.

---

### MLOps and Automation
- **Description**: Apply DevOps principles to manage machine learning models throughout their lifecycle, focusing on automation, version control, and monitoring.
- **Key Activities**:
  - Automate deployment, monitoring, and retraining of models.
  - Ensure continuous integration and delivery (CI/CD) for model updates.
  - Implement version control to manage multiple model versions.
- **Tools**:
  - **SageMaker Pipelines**: Automate and manage the ML workflow end-to-end.
  - **AWS CodePipeline**: Automate the build, test, and deploy phases for models.
  - **SageMaker Model Registry**: Manage and track model versions and metadata.
  - **Amazon S3**: Used to store trained model artifacts after training for both SageMaker and Bedrock. Model outputs, including weights and artifacts, are exported to S3 for easy access during deployment and evaluation.

---

### Model Governance and Explainability
- **Description**: Ensure transparency, accountability, and regulatory compliance for ML models, while making their behavior interpretable to stakeholders.
- **Key Activities**:
  - Implement governance frameworks for tracking model usage and lineage.
  - Use tools to detect and mitigate bias, ensure fairness, and explain predictions.
  - Provide clear documentation of model history and performance for audits.
- **Tools**:
  - **SageMaker Clarify**: _Detect bias_, explain model predictions, and increase transparency.
  - **SageMaker Model Cards**: Create documentation for trained models, including performance metrics and intended use.
  - **ML Governance from SageMaker**: Provides tools for tighter control and visibility over ML models, helping track model information and monitor behavior like bias.
  - **SageMaker ML Lineage Tracking**: Capture the entire workflow, tracking model lineage for reproducibility and governance.
  - **Glue DataBrew**: Simplify data governance with visual data preparation and quality rules.
  - **AWS Audit Manager**: Automates the auditing of AWS services, ensuring continuous compliance and audit readiness for industry regulations.
  - **AWS Artifact**: Provides on-demand access to compliance reports and agreements, helping organizations meet compliance requirements.
  - **AWS AI Service Cards**: Enhance transparency by providing information on use cases, limitations, responsible AI practices, and performance best practices for AI services and models.
  
---

### Cost and Performance Optimization
- **Description**: Optimize resource usage and model performance without inflating costs.
- **Key Activities**:
  - Use managed spot training for lower-cost training jobs.
  - Select appropriate instance types for the job and leverage auto-scaling capabilities.
  - Use resource monitoring to detect inefficiencies in resource utilization.
- **Tools**:
  - **AWS Trusted Advisor**: Provides recommendations for cost and performance improvements.
  - **SageMaker Managed Spot Training**: Reduce training costs by utilizing spare AWS EC2 capacity.
  - **SageMaker Profiler**: Identify inefficient resource use during model training.
  - **Amazon Inspector**: Automates security assessments of ML applications, identifying vulnerabilities that can lead to performance degradation or security issues.

---

### Continual Learning and Retraining
- **Description**: Continuously retrain models to account for new data and changing conditions, preventing performance degradation.
- **Key Activities**:
  - Schedule regular model retraining based on new data.
  - Use tools to detect performance drops and initiate automatic retraining workflows.
  - Handle model drift by monitoring for concept and data drift.
- **Tools**:
  - **SageMaker Model Monitor**: Detect data drift and trigger retraining workflows.
  - **SageMaker Pipelines**: Automate retraining processes end-to-end.

---

### Security
- **Description**: Implement best security practices to safeguard machine learning models, data, and related infrastructure.
  
- **Key Activities**:
  - **Least Privilege Principle**: Ensure that IAM roles and policies grant only the permissions required for specific jobs or functions.
  - **PrivateLink and VPC Endpoints**: Lock down **SageMaker** to prevent exposure to the internet. Use **PrivateLink** and **VPC endpoints** to securely access resources within your private network.
  - **Encryption at Rest and in Transit**: By default, **SageMaker** encrypts data at rest and in transit using **KMS** (Key Management Service).
  - **IAM Roles and Policies**: Create and manage IAM roles and policies to ensure secure access to model data and resources.
  - **S3 Block Public Access**: Prevent model data from being exposed by ensuring **S3 Block Public Access** settings override any potential public access.
  - **AWS IAM Identity Center**: Centralize identity management, allowing access to multiple AWS accounts, and integrate with Active Directory for identity management.
  
- **Tools**:
  - **AWS Config**: Continuously monitors and records configuration changes across AWS resources to ensure compliance and security.
  - **AWS CloudTrail**: Logs API calls and tracks user activity for auditing and compliance.
  - **Amazon Inspector**: Automatically scans for vulnerabilities in machine learning environments to ensure that deployed models are secure.
  - **AWS Audit Manager**: Automates auditing and ensures compliance with industry regulations by generating audit reports for validation.
  - **AWS Artifact**: Provides access to compliance documents and security reports to ensure that your ML environments meet security and regulatory standards.
  - **SageMaker Role Manager**: Simplifies the management of permissions and roles for SageMaker resources and services.

---

## Services 

### AWS Managed AI Services

AWS offers a range of managed AI services designed to be easily integrated into applications, providing powerful AI capabilities without the need for deep machine learning expertise. Here's an overview of key services:

#### Computer Vision
- **AWS Rekognition**
  - Facial comparison and analysis, object and text detection, content moderation. Good for _screening content_ such as identifying violent or inappropriate material.

#### Text and Document Analysis
- **AWS Textract** (OCR)
  - Converts scanned images to text, enabling digital content management.
- **Amazon Comprehend** (NLP)
  - Extracts key phrases, entities, and sentiment from text. Useful for analyzing _sentiment of feedback_ and detecting _PII data_.
- **AWS Intelligent Document Processing** (IDP)
  - A group of AWS services that together automate the extraction, classification, and processing of data from various document types. It leverages AI technologies such as Optical Character Recognition (OCR), Natural Language Processing (NLP), and Machine Learning (ML) to handle unstructured data found in documents like PDFs, invoices, and legal contracts.

#### Language AI
- **Amazon Lex**
  - Builds conversational interfaces for both voice and text, ideal for creating _chatbots_.
- **Amazon Transcribe**
  - Speech to text service, perfect for creating _captions for audio_.
- **Amazon Polly**
  - Converts text into lifelike speech, enhancing user engagement through voice.

#### Customer Experience
- **Amazon Kendra**
  - Provides intelligent document search capabilities.
- **Amazon Personalize**
  - Offers personalized product recommendations, akin to "you may also like" features.
- **Amazon Translate**
  - Facilitates language translation, supporting global user interaction.

#### Business Metrics
- **Amazon Forecast**
  - Predicts future points in time-series data, such as _inventory levels_.
- **Amazon Fraud Detection**
  - Detects potential fraud in various scenarios including online transactions and new account creations.

#### Amazon Q

- **Amazon Q Business**
  - A generative AI-powered assistant that helps with tasks like answering questions, generating content, and automating workflows by accessing enterprise data sources like S3, SharePoint, and Salesforce.
- **Amazon Q Developer**
  - A tool for developers that includes features like code generation and security scanning to help automate tasks related to development and testing.
- **Amazon Q in QuickSight**
  - Integrated with Amazon QuickSight for natural language querying, allowing users to ask business intelligence-related questions and generate insights from their QuickSight data with AI.
- **Amazon Q in Connect**
  - Integrated with Amazon Connect, Amazon Q helps improve customer service by answering customer inquiries, automating responses, and managing tickets using natural language AI.
- **Amazon Q in AWS Supply Chain**
  - Integrated into AWS Supply Chain, Amazon Q assists in optimizing and automating supply chain management by generating insights from supply chain data, streamlining inventory management, and forecasting demand.

---

### Amazon SageMaker

Amazon SageMaker is an integrated machine learning service that enables developers and data scientists to build, train, and deploy machine learning models at scale. Users can create custom models from scratch or use and fine-tune existing ones through SageMaker JumpStart. This platform offers more control than high-level AI services like AWS Rekognition, allowing for detailed customization and optimization to meet specific project requirements.

#### SageMaker Studio

SageMaker Studio is an integrated development environment (IDE) for machine learning, providing a single interface for preparing data, building models, training, tuning, and deploying them. It offers features like Jupyter notebooks for code development, integrated debugging tools, and experiment management, all within a collaborative, cloud-based environment. Studio also supports real-time collaboration and easy access to various SageMaker capabilities, including model monitoring and data preparation.

####  Training Process

The typical SageMaker training process includes several key elements that help configure and manage the training jobs:

- **Training Data Locations**: Data is typically stored in Amazon S3 and accessed via S3 URLs.
- **ML Compute Instances**: SageMaker leverages EC2 instances (ECR instances) for scalable compute power.
- **Training Images**: The training process is run using Docker container images specifically designed for machine learning.
- **Hyperparameters**: Parameters that guide the learning process (e.g., learning rate, batch size).
- **S3 Output Bucket**: The trained model artifacts are stored in an S3 bucket for later use.

#### Features
- **SageMaker Feature Store**  
  - Central repository for storing, retrieving, and sharing machine learning features.
- **SageMaker Model Registry**  
  - Manages different versions of models and their metadata.
- **SageMaker Pipelines**  
  - Provides a workflow orchestration service for building, training, and deploying models with repeatable workflows.
- **SageMaker Model Monitor**  
  - Utilizes built-in rules to detect data drift or create custom rules, monitoring results can be sent to CloudWatch, and automates corrective measures.
- **SageMaker Ground Truth**  
  - Leverages actual humans for labeling data, ensuring high-quality training datasets.
- **SageMaker Canvas**  
  - A visual, no-code tool that allows users to build models based on their data with less technical expertise.
- **SageMaker JumpStart**  
  - Access to PreTrained Models and a hub for easily deploying machine learning solutions.
- **SageMaker Clarify**  
  - Tools to help detect biases and explain predictions to increase transparency.
- **SageMaker Role Manager**  
  - Manages permissions for SageMaker resources and services.
- **SageMaker Model Cards**  
  - Create transparent documentation for trained models.
- **SageMaker ML Lineage Tracking**  
  - Tracks the lineage of ML models to establish model governance, reproduce workflows, and maintain work history.
- **SageMaker Model Dashboard**  
  - Provides a unified interface to manage and monitor all model-related activities.
- **SageMaker Data Wrangler**  
  - Simplifies the process of data preparation for machine learning, enabling quick and easy data cleaning, transformation, and visualization.
- **SageMaker Experiments (Now called MLflow with Amazon SageMaker)**
  - Tracks, organizes, views, analyzes, and compares iterative ML experimentation.
- **SageMaker Autopilot**
  - Automatically builds, trains, and tunes machine learning models while giving you full visibility and control over the process.
- **Amazon Augmented AI (A2I)**
  - Allows you to add human review for low-confidence predictions or random samples, ensuring more accurate results.
- **SageMaker Managed Spot Training**
  - Reduces the cost of training models by using spare AWS EC2 capacity.
- **SageMaker Profiler**
  - Identifies resource inefficiencies in training jobs to minimize cost without sacrificing speed or accuracy.

---

### Amazon Bedrock

Amazon Bedrock is a fully managed, serverless service that provides access to high-performing foundation models (FMs) from leading AI companies through a single API. It is designed to facilitate the creation of generative AI applications, prioritizing security, privacy, and responsible AI.

#### Pricing
- **Pay-as-you-go**: Amazon Bedrock charges based on the number of **input and output tokens** used during inference. This means you only pay for the tokens processed when using the foundation models.
- **Fine-tuned models**: If you are using a **custom or fine-tuned model**, additional charges apply for **Provisioned Throughput**, which guarantees consistent performance and reserved capacity for inference.

#### Features
- **Model Choice**  
  - Access a variety of foundation models from AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon, allowing for optimal model selection based on specific application needs.
  - Amazon Titan Models
    - Exclusive to Amazon Bedrock, Amazon Titan models are pretrained, high-performing foundation models created by AWS, designed for a wide range of use cases with responsible AI practices.
- **Customization**  
  - Customize foundation models privately with your data using techniques such as fine-tuning and Retrieval Augmented Generation (RAG), enhancing the model's relevance and accuracy.
- **Foundation Model Evaluation**
  - Model Evaluation on Amazon Bedrock allows you to evaluate, compare, and select the best foundation models for your specific use case. You can assess models based on custom metrics such as accuracy, robustness, and toxicity, ensuring they meet your performance requirements. Integration with Amazon SageMaker Clarify and fmeval further supports model evaluation by checking for bias and explainability.
- **Bedrock Knowledge Bases**
  - Uses Retrieval Augmented Generation (RAG) to fetch data from private sources, delivering more relevant and accurate responses with full support for the RAG workflow—handling data ingestion, retrieval, and prompt augmentation.
  - Enhances outputs by integrating retrieval processes that pull relevant external knowledge into the generative model.
- **Bedrock Agents**  
  - Create agents capable of planning and executing multistep tasks using company systems and data sources—streamlining complex tasks such as customer inquiries and order processing.
- **Serverless**  
  - Eliminates the need for infrastructure management, simplifying the deployment and scaling of AI capabilities.
- **Security and Privacy Guardrails**  
  - Features robust controls to restrict AI outputs, preventing the generation of inappropriate content and restricting sensitive advice like financial recommendations, ensuring ethical and compliant AI usage.
- **PartyRock**
  - A hands-on AI app-building playground powered by Amazon Bedrock, where users can quickly build generative AI apps and experiment with models without writing code.

---

### AWS Glue 

AWS Glue is a fully managed, cloud-optimized ETL (Extract, Transform, Load) service that helps prepare and load data for analytics and AI models.

#### Features

- **AWS Glue ETL Service**
  - Cloud-based ETL service for data preparation with built-in transformations like dropping duplicates and filling missing values.
  - Example Workflow: AWS Kinesis Data Streams -> AWS Glue ETL Job -> CSV to Parquet -> S3 Data Lake.
- **AWS Glue Data Catalog**
  - Centralized repository for managing and monitoring ETL jobs, storing metadata (schemas, not data) with built-in classifiers.
- **AWS Glue Databrew**
  - Visual tool for data preparation, defining data quality rules, and saving transformations as "recipes."
- **AWS Glue Data Quality**
  - Detects anomalies and recommends data quality rules for ensuring clean, high-quality data for AI models.
---

## Tables

### Traditional ML vs Deep Learning

| Category          | Traditional ML                                      | Deep Learning                                 |
|-------------------|-----------------------------------------------------|-----------------------------------------------|
| **Task Complexity** | Well-defined tasks                                  | Complex tasks                                 |
| **Data Type**      | Structured / Labeled Data                           | Unstructured Data (Images, Video, Text)       |
| **Methodology**    | Solves problems through statistics and mathematics  | Utilizes neural networks                      |
| **Feature Handling** | Manually select and extract features                | Features are learned automatically by the model |
| **Cost**           | Less costly                                         | Higher costs due to computational demands     |


### Types of Machine Learning

| Learning Type         | Description                                          | Challenges                            | AWS Tools              | Common Use Cases                   |
|-----------------------|------------------------------------------------------|---------------------------------------|------------------------|------------------------------------|
| **Supervised Learning** | Uses pre-labeled data to train models.               | Labelling the data can be challenging. | SageMaker Ground Truth | Image classification, spam detection |
| **Unsupervised Learning** | Works with unlabeled data to find patterns.         | Requires methods to interpret patterns.| None specific          | Clustering, anomaly detection, LLMs for initial training phases |
| **Reinforcement Learning** | Learns through trial and error to maximize rewards. | Requires environment for agent interaction. | AWS DeepRacer      | Gaming, robotics, real-time decisions |


### Types of Diffusion Models

| Diffusion Model Type | Description                                          | When to Use                                  | Notes                 |
|----------------------|------------------------------------------------------|----------------------------------------------|--------------------------|
| **Forward Diffusion**| Adds noise to data progressively.                    | Not often used (it adds noise)    |   |
| **Reverse Diffusion**| Reconstructs original data from noise.               | Creating detailed images from distorted inputs. | Image restoration tools |
| **Stable Diffusion** | Works in reduced latent space, not directly in pixels. | Better then Reverse Diffusion | Midjourney, DALL-E       |


### Amazon SageMaker Inference Methods

| Inference Type     | Deployed To         | Characteristics                                                         |
|--------------------|---------------------|-------------------------------------------------------------------------|
| **Batch**          | EC2                 | Cost-effective for infrequent, large jobs                               |
| **Asynchronous**   | EC2                 | Suitable for non-time-sensitive applications and large payload          |
| **Serverless**     | Lambda              | Intermittent traffic, periods of no traffic, auto-scaling out of the box|
| **Real-Time**      | EC2                 | Live predictions, sustained traffic, low latency, consistent performance|


### Types of Training Data for Machine Learning/AI

| Data Type       | AWS Data Source Example                | Actual Example                           |
|-----------------|----------------------------------------|------------------------------------------|
| **Structured**  | SQL data stored in RDS then moved to S3| Customer information in relational tables|
| **Semi-Structured** | Data in DynamoDB or DocumentDB then moved to S3 | JSON logs of user activity           |
| **Unstructured**| Objects and files stored directly in S3| Images, videos, and PDF documents        |
| **Time-Series** | Time-stamped data stored in S3         | IoT device data, stock market data       |

### Generative AI performance metrics
| Metric Name                                         | Explanation                                                             |
|-----------------------------------------------------|-------------------------------------------------------------------------|
| **Recall Oriented Understudy for Gisting Evaluation (ROUGE)** | Measures overlap between generated and reference text, good for summaries. |
| **Bilingual Evaluation Understudy (BLEU)**           | Evaluates translation accuracy by comparing n-grams between outputs and references. |
| **General Language Understanding Evaluation (GLUE)** | Assesses model performance on multiple natural language understanding tasks. |
| **Holistic Evaluation of Language Models (HELM)**    | Provides broad, task-specific evaluation of language model capabilities.  |
| **Massive Multitask Language Understanding (MMLU)**  | Tests model knowledge across a variety of domains and topics.            |
| **Beyond the Imitation Game Benchmark (BIG-bench)**  | Evaluates models on creative and difficult AI tasks not covered by standard benchmarks. |
| **Perplexity**                                       | Measures how well a model predicts the likelihood of the next token or word. |

### Generative AI Models

| Generative AI Model                            | Examples                               | Use Case/What It's Good For                              |
|------------------------------------------------|----------------------------------------|----------------------------------------------------------|
| **Generative Adversarial Networks (GANs)**     | StyleGAN, CycleGAN, ProGAN             | Image generation, face synthesis, video creation          |
| **Variational Autoencoders (VAEs)**            | Kingma & Welling VAE, Beta-VAE         | Image denoising, anomaly detection, image compression     |
| **Transformers**                               | GPT-4, BERT, T5                        | Text generation, language translation, content generation |
| **Recurrent Neural Networks (RNNs)**           | LSTMs, GRUs                            | Sequential data, time series forecasting, language models |
| **Reinforcement Learning for Generative Tasks** | AlphaGo, DQN, OpenAI Five              | Game AI, autonomous control, optimizing generative tasks  |
| **Diffusion**                                  | Stable Diffusion, DALL·E 2, Imagen     | Image and text-to-image generation                        |
| **Flow-Based Models**                          | Glow, RealNVP                          | High-quality image generation, density estimation         |

### Study Sheets

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
| **Concept-Drift**                   | The relationship between inputs and outputs changes, meaning the model’s learned patterns no longer apply (e.g., new fraud patterns).                                |
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
