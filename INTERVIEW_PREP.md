# Comprehensive Interview Preparation Guide
## Roles: AI Engineer | Generative AI Engineer | Senior Software Engineer | ML Engineer | Computer Vision Engineer
### Target Locations: Munich · Amsterdam · Frankfurt · Berlin (Germany & Netherlands)
### Candidate: Md Ashikur Rahman — Lead AI Engineer, Vision-Language & Generative AI

---

> **How to use this guide:** Work through each section systematically. For each question, write out your answer in full sentences first, then condense to bullet points. Aim for the STAR format on behavioral questions (Situation → Task → Action → Result). Revisit weak areas weekly.

---

## Your Profile at a Glance (from Resume)

**Current role:** Lead AI Engineer, The KOW Company (Jan 2023–Present), leading 15+ engineers and researchers.

**Primary technical identity:**
- Vision-Language Models (VLMs): visual grounding, hallucination evaluation, topology faithfulness — active published researcher (ICDAR 2026, two arXiv preprints 2026)
- Production Computer Vision: salient object segmentation (U²-Net-based, 4.5M+ images), object detection, instance segmentation
- Generative AI: diffusion models, LoRA/QLoRA fine-tuning, prompt-guided image editing, ComfyUI, Diffusers
- LLM Applications: Llama, Qwen, prompt safety, hallucination evaluation, key-phrase extraction via SeamlessM4T + Llama 2
- 3D Vision: COLMAP-based SfM, multi-view stereo, Open3D, NeRF, 3D Gaussian Splatting
- Production Backend: FastAPI, Docker, Nginx, Redis, GCP, Google Cloud Storage, AWS S3, DynamoDB, SQL Server
- Early career: .NET/C# enterprise software, SQL Server optimization (query time: 20min → 40s on 4TB DB)

**Your key production systems:**
| System | What it is |
|--------|-----------|
| Retouched.ai | Salient object segmentation for background removal; 4.5M+ images globally |
| Omnimage.ai | Prompt-based image/video generation; Llama-based routing; 200+ brands |
| The Fitting Room | Cross-brand virtual try-on platform; 170+ brands; FastAPI/Docker/GCS/Redis |
| HoloSnap.ai | Multi-view 3D reconstruction; COLMAP, MVS, Open3D, NeRF, 3DGS |
| CogniX | Proprietary multimodal image generation/editing R&D; LoRA, Diffusers |
| Enterprise Catalog Audit | AI image-QA and catalog validation; CV + NLP + FastAPI for US retail client |
| KTM | .NET/SQL Server workflow optimization; integrated Omnimage.ai + Retouched.ai |
| Audio QA (Key-Phrase) | SeamlessM4T transcription + Llama 2 key-phrase extraction; customer-service QA |

**Your publications (be ready to explain all of these deeply):**
1. *Stroke-Level Connectivity Verification: Grounding VLMs Against Topology Hallucination in Diagram Understanding* — ICDAR 2026 (corresponding author)
2. *Step-Level Visual Grounding Faithfulness Predicts Out-of-Distribution Generalization in Long-Horizon VLMs* — arXiv 2026, under review
3. *Beyond Dominant Patches: Spatial Credit Redistribution for Grounded VLMs* — arXiv 2026, under review
4. *Automated Detection of Diabetic Retinopathy using Deep Residual Learning* — IJCA 2020

**Priority order for your profile** (spend most time on top items):
1. **Vision-Language Models** — your published research, expect very deep questions
2. **Computer Vision** — your longest-running production expertise
3. **Generative AI / LLMs** — deployed systems (Omnimage.ai, CogniX, Fitting Room)
4. **Deep Learning & Neural Networks** — foundation for all of above
5. **MLOps & System Design** — you have real production systems to discuss
6. **Python + Software Engineering** — coding interviews
7. **ML Fundamentals + Math** — theory grounding
8. **Behavioral** — you have rich project and leadership material
9. **DSA / Algorithms** — still tested; strengthen with practice
10. **Reinforcement Learning** — only study RLHF/DPO/GRPO sections; skip deep RL theory (not your background)
11. **Data Engineering, Cloud, SQL** — supporting knowledge; you have some practical exposure

---

## Table of Contents

0. [Your Resume-Based Talking Points (Behavioral Prep)](#0-your-resume-based-talking-points-behavioral-prep)
1. [Python Programming](#1-python-programming)
2. [Mathematics for Machine Learning](#2-mathematics-for-machine-learning)
3. [Machine Learning Fundamentals](#3-machine-learning-fundamentals)
4. [Deep Learning & Neural Networks](#4-deep-learning--neural-networks)
5. [Generative AI & Large Language Models (LLMs)](#5-generative-ai--large-language-models-llms)
5a. [Vision-Language Models (VLMs) — Your Primary Research Area](#5a-vision-language-models-vlms--your-primary-research-area)
6. [Computer Vision](#6-computer-vision)
7. [Natural Language Processing (NLP)](#7-natural-language-processing-nlp)
8. [Reinforcement Learning](#8-reinforcement-learning)
9. [Model Evaluation, Metrics & Experimentation](#9-model-evaluation-metrics--experimentation)
10. [Data Engineering & Pipelines](#10-data-engineering--pipelines)
11. [MLOps, Model Deployment & Serving](#11-mlops-model-deployment--serving)
12. [System Design for ML Systems](#12-system-design-for-ml-systems)
13. [Data Structures & Algorithms](#13-data-structures--algorithms)
14. [Software Engineering Best Practices](#14-software-engineering-best-practices)
15. [SQL & Databases](#15-sql--databases)
16. [Cloud & Infrastructure (AWS / GCP / Azure)](#16-cloud--infrastructure-aws--gcp--azure)
17. [AI Ethics, Fairness, Bias & Safety](#17-ai-ethics-fairness-bias--safety)
18. [Behavioral & Leadership Questions](#18-behavioral--leadership-questions)
19. [German / European Tech Market Specifics](#19-german--european-tech-market-specifics)

---

## 0. Your Resume-Based Talking Points (Behavioral Prep)

> These are the stories interviewers will ask you to elaborate on. Prepare a full STAR answer for each. Do not memorize — internalize.

### Retouched.ai (Salient Object Segmentation)
- **What to prepare:** Architecture choices for U²-Net-inspired segmentation; why this architecture over Mask R-CNN or DeepLab; how you measured the 17% quality improvement; what "2.27s average processing time" means in terms of throughput; how you handled 257 MB uploads reliably; how GCP infrastructure was structured; what happens at 4.5M-image scale operationally.
- **Likely questions:** "Walk me through the architecture." / "How did you achieve the 30% speed improvement?" / "How do you monitor quality at scale?" / "What would you do differently now?"

### Omnimage.ai (Image/Video Generation with LLM Routing)
- **What to prepare:** How Llama-based intent routing works (prompt → classification → model selection); how you handled multi-model selection; what reference-image conditioning involves technically; how you onboarded 200+ brands safely; what the API design looks like.
- **Likely questions:** "How did you design the routing logic?" / "What were the failure modes of prompt classification?" / "How do you handle inappropriate content?"

### The Fitting Room (Virtual Try-On, 170+ Brands)
- **What to prepare:** What the 2D try-on pipeline looks like technically (human parsing, clothing warping, try-on synthesis); why FastAPI + Docker + Nginx + Redis + SQL Server + GCS; how you handle cross-brand scale; what "recommendation workflows" means in this context.
- **Likely questions:** "How does virtual try-on work technically?" / "How did you manage 170+ brands with different catalog formats?"

### HoloSnap.ai (3D Reconstruction)
- **What to prepare:** COLMAP pipeline end-to-end (feature extraction → matching → SfM → dense reconstruction → MVS → meshing); why COLMAP; what Open3D was used for in mesh processing; what NeRF/3DGS added vs. MVS alone; what GLB/OBJ format requirements were; what the input video/image requirements were.
- **Likely questions:** "Explain SfM." / "Why did you choose COLMAP over other SfM tools?" / "What is the quality tradeoff between MVS and 3DGS?"

### CogniX (Proprietary Generative Image R&D)
- **What to prepare:** What "multi-reference fusion" means technically; how LoRA adaptation is used for garment/style; what QLoRA experiments involved; ComfyUI workflow design; why you're building proprietary vs. using APIs.
- **Likely questions:** "What is LoRA and how does fine-tuning work?" / "How do you evaluate generated image quality?" / "What is the business case for proprietary models?"

### ICDAR 2026 Paper (Topology Hallucination in VLMs)
- **What to prepare:** What stroke-level connectivity is; what topology hallucination means (VLM says two strokes are connected when they are not); how you designed the verification method; what the evaluation benchmark was; what findings were.
- **Likely questions:** "Tell me about your research." / "What is hallucination in VLMs?" / "What is visual grounding?" — this is your most impressive differentiator; practice a 2-minute and a 5-minute version.

### arXiv Papers (Visual Grounding Faithfulness / Spatial Credit Redistribution)
- **What to prepare:** What step-level faithfulness evaluation means in long-horizon VLMs; what "out-of-distribution generalization" means in this VLM context; what "dominant patches" are and why spatial credit redistribution matters for grounded VLMs; how these connect to your ICDAR paper.
- **Likely questions:** "What's the relationship between these papers?" / "What is the practical application?" / "What's next in this research direction?"

### Leading 15+ Engineers
- **What to prepare:** How you structure a team of engineers and researchers; how you maintain 90-95% on-time delivery; how you balance applied research with product delivery; how you handle a junior researcher who's stuck; how you translate business requirements from client to technical spec.
- **Likely questions:** "How do you lead a technical team?" / "How do you balance research and delivery?" / "How do you mentor junior engineers?"

### KTM System (SQL Server Optimization)
- **What to prepare:** What the original bottleneck was (query structure, indexing, full scans on 4TB); what specific optimizations reduced 20min to 40-54 seconds; how you integrated Omnimage.ai/Retouched.ai into the FTP/QC workflow.
- **Likely questions:** "Tell me about a time you optimized a slow system." — use this story.

### Early Career: Senior Software Engineer, Smart Technologies
- **What to prepare:** ERP supply-chain module scope; what "70-75% process automation" means; offline-capable enterprise data sync architecture; why this background is relevant (shows full-stack, enterprise-grade, and system-optimization experience before ML).
- **Likely questions:** "What is your background before ML?" / "Have you built non-ML production systems?"

---

---

## 1. Python Programming

> Core for all roles. Expect live coding, debugging, and design questions.

### Fundamentals

1. What is the difference between `is` and `==` in Python? Give an example where they differ.
2. Explain Python's GIL (Global Interpreter Lock). How does it affect multi-threading? How do you work around it?
3. What are Python generators? How do they differ from regular functions and lists? When would you use one?
4. Explain the difference between `@staticmethod`, `@classmethod`, and instance methods. When would you use each?
5. What are Python decorators? Write a decorator that measures execution time of any function.
6. What is the difference between `*args` and `**kwargs`? Can you use both in the same function? Show an example.
7. Explain Python's memory management and garbage collection. What is reference counting?
8. What are context managers (`with` statement)? How do you create a custom context manager using both a class and `contextlib`?
9. What is the difference between `deepcopy` and `copy`? When does it matter in ML workflows?
10. Explain list comprehensions, dict comprehensions, and set comprehensions. What are their performance characteristics?
11. What is the difference between `__str__` and `__repr__`? When does each get called?
12. What are dunder (magic/special) methods? Name 10 and explain their purpose.
13. Explain Python's MRO (Method Resolution Order). How does `super()` work in multiple inheritance?
14. What is the difference between `itertools.chain`, `itertools.product`, and `itertools.combinations`? Give practical ML use cases.
15. How do Python closures work? What is a free variable? Demonstrate with a factory function.

### Intermediate & Performance

16. What is the difference between `multiprocessing`, `threading`, and `asyncio`? Which would you use for CPU-bound ML training? For I/O-bound data loading?
17. How do you profile Python code? Name at least three profiling tools and explain the difference between CPU and memory profiling.
18. What are Python slots (`__slots__`)? How do they improve memory usage? When should you avoid them?
19. Explain `functools.lru_cache` and `functools.cache`. How do they differ? What are their limitations in ML pipelines?
20. What is the difference between `pickle`, `joblib`, and `cloudpickle`? Which do you use for serializing ML models and why?
21. How does Python handle integer overflow? How about floating-point precision? What are the implications for numerical computation?
22. What are abstract base classes (ABCs) in Python? How do you use `abc.ABC` and `@abstractmethod`?
23. Explain Python's descriptor protocol (`__get__`, `__set__`, `__delete__`). How do properties use this?
24. What is `__init_subclass__` and when would you use it?
25. Explain the difference between eager evaluation and lazy evaluation in Python. Give examples of each.

### NumPy / Pandas / Scientific Stack

26. What is broadcasting in NumPy? Explain with an example of adding a (3, 4) array with a (4,) array.
27. What is the difference between a NumPy view and a copy? When does slicing return a view vs. a copy? Why does this matter?
28. Explain vectorization in NumPy. Why is a vectorized operation faster than a Python loop?
29. How do you efficiently handle missing values in Pandas? Compare `dropna`, `fillna`, and imputation strategies.
30. What is the difference between `pd.merge`, `pd.concat`, and `pd.join`? When would you use each?
31. Explain the concept of "method chaining" in Pandas. What are its benefits and pitfalls?
32. How do you handle memory-efficient processing of datasets that do not fit in RAM using Pandas or alternatives like Polars, Dask, or Vaex?
33. What is the difference between `apply`, `map`, `applymap`, and `transform` in Pandas? What are their performance implications?
34. Write a function to normalize a 2D NumPy array column-wise without using any loops.
35. How do you detect and remove duplicate rows in a DataFrame while keeping the most recent entry based on a timestamp column?

---

## 2. Mathematics for Machine Learning

> Frequently tested in ML/AI Engineer roles. Expect both conceptual and applied questions.

### Linear Algebra

1. What is the geometric interpretation of matrix multiplication?
2. What is the rank of a matrix, and how does it relate to the linear independence of columns/rows?
3. Explain eigenvalues and eigenvectors. What do they represent geometrically?
4. What is PCA (Principal Component Analysis) mathematically? How is it related to eigendecomposition of the covariance matrix?
5. What is Singular Value Decomposition (SVD)? How does it differ from eigendecomposition? Where is it used in ML?
6. What is the Moore-Penrose pseudoinverse? When is it used instead of a regular matrix inverse?
7. What is a positive definite matrix? Why do covariance matrices need to be positive semi-definite?
8. Explain the dot product and its relationship to cosine similarity. Why is cosine similarity useful for text and embedding comparisons?
9. What is the Frobenius norm? When is it used in deep learning regularization?
10. What is the determinant of a matrix, and what does it signify geometrically?

### Calculus & Optimization

11. What is a gradient? What is the relationship between gradient, partial derivatives, and the direction of steepest ascent?
12. Explain the chain rule. How is it applied in backpropagation?
13. What is the difference between a local minimum, global minimum, and saddle point? How do optimizers handle saddle points?
14. What is the Jacobian matrix? What is the Hessian matrix? Where are they used in optimization?
15. Derive the update rule for gradient descent from first principles.
16. What is the difference between convex and non-convex optimization? Why does non-convexity make neural network training challenging?
17. What is L'Hôpital's Rule and when is it relevant to ML (e.g., vanishing gradients)?
18. Explain Newton's method for optimization. Why is it rarely used for deep learning despite faster convergence?
19. What is automatic differentiation (autograd)? How does it differ from symbolic differentiation and numerical differentiation?
20. What is the Lagrangian and KKT conditions? How do they relate to SVMs?

### Probability & Statistics

21. What is Bayes' Theorem? Write it out and explain each term. Give an ML example.
22. What is the difference between MLE (Maximum Likelihood Estimation) and MAP (Maximum A Posteriori) estimation?
23. What is the Central Limit Theorem? Why does it matter for ML training and evaluation?
24. Explain the difference between frequentist and Bayesian interpretations of probability.
25. What is the difference between variance and bias in statistical estimation?
26. What is a p-value? What are its common misinterpretations? When should you use it in A/B testing?
27. What is the difference between a normal distribution, log-normal distribution, and Poisson distribution? Give an ML use case for each.
28. What is KL divergence? Is it symmetric? How is it used in VAEs and other generative models?
29. What is mutual information? How does it relate to feature selection?
30. Explain the difference between Type I error (false positive) and Type II error (false negative). How does the decision threshold affect them?
31. What is a confidence interval? How does it differ from a credible interval in Bayesian statistics?
32. What is the law of large numbers and why does it justify using mini-batches in SGD?
33. What is the difference between covariance and correlation? When can correlation be misleading?
34. Explain Markov chains. What is the stationary distribution? How is it related to MCMC methods?
35. What is the difference between a parametric and a non-parametric test? Give an ML-relevant example of each.

---

## 3. Machine Learning Fundamentals

> Core of all ML/AI roles. Deep understanding expected at Senior level.

### Supervised Learning

1. Explain the bias-variance tradeoff in detail. How does model complexity affect each? How do you find the sweet spot?
2. What is regularization? Explain L1 (Lasso), L2 (Ridge), and Elastic Net. What are their geometric interpretations and effects on coefficients?
3. Derive the closed-form solution for linear regression (ordinary least squares). Under what conditions does it fail?
4. What is logistic regression? What assumptions does it make? How does it handle multi-class classification?
5. How does a decision tree split nodes? What are the splitting criteria (Gini impurity, information gain, variance reduction)? Derive Gini impurity.
6. What is overfitting? Name at least 5 techniques to prevent it.
7. How does Random Forest work? What are the key hyperparameters? What is out-of-bag (OOB) error?
8. Explain gradient boosting. How does it differ from AdaBoost? What are XGBoost's key innovations over vanilla gradient boosting?
9. What is a support vector machine (SVM)? Explain the concept of the margin, support vectors, and the kernel trick. What is the dual formulation?
10. What is the kernel trick? Name 4 common kernels and when to use each.
11. What is k-Nearest Neighbors (kNN)? What are its computational complexities for training and inference? How do you choose k?
12. What is Naive Bayes? What is the "naive" assumption? Under what conditions does it still perform well despite the assumption being violated?
13. What is the difference between discriminative and generative models? Give 3 examples of each.
14. How does a learning curve differ from a validation curve? What information does each provide?
15. What is early stopping? How do you implement it correctly to avoid data leakage?

### Unsupervised Learning

16. Explain the k-Means clustering algorithm. What is the objective function? What are its limitations? How does k-Means++ improve initialization?
17. What is DBSCAN? How does it handle noise and arbitrary cluster shapes? What are `eps` and `minPts`?
18. How does hierarchical clustering work? What is the difference between agglomerative and divisive approaches? What is a dendrogram?
19. Explain the Expectation-Maximization (EM) algorithm. What is the connection to Gaussian Mixture Models (GMM)?
20. What is t-SNE? What are its known limitations? Why shouldn't you interpret cluster distances in a t-SNE plot?
21. What is UMAP? How does it compare to t-SNE in terms of preserving global vs. local structure?
22. What is an autoencoder? What is the bottleneck? What is a variational autoencoder (VAE)?

### Feature Engineering & Selection

23. What is the difference between feature selection, feature extraction, and feature construction?
24. How do you handle imbalanced datasets? Name at least 6 strategies including both data-level and algorithm-level approaches.
25. What is the difference between label encoding and one-hot encoding? When is each appropriate? What is target encoding and its risks?
26. How do you handle missing values in a dataset? When should you impute vs. drop?
27. What is multicollinearity? How do you detect it (VIF, correlation matrix)? How does it affect regression models?
28. What is feature importance in tree-based models? What are the different methods (MDI, permutation importance)? Which is more reliable?
29. What is data leakage? Give 3 concrete examples of how it can occur and how to prevent it.
30. How do you perform cross-validation? What is the difference between k-fold, stratified k-fold, time-series split, and group k-fold? When does each apply?
31. What is the difference between train/validation/test splits? Why is the test set sacrosanct?
32. What is SMOTE? How does it oversample minority classes? What are its pitfalls?
33. How do you normalize vs. standardize features? When does normalization matter (e.g., for SVMs vs. tree models)?
34. What is target leakage vs. train-test leakage? How do you detect each?
35. How would you approach building an ML model from scratch on a new dataset? Walk me through your full workflow.

---

## 4. Deep Learning & Neural Networks

> Expected in depth for AI Engineer and Senior ML Engineer roles.

### Architecture & Theory

1. What is the Universal Approximation Theorem? What does it guarantee and what does it NOT guarantee?
2. Explain the vanishing gradient problem. What causes it? How is it addressed (activation functions, normalization, skip connections)?
3. What is the exploding gradient problem? How do gradient clipping and weight initialization help?
4. Compare activation functions: ReLU, Leaky ReLU, ELU, SELU, GELU, Swish, Sigmoid, Tanh. When would you choose each?
5. What is Batch Normalization? How does it work? What is the difference between training and inference behavior?
6. What is Layer Normalization? How does it differ from Batch Normalization? When is it preferred (e.g., Transformers)?
7. What is Dropout? How does it work differently at training vs. inference? What is the theoretical justification (ensemble approximation)?
8. Explain weight initialization. Compare Xavier/Glorot, He initialization, and orthogonal initialization. How do they prevent vanishing/exploding gradients?
9. What is the difference between a fully connected (dense) layer and a convolutional layer in terms of parameters, computation, and inductive biases?
10. What is the receptive field of a convolutional layer? How do pooling, stride, and dilation affect it?

### Training & Optimization

11. Explain SGD, Momentum, RMSprop, Adam, AdamW, and Adafactor. What are the tradeoffs? When is SGD with momentum preferred over Adam?
12. What is learning rate scheduling? Explain cosine annealing, warmup, ReduceLROnPlateau, and OneCycleLR.
13. What is gradient accumulation? When and how do you use it?
14. What is mixed precision training (FP16/BF16)? How does loss scaling work? What is the benefit over full FP32?
15. What is the difference between model parallelism, data parallelism, and pipeline parallelism? When would you use each?
16. What is gradient checkpointing (activation checkpointing)? What is the memory vs. compute tradeoff?
17. How do you detect and fix unstable training? What do loss curves tell you about underfitting, overfitting, and exploding gradients?
18. What is curriculum learning? Give an example of when it helps.
19. Explain knowledge distillation. What is the role of the temperature parameter? What is soft vs. hard target distillation?
20. What is transfer learning? What is the difference between feature extraction and fine-tuning? When is each appropriate?

### Architecture Types

21. Explain the architecture of a Convolutional Neural Network (CNN). What are the roles of conv layers, pooling, and FC layers?
22. What is a Residual Network (ResNet)? Why do skip connections help training? Explain the bottleneck block.
23. What is a Recurrent Neural Network (RNN)? What is the vanishing gradient problem in RNNs specifically?
24. What is an LSTM? Explain all four gates (forget, input, cell, output). How does it solve the vanishing gradient problem vs. vanilla RNN?
25. What is a GRU? How does it compare to LSTM in terms of parameters and performance?
26. Explain the Transformer architecture in detail: multi-head self-attention, positional encoding, feed-forward layers, encoder, decoder.
27. What is the attention mechanism? Derive the scaled dot-product attention formula. Why is it scaled by √d_k?
28. What is a Vision Transformer (ViT)? How does it differ from a CNN? What are its strengths and weaknesses?
29. What is a Graph Neural Network (GNN)? What is message passing? Name 3 GNN variants (GCN, GAT, GraphSAGE).
30. What is a Diffusion Model at a high level? How does the forward and reverse process work?
31. What is a Normalizing Flow? How does it differ from a VAE and GAN?
32. What is a GAN? Explain the minimax objective. What is mode collapse and how do you address it?
33. What is U-Net and why was it designed for medical image segmentation?
34. What is a Siamese network? What is a contrastive loss and triplet loss? Where are they used?
35. What is self-supervised learning? Give 3 concrete examples (SimCLR, BYOL, MAE).

---

## 5. Generative AI & Large Language Models (LLMs)

> Critical for Generative AI Engineer roles. Very high depth expected.

### Transformer & Pre-training

1. Explain the GPT architecture (decoder-only Transformer). How does causal masking work and why is it needed?
2. What is BERT? How does masked language modeling (MLM) work? How does it differ from GPT's causal LM?
3. What is the difference between encoder-only, decoder-only, and encoder-decoder architectures? Give an example model for each.
4. What is tokenization? Explain BPE (Byte Pair Encoding), WordPiece, and SentencePiece. What is the tradeoff in vocabulary size?
5. What is positional encoding? What are the differences between sinusoidal (absolute), learned, RoPE (Rotary Position Embedding), and ALiBi?
6. What is the context window/sequence length? What are the memory and computational challenges of extending it?
7. What is Flash Attention? How does it reduce memory complexity? What is the key algorithmic trick (tiling)?
8. What is sparse attention? Name 3 sparse attention patterns (Longformer, BigBird, etc.) and explain the tradeoff.
9. What is a KV cache? How does it speed up autoregressive inference? What are its memory implications?
10. What is the quadratic complexity problem of full self-attention (O(n²))? What approaches address it?

### Fine-tuning & Adaptation

11. What is instruction fine-tuning? How does it differ from pre-training? What data format does it require?
12. What is RLHF (Reinforcement Learning from Human Feedback)? Explain the 3 stages: SFT, reward model training, PPO fine-tuning.
13. What is DPO (Direct Preference Optimization)? How does it simplify RLHF? What are its limitations?
14. What is PEFT (Parameter-Efficient Fine-Tuning)? Name at least 4 PEFT methods.
15. Explain LoRA (Low-Rank Adaptation) in detail. What is the mathematical formulation? Why are low-rank updates sufficient?
16. What is QLoRA? How does 4-bit quantization interact with LoRA? What is NormalFloat4 (NF4)?
17. What is catastrophic forgetting? How do you mitigate it during fine-tuning?
18. What is continual learning (lifelong learning)? How is it different from regular fine-tuning?
19. What is domain adaptation? How does it differ from fine-tuning for a specific task?
20. What are soft prompts / prompt tuning? How do they differ from prefix tuning and LoRA?

### Inference & Serving

21. What is beam search? What is greedy search? What is top-k sampling and top-p (nucleus) sampling? How does temperature affect generation?
22. What is speculative decoding? How does it speed up inference without changing the output distribution?
23. What is quantization? Explain INT8, INT4, GPTQ, AWQ, and bitsandbytes. What are the accuracy vs. speed tradeoffs?
24. What is model pruning? What is structured vs. unstructured pruning? What is the lottery ticket hypothesis?
25. What is vLLM? What is PagedAttention? How does it solve KV cache fragmentation?
26. What is continuous batching in LLM serving? How does it improve GPU utilization compared to static batching?
27. What are the key metrics for LLM serving? (TTFT, TBT/TPOT, throughput tokens/s, latency P99)

### RAG & Agents

28. What is Retrieval-Augmented Generation (RAG)? What problem does it solve? Describe the full pipeline.
29. What is the difference between naive RAG, advanced RAG, and modular RAG? What are the main failure modes of RAG?
30. What is a vector database? Name 4 (Pinecone, Weaviate, Qdrant, Chroma, FAISS). How does approximate nearest neighbor (ANN) search work?
31. What is HNSW (Hierarchical Navigable Small World)? How does it achieve O(log n) ANN search?
32. What is an LLM agent? What is the ReAct framework? What is chain-of-thought (CoT) prompting?
33. What is tool use / function calling in LLMs? How do you implement it reliably?
34. What is prompt injection? How do you defend against it in production systems?
35. What are hallucinations in LLMs? What are the categories (intrinsic, extrinsic, factual)? Name at least 5 mitigation strategies.
36. What is Constitutional AI (CAI)? How does it differ from RLHF?
37. What are evaluation frameworks for LLMs? (BLEU, ROUGE, BERTScore, MT-Bench, MMLU, HumanEval, LM-Eval Harness)
38. What is the difference between fine-tuning a model and using it via in-context learning (few-shot prompting)? When is each preferable?
39. What is a mixture of experts (MoE) model? How does sparse gating work? Name 2 MoE LLMs.
40. What is multi-modal AI? Explain how models like GPT-4V, LLaVA, and Flamingo integrate vision and text.

---

## 5a. Vision-Language Models (VLMs) — Your Primary Research Area

> This is your strongest differentiator. You have three 2026 publications in this space. Expect very deep questions here. Master every question below.

### Architecture & Foundations

1. What is a Vision-Language Model (VLM)? How does it fundamentally differ from a pure LLM and a pure CV model?
2. How does a VLM align vision and language modalities? Describe the alignment training paradigm (e.g., contrastive pre-training as in CLIP vs. generative alignment as in LLaVA).
3. What is visual grounding? What is the difference between referring expression comprehension, visual question answering, and grounded captioning?
4. Explain the architecture of LLaVA. How does the visual encoder connect to the LLM decoder? What is the projection layer?
5. What is CLIP? How is it trained? How is it used as the visual backbone in LLaVA and similar models?
6. What is the difference between using a ViT encoder vs. a CNN encoder as the visual backbone in a VLM? What are the tradeoffs?
7. What are image tokens in a VLM? How does LLaVA represent an image as tokens fed to the LLM?
8. What is visual instruction tuning? How is the LLaVA dataset constructed? What is the role of GPT-4 in generating instruction-following data?
9. What is InstructBLIP? How does its Q-Former module work? How does it differ from LLaVA's approach?
10. What is Flamingo? What is the gated cross-attention mechanism used to inject visual features? How does it enable few-shot visual learning?
11. What is PaliGemma? What is Idefics? What is InternVL? How do they differ in their vision-language fusion approach?
12. What is GPT-4V / GPT-4o? What do we know about their architecture? What capabilities do they have beyond LLaVA?
13. What is Qwen-VL? What is its training pipeline and what makes it strong for Chinese-language vision-language tasks?
14. What is the role of spatial resolution in VLMs? How does image resolution affect VLM performance? What is the "anyres" or dynamic resolution approach?
15. What is a multimodal projector? Compare MLP projector (LLaVA-1.5), Q-Former (BLIP-2/InstructBLIP), and perceiver resampler (Flamingo). What are the tradeoffs?

### Hallucination in VLMs

16. What is hallucination in VLMs? What are the main categories: object hallucination, attribute hallucination, relation hallucination, and topological/structural hallucination?
17. What is POPE (Polling-based Object Probing Evaluation)? How does it measure object hallucination? What are its limitations?
18. What is CHAIR (Caption Hallucination Assessment with Image Relevance)? How is it computed? What does it measure vs. POPE?
19. What is MMHal-Bench? What is HallusionBench? What aspects of hallucination do they evaluate?
20. What causes hallucination in VLMs? List and explain at least 5 root causes (e.g., training data distribution, language prior dominance, positional bias, attention sparsity, insufficient grounding supervision).
21. What is spatial/topological hallucination specifically? How does it differ from object-level hallucination? (Directly relevant to your ICDAR 2026 paper)
22. What is visual grounding faithfulness? How do you evaluate whether a VLM's reasoning is actually grounded in the image vs. relying on language priors?
23. What is the dominant patch problem in VLMs? Why do attention weights concentrate on a small number of image patches? (Directly relevant to your "Beyond Dominant Patches" paper)
24. What is spatial credit redistribution in the context of visual attention? What is the intuition behind it?
25. What is step-level faithfulness evaluation in long-horizon VLMs? How does it differ from single-step or final-answer evaluation? (Directly relevant to your arXiv preprint)
26. How does step-level faithfulness correlate with out-of-distribution (OOD) generalization? What is the intuition behind this finding?
27. What mitigation strategies exist for VLM hallucination? Compare: RLHF-based, contrastive decoding, improved grounding supervision, visual augmentation, and inference-time corrections.
28. What is contrastive decoding for hallucination reduction (VCD — Visual Contrastive Decoding)? How does it work?
29. What is OPERA (Over-Trust Penalty and Retrospection-Allocation)? How does it address hallucination at the decoding stage?
30. What is ICD (Instruction Contrastive Decoding)? How does it suppress language prior dominance?

### Grounding, Localization & Diagram Understanding

31. What is referring expression comprehension (REC)? Name standard benchmarks (RefCOCO, RefCOCO+, RefCOCOg). What makes a good REC model?
32. What is phrase grounding? How is it evaluated? (Flickr30k Entities)
33. What is grounded VQA? How does it require both visual evidence and a correct answer?
34. What is diagram understanding in VLMs? Why is it harder than natural image understanding?
35. What is stroke-level connectivity in diagrams? Why is verifying topological correctness a non-trivial grounding task? (Core of your ICDAR 2026 paper)
36. What is the difference between semantic correctness and structural/topological correctness in diagram interpretation by a VLM?
37. What are the failure modes of VLMs on OCR-heavy tasks, charts, and structured diagrams?
38. What is ChartQA? What is DocVQA? What is TextVQA? What specific challenges do they expose in VLMs?
39. What is the role of position encodings in enabling spatial reasoning in VLMs?
40. How do you build a ground truth dataset for topological/structural hallucination evaluation? What were the annotation challenges?

### Fine-tuning & Adaptation of VLMs

41. How do you fine-tune a VLM efficiently? Compare full fine-tuning, LoRA on LLM backbone only, LoRA on both vision and LLM, and vision encoder freezing strategies.
42. What are the common failure modes when fine-tuning a VLM on a domain-specific dataset (e.g., catalog images, product photography)?
43. What is catastrophic forgetting in VLMs during fine-tuning? How do you mitigate it?
44. How do you construct a high-quality visual instruction tuning dataset for a domain-specific VLM?
45. What is prompt safety in VLMs? How does it differ from prompt safety in text-only LLMs? How do visual inputs create new attack surfaces?

---

## 6. Computer Vision

> Deep expertise expected for Computer Vision Engineer roles.

### Classical CV & Foundations

1. What is the difference between image classification, object detection, semantic segmentation, instance segmentation, and panoptic segmentation?
2. What is a convolution operation? What is the difference between cross-correlation and convolution (as used in CNNs)?
3. What are filters/kernels? Explain Sobel, Laplacian, and Gaussian filters and their use in edge detection.
4. What is image padding (same vs. valid)? How do you calculate the output size of a convolutional layer?
5. What is pooling? Compare max pooling, average pooling, global average pooling (GAP). Why is GAP preferred over FC layers in modern architectures?
6. What is the difference between stride and dilation (atrous convolution)? How does dilation affect the receptive field without reducing spatial resolution?
7. What is depthwise separable convolution? How does MobileNet use it? What is the parameter reduction factor?
8. What is the Histogram of Oriented Gradients (HOG) feature descriptor? Where was it classically used?
9. What is SIFT? Why is it scale and rotation invariant?
10. What is the difference between feature matching and feature tracking? Name algorithms for each.

### Object Detection

11. Explain the R-CNN family: R-CNN → Fast R-CNN → Faster R-CNN. What was the key improvement at each step?
12. What is a Region Proposal Network (RPN)? What are anchors? How are they used to generate bounding box proposals?
13. What is YOLO? What is the key innovation vs. two-stage detectors? Explain the grid-based detection paradigm.
14. What is the difference between YOLO v1 and modern variants (YOLOv8, YOLOv9)? What are the key improvements?
15. What is Non-Maximum Suppression (NMS)? How does Soft-NMS improve it? What is DIoU-NMS?
16. What are anchor-based vs. anchor-free detectors? Give examples of each. What are the tradeoffs?
17. What is DETR (Detection Transformer)? How does it eliminate anchor boxes and NMS using bipartite matching?
18. What are the standard IoU thresholds for COCO evaluation? Explain mAP@0.5 and mAP@[0.5:0.95].

### Segmentation & 3D Vision

19. Explain Mask R-CNN. What does RoIAlign do differently from RoIPool? Why does it matter for segmentation?
20. What is DeepLab? What are dilated convolutions and ASPP (Atrous Spatial Pyramid Pooling)?
21. What is SAM (Segment Anything Model)? What is its promptable segmentation paradigm?
22. What is optical flow? How does Lucas-Kanade differ from Farneback? What are they used for?
23. What is depth estimation? What is the difference between monocular, stereo, and LiDAR-based depth?
24. What is camera calibration? What are intrinsic and extrinsic parameters? What is the camera matrix K?
25. What are homogeneous coordinates? What is a homography matrix and when is it used?
26. What is the epipolar constraint? What is the fundamental matrix F and essential matrix E?
27. What is Structure from Motion (SfM)? How does it relate to SLAM?
28. What are Neural Radiance Fields (NeRF)? What do they represent? What is the rendering process?
29. What is 3D Gaussian Splatting? How does it differ from NeRF in representation and speed?

### Generative Models for Vision

30. What is a GAN for image generation? Compare DCGAN, StyleGAN2, and BigGAN.
31. What is a Latent Diffusion Model (LDM)? How does Stable Diffusion use a VAE to reduce the dimensionality?
32. What is classifier-free guidance (CFG) in diffusion models? What does the guidance scale control?
33. What is ControlNet? How does it add spatial conditioning to a frozen diffusion model?
34. What is CLIP? How is it trained with contrastive learning? How is it used for zero-shot classification?
35. What is image augmentation? Name 10 augmentation techniques and explain when each is appropriate (RandomCrop, ColorJitter, Mixup, CutMix, etc.).

---

## 7. Natural Language Processing (NLP)

> Required for AI Engineer and Generative AI Engineer roles.

### Classical NLP

1. What is tokenization in classical NLP? What are the challenges with whitespace-based tokenization for non-English languages?
2. What is stemming vs. lemmatization? When does the distinction matter?
3. What is TF-IDF? Derive the formula. What are its limitations?
4. What is Word2Vec? Explain both the Skip-gram and CBOW architectures. What is negative sampling?
5. What is GloVe? How does it differ from Word2Vec? What is the global co-occurrence matrix?
6. What is FastText? How does it handle out-of-vocabulary words?
7. What is the difference between syntactic parsing and semantic parsing?
8. What is Named Entity Recognition (NER)? What are common tagging schemes (BIO, BIOES)?
9. What is POS tagging? What is dependency parsing? What is constituency parsing?
10. What is coreference resolution? Why is it challenging?

### Modern NLP (Transformers & Beyond)

11. What is the BERT fine-tuning paradigm? What is the [CLS] token used for?
12. What is sentence embedding? Compare BERT embeddings, Sentence-BERT (SBERT), and E5/BGE models. What is mean pooling vs. [CLS] pooling?
13. What is cross-encoder vs. bi-encoder for sentence similarity? What are their speed/accuracy tradeoffs?
14. What is the difference between extractive QA and abstractive QA?
15. What is text summarization? Compare extractive vs. abstractive approaches.
16. What is machine translation? Explain the seq2seq with attention model that preceded Transformers.
17. What is zero-shot, one-shot, and few-shot classification? How does GPT-3 demonstrate in-context learning?
18. What are text embeddings used for? Name 5 downstream tasks that use them.
19. What is semantic search vs. keyword search? How does BM25 work? How do dense retrievers improve on it?
20. What is ColBERT? How does late interaction differ from standard bi-encoder retrieval?

### Evaluation & Multilingual

21. What is BLEU score? What are its limitations for NLG evaluation?
22. What is ROUGE? What are ROUGE-1, ROUGE-2, and ROUGE-L?
23. What is BERTScore? How does it improve upon BLEU?
24. What is perplexity? How is it calculated? What does a lower perplexity mean?
25. What is a language model's train/eval data contamination problem?
26. What is multilingual NLP? How do mBERT and XLM-R handle multiple languages? What is cross-lingual transfer?
27. What are the challenges of NLP for German, Dutch, and other morphologically rich languages?
28. What is subword tokenization's advantage for morphologically rich languages?
29. What is the difference between text classification, sequence labeling, and sequence-to-sequence tasks?
30. What is document chunking in RAG? What are the key chunking strategies (fixed-size, sentence, semantic)? How does chunk size affect retrieval quality?
31. How do you evaluate a chatbot or conversational AI system? What metrics do you use?
32. What is constitutional AI and RLAIF?
33. What is the Needle-in-a-Haystack test for LLMs? What does it measure?
34. What is LLM grounding? How do you ground an LLM to a knowledge base?
35. What are common failure modes in LLM-based NLP applications?

---

## 8. Reinforcement Learning

> **For your profile:** You do not have RL engineering experience on your resume. Do NOT claim it. Focus exclusively on the RLHF/DPO/GRPO sub-section (questions 1–8 and 18–20 below) since those directly connect to your LLM fine-tuning and hallucination work. Skip deep RL theory (DQN, SAC, MCTS etc.) unless a role specifically lists it.

> **What you CAN honestly connect to RL:** RLHF is the training paradigm behind the LLMs you use (Llama, Qwen). DPO is a simpler RLHF alternative. GRPO is used in DeepSeek-R1 which relates to your LLM routing work. Reward modeling connects to your hallucination evaluation research (reward signal for grounding faithfulness).

### RLHF / DPO / GRPO — Focus Area

1. What is the Markov Decision Process (MDP)? Define all components: S, A, P, R, γ.
2. What is the Bellman equation? What is the Bellman optimality equation for Q-values?
3. What is the difference between model-based and model-free RL?
4. What is Q-learning? Derive the update rule. What is the convergence guarantee?
5. What is Deep Q-Network (DQN)? What are experience replay and target networks, and why are they needed?
6. What is the difference between on-policy and off-policy learning? Give an example of each.
7. What is SARSA? How does it differ from Q-learning?
8. What is a policy gradient method? Derive the policy gradient theorem (REINFORCE).
9. What is the Actor-Critic architecture? What is the Advantage function?
10. What is Proximal Policy Optimization (PPO)? What problem does the clipped objective solve?
11. What is Soft Actor-Critic (SAC)? What is the entropy maximization objective?
12. What is the exploration-exploitation tradeoff? Explain ε-greedy, UCB, and Thompson sampling.
13. What is reward shaping? What are potential-based shaping functions and why do they preserve optimal policy?
14. What is inverse reinforcement learning (IRL)? How is it related to imitation learning?
15. What is multi-armed bandit problem? How is it a special case of RL?
16. What is the credit assignment problem in RL?
17. What is Monte Carlo Tree Search (MCTS)? How does AlphaGo use it?
18. What is GRPO (Group Relative Policy Optimization)? How is it used to train LLMs (e.g., DeepSeek-R1)?
19. What is reward hacking / reward gaming? Give an example and how to prevent it.
20. What is RLHF at a technical level? Describe the PPO training loop applied to an LLM.
21. What is distributional RL? How does it differ from standard value-based RL?
22. What is hierarchical RL? What problem does it address?
23. What is multi-agent RL (MARL)? What is the difference between cooperative and competitive settings?
24. What is offline RL (batch RL)? What is the distributional shift problem it faces?
25. What is Conservative Q-Learning (CQL)? Why is it useful for offline RL?
26. What are the key RL frameworks? (Gymnasium, Stable-Baselines3, Ray RLlib, TorchRL)
27. How does RL differ from supervised learning in terms of data collection and feedback?
28. What is the difference between sparse and dense rewards? How do you handle sparse rewards?
29. What are common RL environments used for benchmarking? (MuJoCo, Atari, MineDojo, etc.)
30. What is curriculum learning in RL and how does it help with hard exploration problems?

---

## 9. Model Evaluation, Metrics & Experimentation

> Critical for all roles. Often overlooked but always tested.

1. What is precision, recall, F1 score? Write the formulas from scratch. When is F1 insufficient and you should use F-beta?
2. What is AUC-ROC? What does an AUC of 0.5 mean? What does 1.0 mean? When is AUC-ROC misleading?
3. What is AUC-PR (Precision-Recall curve)? When is it preferred over ROC-AUC (hint: imbalanced datasets)?
4. What is the confusion matrix? What are TP, TN, FP, FN? What is Balanced Accuracy?
5. What is Matthews Correlation Coefficient (MCC)? Why is it considered the most informative single metric for binary classification?
6. What is the difference between micro-averaging, macro-averaging, and weighted averaging for multi-class metrics?
7. What is Mean Squared Error (MSE), Root MSE, Mean Absolute Error (MAE), MAPE, and Huber loss? When would you prefer MAE over MSE?
8. What is R² (coefficient of determination)? Can it be negative? What does that mean?
9. What is log loss (cross-entropy loss)? Why is it used for probabilistic classifiers?
10. What is calibration of a probabilistic classifier? What is a reliability diagram? What is Platt scaling and isotonic regression?
11. What is the difference between online evaluation and offline evaluation of an ML model?
12. What is an A/B test? What is the minimum sample size needed? How do you calculate statistical power?
13. What is a p-value in A/B testing? What is a Type I error rate? What is multiple testing correction (Bonferroni, Benjamini-Hochberg)?
14. What is the novelty effect in A/B testing? How do you account for it?
15. What is holdout evaluation vs. cross-validation? When do you use each?
16. What is the difference between validation loss and test loss? Why can validation loss be lower than test loss in some settings?
17. What is stratified sampling? Why is it important for evaluation on imbalanced data?
18. What is the difference between accuracy, top-1 accuracy, and top-5 accuracy? Where is top-5 used?
19. What is mean Average Precision (mAP) in object detection? Walk through the calculation step by step.
20. What is Intersection over Union (IoU)? What is GIoU, DIoU, CIoU? Why were they introduced?
21. What is FID (Fréchet Inception Distance) for evaluating generative image models?
22. What is CLIP score for evaluating text-to-image generation?
23. What are the key metrics for ranking systems? (NDCG, MRR, MAP, Precision@k, Recall@k)
24. What is shadow mode deployment? How does it help safely evaluate a new model?
25. What is the difference between a model monitor and a data monitor in production ML?
26. What is concept drift vs. data drift vs. model drift? How do you detect each?
27. How do you compare two models statistically? What is the McNemar's test?
28. What is the difference between a metric and a loss function? Do they need to be the same?
29. What is MMLU? What is HumanEval? What limitations do LLM benchmarks have?
30. How would you design an evaluation framework for a RAG system? What are the key components (faithfulness, answer relevance, context relevance)?
31. What is RAGAS? What metrics does it compute?
32. What is the problem with using BLEU to evaluate code generation?
33. How do you handle evaluation when ground truth labels are expensive or unavailable?
34. What is LLM-as-a-judge? What are its biases and limitations?
35. What is an ablation study? Why is it important for publishing ML results?

---

## 10. Data Engineering & Pipelines

> Required for all Senior roles. ML pipelines are 80% data engineering.

1. What is an ETL pipeline vs. an ELT pipeline? When is ELT preferred in modern data stacks?
2. What is Apache Spark? What is a DataFrame vs. an RDD? When should you use each?
3. What is lazy evaluation in Spark? How does it enable optimization? What is the difference between transformations and actions?
4. What is data partitioning in Spark? What is data skew and how do you handle it?
5. What is Apache Kafka? What is a topic, partition, consumer group, and offset?
6. What is a streaming data pipeline? Compare micro-batch (Spark Structured Streaming) vs. true streaming (Apache Flink).
7. What is a feature store? Name 3 feature store solutions (Feast, Hopsworks, Tecton). What problems do they solve?
8. What is the difference between online and offline feature serving?
9. What is a data lake vs. a data warehouse vs. a data lakehouse?
10. What is the medallion architecture (Bronze/Silver/Gold)?
11. What is Delta Lake? What ACID properties does it provide over regular Parquet?
12. What is Apache Airflow? What is a DAG, Operator, and Sensor? What are common pitfalls?
13. What is dbt (data build tool)? How does it fit into the modern data stack?
14. What is data versioning? Name tools for versioning datasets (DVC, LakeFS, Delta Lake).
15. What is schema evolution? How do Parquet and Avro handle it differently?
16. What is serialization format comparison? Compare CSV, JSON, Parquet, Avro, ORC. When would you choose each?
17. What is a data catalog? What is Apache Atlas or AWS Glue Data Catalog?
18. What are the GDPR implications for ML data pipelines? What is data retention, right to erasure, and purpose limitation?
19. What is a Lambda architecture? What is a Kappa architecture? What are the tradeoffs?
20. What is exactly-once semantics in stream processing? How does Kafka achieve it?
21. What is backpressure in stream processing? How do you handle it?
22. What is data lineage? Why is it important for ML? What tools track it (OpenLineage, Marquez)?
23. What is a data contract? Why is it becoming important in modern data engineering?
24. How do you handle large-scale image/video data in ML pipelines? (TFRecords, WebDataset, LMDB, Petastorm)
25. What is a training data pipeline for LLMs? What are the key components (deduplication, quality filtering, tokenization)?
26. How do you build a data deduplication pipeline at scale? What is MinHash LSH?
27. What is data quality monitoring? Name tools and metrics used (Great Expectations, dbt tests, etc.).
28. How do you handle data at petabyte scale? What are the key challenges?
29. What is the N+1 query problem in databases? How does it relate to batch fetching?
30. What is change data capture (CDC)? How does Debezium work?
31. What is a vector data pipeline? How do you build a pipeline that keeps embeddings in a vector DB in sync with a source database?
32. What is infrastructure-as-code for data pipelines? (Terraform, Pulumi)
33. What is a column-store database? Why is it better than row-store for analytics?
34. What is Iceberg vs. Hudi vs. Delta Lake? What problems do open table formats solve?
35. How would you design a real-time feature pipeline for a fraud detection system?

---

## 11. MLOps, Model Deployment & Serving

> Critical for Senior ML Engineer and AI Engineer roles.

### Experiment Tracking & Versioning

1. What is MLflow? What are its four main components (Tracking, Projects, Models, Registry)?
2. What is Weights & Biases (W&B)? How does it compare to MLflow?
3. What is DVC (Data Version Control)? How does it track large binary files? How does it integrate with Git?
4. What is a model registry? Why is it important in a production ML system?
5. What is an ML experiment? What should you always log? (hyperparameters, metrics, artifacts, code version, data version, environment)
6. What is reproducibility in ML? What are the sources of non-reproducibility? (random seeds, GPU non-determinism, library versions, data shuffling)

### Deployment

7. What is the difference between batch inference, online (real-time) inference, and streaming inference? Give use cases for each.
8. What is a REST API? What is gRPC? What are the tradeoffs for ML model serving?
9. What is Docker? What is the difference between an image and a container? Write a simple Dockerfile for a Python ML service.
10. What is Kubernetes (K8s)? What is a Pod, Deployment, Service, and Ingress?
11. What is a Helm chart? How does it simplify Kubernetes deployments?
12. What is model serving? Compare Triton Inference Server, TorchServe, BentoML, Seldon Core, and KServe.
13. What is TensorRT? What optimizations does it apply? When should you use it?
14. What is ONNX? What is the ONNX Runtime? How does ONNX improve model portability?
15. What is canary deployment? What is blue-green deployment? What is a shadow deployment?
16. What is model A/B testing in production? How do you route traffic and collect feedback?
17. What is an SLA (Service Level Agreement)? What is p99 latency? How do you achieve low-latency inference?

### Monitoring & CI/CD for ML

18. What is CI/CD for ML (MLOps)? How does it differ from standard software CI/CD?
19. What is a GitHub Actions workflow for ML? What are the key steps? (lint, test, train, evaluate, deploy)
20. What is infrastructure-as-code (IaC) for ML? Compare Terraform, Pulumi, and CDK.
21. What is data drift? How do you detect it in production? (PSI, KS test, ADWIN)
22. What is model performance degradation? How do you set up alerts?
23. What is a model card? What information should it contain? Who published the model card standard?
24. What is Prometheus + Grafana? What metrics would you monitor for an ML serving system?
25. What is distributed training? Compare Horovod, DeepSpeed, and PyTorch DDP/FSDP.
26. What is ZeRO optimization in DeepSpeed? Explain ZeRO-1, ZeRO-2, and ZeRO-3.
27. What is FSDP (Fully Sharded Data Parallel)? How does it differ from DDP?
28. What is a serving SLO (Service Level Objective)? Name 5 key metrics to track for LLM serving.
29. What is autoscaling? Explain horizontal pod autoscaling (HPA) vs. KEDA for ML workloads.
30. What are common failure modes in production ML systems? How do you build resilience?
31. What is a feature pipeline SLA? How do you handle late/missing features at inference time?
32. What is model explainability in production? Name 3 tools used for production explainability (SHAP, LIME, Captum).
33. What is the model deployment checklist? What must you verify before deploying a model to production?
34. What is a load test for ML inference? What tools do you use? (Locust, K6, wrk)
35. How would you design a zero-downtime model update strategy for a critical production system?

---

## 12. System Design for ML Systems

> Expected at Senior level. Tests architectural thinking.

1. Design a real-time recommendation system for an e-commerce platform. Handle 1M users, 10M products, sub-100ms latency.
2. Design a large-scale image classification pipeline that processes 1 billion images per day.
3. Design a fraud detection system with real-time (<50ms) scoring.
4. Design a search ranking system for a job portal. How do you personalize results?
5. Design a document question-answering system using RAG for a legal firm with 10M documents.
6. Design a multi-modal content moderation system for a social media platform.
7. Design a real-time anomaly detection system for IoT sensor data.
8. Design a model training infrastructure for fine-tuning LLMs with a team of 50 ML engineers.
9. Design a feature store for a ride-sharing company. Handle both online and offline features.
10. Design a model monitoring system that detects data drift and model degradation automatically.
11. What is the two-tower model for recommendations? Explain the architecture and training objective.
12. What is approximate nearest neighbor (ANN) search? Compare FAISS, ScaNN, and HNSW. How do you choose an index?
13. How would you reduce the latency of a Transformer model serving endpoint from 200ms to 20ms?
14. What is the serving stack for a production LLM application? (API gateway, load balancer, model server, cache, vector DB)
15. How would you design a distributed training system for a 70B parameter model?
16. What is a medallion architecture for an ML data lakehouse?
17. How do you handle cold start in recommendation systems?
18. What is multi-armed bandit vs. A/B testing for online model selection? When is each preferred?
19. How would you design a continuous training (CT) pipeline that retrains a model automatically when drift is detected?
20. What is the ML Platform stack? Name the components (feature store, model registry, experiment tracker, serving infrastructure, monitoring).
21. Design a speech recognition pipeline for real-time transcription of customer calls.
22. How would you build a scalable document embedding service that keeps embeddings fresh as documents are updated?
23. What is the trade-off between model complexity and inference cost in production? How do you make this decision?
24. Design a system for running hyperparameter search at scale. (Optuna, Ray Tune, Bayesian optimization)
25. What is the difference between synchronous and asynchronous ML inference? When would you use a queue-based async architecture?
26. How do you handle model versioning when different clients need different model versions simultaneously?
27. What is a semantic cache for LLM inference? How does it reduce cost and latency?
28. Design a personalized news feed ranking system with privacy constraints (GDPR, differential privacy).
29. How would you architect a multi-tenant ML platform for SaaS customers?
30. What is the difference between a data mesh and a data lake? Which approach scales better for large organizations?

---

## 13. Data Structures & Algorithms

> Expect LeetCode-style questions at FAANG-adjacent companies. Senior roles still test this.

### Arrays & Strings

1. What is the time and space complexity of sorting algorithms: Bubble, Selection, Insertion, Merge, Quick, Heap, Radix, Counting?
2. Implement binary search. What are the conditions for it to work correctly?
3. What is the two-pointer technique? Give 3 ML-relevant problems it solves.
4. What is a sliding window? Explain the fixed-size and variable-size variants. Give an example.
5. What is the difference between in-place and out-of-place algorithms?
6. Given an array of integers, find the maximum subarray sum (Kadane's algorithm). What is the time complexity?
7. How would you find all pairs in an array that sum to a target value in O(n) time?
8. Implement a function to check if a string is a valid palindrome, ignoring non-alphanumeric characters.

### Linked Lists, Stacks, Queues

9. What is the difference between a singly linked list, doubly linked list, and a circular linked list?
10. How do you detect a cycle in a linked list? (Floyd's cycle detection / tortoise and hare)
11. How do you reverse a linked list? What is the time and space complexity?
12. What is a stack? What is a queue? Implement a queue using two stacks.
13. What is a monotonic stack? Give an example problem it solves efficiently.
14. What is a priority queue? What data structure implements it? What are the time complexities of push and pop?

### Trees & Graphs

15. What is a BST? What are the time complexities for search, insert, and delete?
16. What is a balanced BST? Compare AVL trees and Red-Black trees. Which is faster for lookups? Which for insertions?
17. What is BFS vs. DFS? When would you prefer each? What is the space complexity of each?
18. What is topological sorting? What algorithms can compute it? When is it used in ML pipelines?
19. What is Dijkstra's algorithm? What is its time complexity with a priority queue? When does it fail?
20. What is A* search? How is the heuristic function chosen? What makes it optimal and complete?
21. What is the difference between a tree and a graph? What is a DAG?
22. What is dynamic programming? Explain the concept of memoization vs. tabulation.
23. Solve the coin change problem (minimum coins to make amount X). What is the DP solution?

### Hashing & Advanced

24. What is a hash table? What is the average and worst-case time complexity for lookup?
25. What is a hash collision? What are open addressing and separate chaining?
26. What is a trie (prefix tree)? What are its advantages over a hash map for string prefix queries?
27. What is a segment tree? What problems does it efficiently solve? (range sum, range min/max queries)
28. What is a Bloom filter? How does it work? What are the false positive/negative characteristics?
29. What is consistent hashing? Why is it used in distributed systems and ML serving?
30. What is the difference between O(n log n) and O(n²) in practical terms for ML data preprocessing at scale?
31. What is a Union-Find (Disjoint Set Union) data structure? What is path compression and union by rank?
32. What is the knapsack problem? How does it relate to feature selection in ML?
33. What is the time complexity of matrix multiplication? What is Strassen's algorithm?
34. Write a function to serialize and deserialize a binary tree.
35. How would you find the K most frequent elements in a stream of data efficiently?

---

## 14. Software Engineering Best Practices

> Senior Software Engineer role requires deep knowledge here.

### OOP & Design Patterns

1. What are the SOLID principles? Give an ML-relevant example for each.
2. What is the difference between composition and inheritance? When should you prefer composition?
3. What is the Factory pattern? Give an example in the context of ML model loading.
4. What is the Strategy pattern? How would you use it to make a training loop interchangeable with different loss functions?
5. What is the Observer pattern? How is it used in ML training callback systems (Keras, Lightning)?
6. What is the Singleton pattern? When is it appropriate? What are the drawbacks in multi-threaded environments?
7. What is the Adapter pattern? What is the Decorator pattern? Give ML pipeline examples.
8. What is the Repository pattern? How does it decouple data access from business logic in an ML service?
9. What is dependency injection? How does it improve testability of ML components?
10. What is the difference between a monolith and microservices architecture? When is each appropriate for an ML platform?

### Testing

11. What is unit testing vs. integration testing vs. end-to-end testing? Give examples for an ML system.
12. What is test-driven development (TDD)? How do you apply it to ML code?
13. What is mocking? When should you mock in ML tests? What are the risks of over-mocking?
14. What is property-based testing? What is Hypothesis (Python library)? Give an ML use case.
15. How do you test an ML model? What is the difference between testing code and testing model behavior?
16. What is a flaky test? How do you identify and fix them in ML pipelines?
17. What is code coverage? What is branch coverage? When is 100% coverage a bad goal?
18. What testing tools do you use for Python ML code? (pytest, unittest, hypothesis, deepchecks)

### Code Quality & Architecture

19. What is Clean Code? Name 5 principles from Robert C. Martin's Clean Code.
20. What is technical debt? How do you manage it in a fast-moving ML team?
21. What is a code review best practice? What do you look for when reviewing ML code specifically?
22. What is the difference between synchronous and asynchronous code? When is async preferred in ML APIs?
23. What is a REST API best practice? What are idempotent operations? What are HTTP status codes you commonly use?
24. What is GraphQL? When would you use it over REST for an ML data API?
25. What is semantic versioning (semver)? How do you version ML models differently from software?
26. What is documentation as code? What tools generate API docs from docstrings? (Sphinx, pdoc, mkdocs)
27. What is a linter vs. a formatter? Name Python tools for each and their role in ML codebases.
28. What is type hinting in Python? What is `mypy`? How does it improve ML code reliability?
29. What is the difference between a library, framework, and platform? Where does PyTorch fit?
30. How do you handle configuration management in ML projects? Compare YAML files, Hydra, Pydantic, and environment variables.
31. What is an API contract? How do you ensure backward compatibility in an ML model API?
32. What is event-driven architecture? How is it used in ML systems (e.g., triggering retraining on data events)?
33. What is a message queue? Compare RabbitMQ, SQS, and Kafka for ML pipeline orchestration.
34. What is a circuit breaker pattern? How does it improve resilience in ML serving systems?
35. How do you handle secrets (API keys, credentials) in an ML production system?

---

## 15. SQL & Databases

> Still tested at all levels. ML engineers query data daily.

### SQL Fundamentals

1. What is the difference between `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`? Give examples.
2. What is a subquery vs. a CTE (Common Table Expression)? When is a CTE preferred?
3. What are window functions? Explain `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`, `SUM() OVER()`.
4. What is the difference between `WHERE` and `HAVING`? When does each apply?
5. What is a GROUP BY? What columns can appear in SELECT when using GROUP BY?
6. What is `DISTINCT` vs. `GROUP BY`? When is each preferred?
7. What is a correlated subquery? What is an uncorrelated subquery? Which is more efficient and why?
8. What is the difference between `UNION` and `UNION ALL`?
9. What is a recursive CTE? Write one to find all paths in a hierarchy (e.g., employee-manager tree).
10. What is `COALESCE`? What is `NULLIF`? What is `CASE WHEN`?
11. Write a query to find the second highest salary in an employee table without using `LIMIT/OFFSET`.
12. Write a query to find duplicate rows in a table.
13. Write a query to compute a 7-day rolling average of daily active users.
14. Write a query to pivot rows to columns (crosstab).
15. Write a query to detect sessions from a raw event log (sessionization problem).

### Performance & Design

16. What is a database index? What is a B-tree index? What is a hash index?
17. When should you add an index and when should you not? What is the tradeoff?
18. What is an EXPLAIN/EXPLAIN ANALYZE plan? What do you look for in query optimization?
19. What is the N+1 query problem? How do you fix it?
20. What is normalization? What are 1NF, 2NF, 3NF, and BCNF? When do you deliberately denormalize?
21. What is a transaction? What are ACID properties (Atomicity, Consistency, Isolation, Durability)?
22. What are isolation levels? (Read Uncommitted, Read Committed, Repeatable Read, Serializable). What are dirty reads, phantom reads, and non-repeatable reads?
23. What is an ORM? Name 2 Python ORMs. What are the tradeoffs vs. raw SQL?
24. What is the difference between a relational database and a NoSQL database? Give ML use cases for each.
25. What is a columnar database (e.g., ClickHouse, BigQuery, Redshift)? Why is it faster for analytical queries?
26. What is partitioning vs. sharding? When does each apply?
27. What is a materialized view? How does it differ from a regular view?
28. What is a deadlock? How do databases detect and resolve them?
29. What is PostgreSQL's `JSONB` type? When would you use it in an ML feature store?
30. How would you design a database schema for storing ML experiment results (runs, metrics, artifacts, parameters)?
31. What is the difference between optimistic and pessimistic locking?
32. What is connection pooling? Why is it important for ML microservices?
33. What is a time-series database? Give examples (InfluxDB, TimescaleDB, QuestDB). When is it preferred?
34. How would you design a vector search schema in PostgreSQL using `pgvector`?
35. What is database replication? What is the difference between synchronous and asynchronous replication?

---

## 16. Cloud & Infrastructure (AWS / GCP / Azure)

> Required for Senior ML Engineer and AI Engineer in European tech companies.

### General Cloud

1. What is the difference between IaaS, PaaS, and SaaS? Give ML-specific examples of each.
2. What is the difference between vertical scaling and horizontal scaling? When is each preferred for ML?
3. What is a VPC (Virtual Private Cloud)? What are subnets, security groups, and NACLs?
4. What is IAM (Identity and Access Management)? What is the principle of least privilege?
5. What is object storage (S3, GCS, Azure Blob)? How does it differ from a file system? What are its consistency guarantees?
6. What are spot/preemptible instances? How do you make ML training jobs fault-tolerant on them?
7. What is a managed Kubernetes service (EKS, GKE, AKS)? What is the control plane vs. data plane?
8. What is serverless computing (AWS Lambda, GCP Cloud Functions)? When is it useful for ML? When is it not?
9. What is CDN (Content Delivery Network)? When would an ML application need one?
10. What is Infrastructure as Code (IaC)? Compare Terraform, AWS CDK, and Pulumi.

### ML-Specific Cloud Services

11. What is AWS SageMaker? What components does it provide? (Training, Hyperparameter Tuning, Endpoints, Pipelines, Feature Store)
12. What is Google Vertex AI? How does it compare to SageMaker?
13. What is Azure ML? What is the workspace concept?
14. What is a managed notebook environment in the cloud (SageMaker Studio, Vertex AI Workbench)?
15. What is AWS Batch vs. AWS Lambda vs. SageMaker Training Job for running ML workloads?
16. What is a GPU instance type for ML? Compare A100, H100, V100, T4 in terms of memory and use cases.
17. What is AWS EFS vs. FSx for Lustre? When do you use each for ML training?
18. What is NVIDIA NCCL? How is it used in distributed GPU training?
19. What is AWS ECR (Elastic Container Registry)? How is it used in ML deployment?
20. What is Kubeflow? What is MLflow on Kubernetes? What are the components of a full ML platform on Kubernetes?
21. What is Argo Workflows / Argo CD? How is it used for ML pipeline orchestration and GitOps?
22. What is Apache Ray? What is Ray Tune, Ray Train, Ray Serve, and Ray Data?
23. What is the difference between a warm pool and cold start in Lambda/serverless inference?
24. How do you estimate and optimize cloud costs for ML training and inference?
25. What is a data egress cost? Why is it important in multi-cloud ML architectures?
26. What is Terraform remote state? Why is it critical for team environments?
27. What is AWS Step Functions vs. Airflow vs. Prefect for ML pipeline orchestration?
28. What is the difference between model serving on GPU and CPU? What is the cost tradeoff?
29. How do you implement multi-region ML serving for low-latency global inference?
30. What is DataDog / CloudWatch / Prometheus for ML monitoring? What is the key difference in their data model?
31. What is a secrets manager (AWS Secrets Manager, HashiCorp Vault)? How do you use it in ML pipelines?
32. What is GitOps? How does it differ from traditional CI/CD? What tools implement it (Flux, Argo CD)?
33. What is a service mesh (Istio, Linkerd)? When would you add one to an ML platform?
34. What is FinOps for ML? What strategies reduce costs while maintaining performance?
35. How would you architect a fully serverless ML inference pipeline for a startup with unpredictable traffic?

---

## 17. AI Ethics, Fairness, Bias & Safety

> Critical for European roles (GDPR, EU AI Act). Always asked at senior level.

1. What is algorithmic bias? What are the different sources of bias in ML systems (data bias, label bias, aggregation bias, evaluation bias)?
2. What is demographic parity? What is equalized odds? What is individual fairness? Can you achieve all simultaneously?
3. What is the EU AI Act? What are the risk categories? What does it mean for an ML engineer in Germany/Netherlands?
4. What is GDPR? What are the key rights it gives individuals (access, erasure, portability, explanation)?
5. What is "right to explanation" under GDPR? How does it affect black-box ML models?
6. What is the difference between explainability and interpretability? Give examples of each type of ML model.
7. What is SHAP (SHapley Additive exPlanations)? What is the mathematical foundation (Shapley values from game theory)?
8. What is LIME (Local Interpretable Model-Agnostic Explanations)? How does it work?
9. What is a model card? What is a datasheet for datasets? Who standardized them (Google)?
10. What is differential privacy? What is the ε-differential privacy guarantee? What is the privacy-accuracy tradeoff?
11. What is federated learning? What privacy benefits does it offer? What are its practical challenges?
12. What is membership inference attack? How do you defend against it?
13. What is model inversion attack? What is training data extraction? How are these risks mitigated?
14. What is adversarial robustness? What are adversarial examples? What is FGSM (Fast Gradient Sign Method)?
15. What is red-teaming for AI systems? How is it different from standard software penetration testing?
16. What is AI safety? What is alignment? What is the difference between narrow safety and AGI safety?
17. What is Constitutional AI? How does Anthropic use it to make Claude safer?
18. What is the difference between safety-tuning and censorship? Where is the line?
19. What is model watermarking? How is it used to detect synthetic content?
20. What is the NIST AI Risk Management Framework?
21. How do you audit a model for discriminatory outcomes? What is an audit trail?
22. What is counterfactual explanation? How does it help individuals understand why they got a negative decision?
23. What is the fairness-accuracy tradeoff? Is it real? How do you navigate it with stakeholders?
24. What are deepfakes? What is synthetic media detection? What tools/models are used?
25. What is AI governance? What are the roles and responsibilities of an AI engineer in an organization with an AI governance framework?
26. What is the precautionary principle applied to AI? How does it differ from "move fast and break things"?
27. What is environmental cost of AI? What is the carbon footprint of training a large model?
28. What is the reproducibility crisis in AI research? How does it affect ML engineering practice?
29. What is data provenance? Why is it critical for responsible AI?
30. How do you handle a discovered model bias post-deployment? What is the escalation process?
31. What is the difference between privacy by design and privacy by compliance?
32. What is synthetic data generation for privacy preservation? What are the risks?
33. What is the AI transparency obligation in the EU AI Act for high-risk systems?
34. What is human-in-the-loop (HITL)? When is it legally required vs. just good practice?
35. How would you explain a rejected loan decision made by an ML model to a customer, in compliance with EU regulations?

---

## 18. Behavioral & Leadership Questions

> Critical for Senior roles. Use STAR format: **S**ituation → **T**ask → **A**ction → **R**esult.

### Technical Leadership & Decision Making

1. Tell me about a time you had to make a technical decision with incomplete information. How did you proceed?
2. Describe a time you disagreed with a team member about a technical approach. How was it resolved?
3. Tell me about the most complex ML system you've built. What were the key design decisions and their tradeoffs?
4. Describe a time when a model you deployed underperformed in production. How did you detect it and what did you do?
5. Tell me about a time you had to balance technical quality with a tight deadline. What did you prioritize?
6. Describe a situation where you had to convince non-technical stakeholders to invest in ML infrastructure. How did you make the case?
7. Tell me about a time you mentored a junior engineer. What was your approach and what did they learn?
8. Describe a time you identified and addressed technical debt in an ML system. What was the impact?
9. Tell me about a time you had to learn a completely new technology or domain quickly for a project. How did you approach it?
10. Describe a time you had to shut down or deprecate an ML model. How did you manage the transition?

### Problem Solving & Impact

11. What is the most impactful ML project you've worked on? How did you measure its impact?
12. Describe a time you had to debug a particularly difficult ML bug. Walk me through your debugging process.
13. Tell me about a failed ML project. What went wrong and what did you learn?
14. How do you prioritize which ML improvements to work on? Walk me through your framework.
15. Describe a time you improved the performance (latency, throughput, or accuracy) of an ML system significantly.
16. Tell me about a time you had to work with imperfect, noisy, or incomplete data. How did you handle it?
17. Describe a time you implemented something that significantly reduced cloud/compute costs.
18. Tell me about a project where you collaborated closely with product managers and designers. How did you translate ML capabilities into product requirements?

### Collaboration & Communication

19. How do you explain a complex ML concept to a non-technical stakeholder?
20. Describe a time you received critical feedback. How did you respond?
21. How do you approach code reviews? What do you look for, and how do you give constructive feedback?
22. Tell me about a time you worked in a cross-functional team (with product, design, data engineering). What was your role?
23. How do you stay current with the rapidly evolving ML/AI field? Name the last 3 papers you read.
24. Describe your approach to documentation. How do you ensure your ML code and decisions are well-documented?
25. Tell me about a time you had to deliver bad news to a manager or stakeholder about a project. How did you handle it?

### Culture & Values (European Context)

26. Why do you want to work in Munich/Amsterdam/Berlin/Frankfurt? What attracts you to the European tech ecosystem?
27. How do you approach work-life balance? How do you prevent burnout on intensive ML projects?
28. How do you handle working in a multicultural, multilingual team?
29. What is your approach to remote vs. on-site work? How do you maintain collaboration quality in a hybrid environment?
30. Why are you interested in this specific role / company? (Research the company beforehand — always required)
31. Where do you see yourself in 3-5 years? How does this role fit your career trajectory?
32. What is your greatest professional strength? What is an area you are actively working to improve?
33. Tell me about a time you had to navigate ambiguous requirements. How did you clarify them and move forward?
34. How do you handle competing priorities when multiple projects demand your attention simultaneously?
35. What kind of engineering culture do you thrive in? What does your ideal team look like?

---

## 19. German / European Tech Market Specifics

> Unique considerations for landing a job in Germany / Netherlands.

### Work & Visa

1. What is a Blue Card (Blaue Karte EU)? What are the salary thresholds for Germany and the Netherlands? (Germany 2024: ~€43,800 for shortage occupations, ~€58,400 general; Netherlands: ~€60,000 for knowledge migrants <30, ~€45,000 for 30+)
2. What is the process for a Fachkräftezuwanderungsgesetz (Skilled Immigration Act) visa for non-EU engineers?
3. What is anerkannte Berufsqualifikation (recognized professional qualification) and does a Computer Science degree typically need recognition in Germany?
4. What is a Niederlassungserlaubnis (permanent residence) and after how many years can you apply?
5. What is the Arbeitnehmerfreizügigkeit (freedom of movement for workers) in the EU? How does it simplify moving between Germany and the Netherlands?

### Company Culture

6. What is the German engineering culture? How is it different from Silicon Valley culture (e.g., thoroughness, risk aversion, process)?
7. What is a Betriebsrat (works council)? How can it affect ML hiring, data usage policies, and product decisions?
8. What is Tarifvertrag (collective bargaining agreement) and how does it affect salaries in some German tech companies?
9. How are salaries structured in Germany vs. Netherlands? What is the difference between Brutto (gross) and Netto (net) salary?
10. What is the notice period (Kündigungsfrist) standard for senior engineers in Germany? (typically 1-3 months)

### GDPR & Regulations for ML Engineers

11. What are the six lawful bases for processing personal data under GDPR? Which is most commonly used for ML training data?
12. What is a Data Processing Agreement (DPA)? When is it required between an ML SaaS provider and a customer?
13. What is a Data Protection Officer (DPO)? When must a company appoint one?
14. What is Privacy Impact Assessment (PIA/DPIA)? When is it required for ML systems?
15. What does GDPR say about automated decision-making and profiling (Article 22)?
16. How does the EU AI Act categorize AI systems? What are the obligations for high-risk AI systems that a German ML engineer must comply with?
17. What is NIS2 (Network and Information Security Directive 2)? How does it affect AI companies in the EU?
18. What is the German BDSG (Bundesdatenschutzgesetz)? How does it extend GDPR for Germany?
19. What is the Digital Markets Act (DMA) and how might it affect AI products built on top of large platforms?
20. How do you handle cross-border data transfer from the EU to the US (e.g., using US-based cloud services)? What is a Standard Contractual Clause (SCC)?

### Language & Integration

21. Is German required for senior ML roles in Munich, Frankfurt, and Berlin? (Generally: Multinationals often English-only. Mittelstand companies often require German. Research the specific company.)
22. What is the difference between working in a German Mittelstand company vs. a startup vs. a large corporation? What are the ML team structures like?
23. What Dutch language requirements exist for Amsterdam ML roles? (Many Dutch companies operate in English, but knowing Dutch is a strong advantage outside of multinationals)
24. What are the leading AI research hubs in Germany? (Munich: TU Munich, LMU, Fraunhofer; Berlin: DFKI, HPI; Frankfurt: AIIC; Heidelberg: MPI)
25. What are major German AI companies and research labs you should know? (Aleph Alpha, DeepL, Celonis, Personio, TU Munich Chair for AI, DFKI, Fraunhofer IAIS, Bosch AI, BMW AI, SAP AI Research, Siemens AI Lab)
26. What are major Amsterdam/Netherlands AI companies? (Booking.com, Adyen, ASML, Philips AI, TomTom, Elastic, Takeaway.com, Bol.com)
27. What German tech job portals are popular for ML/AI roles? (LinkedIn, StepStone, XING, Glassdoor, Indeed.de, Honeypot, Relocate.me)
28. What is the typical ML interview process at a German tech company vs. a US-origin company with German offices?
29. What is Kurzarbeit (short-time work scheme)? How does it affect job security perceptions in Germany?
30. What questions are illegal to ask in a German job interview (according to AGG - Allgemeines Gleichbehandlungsgesetz)?

---

## Quick Reference: Recommended Study Resources

### Books
- *Deep Learning* — Goodfellow, Bengio, Courville (free online)
- *Pattern Recognition and Machine Learning* — Bishop
- *Hands-On Machine Learning* — Aurélien Géron (Scikit-Learn, Keras, TF)
- *Designing Machine Learning Systems* — Chip Huyen
- *The ML Engineer* — Andriy Burkov
- *Clean Code* — Robert C. Martin
- *Designing Data-Intensive Applications* — Martin Kleppmann

### Online Courses
- Stanford CS229 (ML), CS231N (CV), CS224N (NLP) — free lecture notes/videos
- fast.ai Practical Deep Learning for Coders
- DeepLearning.AI Specializations (Coursera)
- Hugging Face NLP Course (free)
- Full Stack Deep Learning (free)

### Papers to Know
- *Attention Is All You Need* (Transformers, 2017)
- *BERT* (Devlin et al., 2018)
- *GPT-3* (Brown et al., 2020)
- *LoRA* (Hu et al., 2021)
- *Retrieval-Augmented Generation for NLP* (Lewis et al., 2020)
- *InstructGPT / RLHF* (Ouyang et al., 2022)
- *DPO* (Rafailov et al., 2023)
- *Flash Attention* (Dao et al., 2022)
- *ResNet* (He et al., 2015)
- *YOLO* (Redmon et al., 2015)
- *ViT* (Dosovitskiy et al., 2020)
- *CLIP* (Radford et al., 2021)
- *Stable Diffusion / LDM* (Rombach et al., 2022)
- *DeepSeek-R1* (2025)

### Practice Platforms
- LeetCode (DSA — aim for 150 medium/hard)
- Kaggle (competition ML)
- HuggingFace (LLM ecosystem practice)
- MLflow + W&B (local experiment tracking)
- Papers With Code (SOTA benchmarks)

### Mock Interview
- Pramp (free peer mock interviews)
- InterviewBit
- AlgoExpert / SystemDesignPrimer (GitHub)
- ML-Interviews Book by Chip Huyen (free online)

---

## Study Plan — Ashikur's Profile-Specific Order (12-Week)

> This is reordered for your actual background. Strengths first (to sharpen, not ignore), gaps second.

| Week | Focus | Priority | Notes |
|------|-------|----------|-------|
| 1 | **VLM Section (5a)** — all 45 questions | Critical | Your publications are your #1 differentiator. Prepare 2-min + 5-min answers for each paper. |
| 2 | **Computer Vision Section (6)** — all 35 questions | Critical | You have 6+ years of CV production experience. Lock down the theory behind what you've done. |
| 3 | **Generative AI + LLMs Section (5)** — focus on diffusion, LoRA, RAG, agents | Critical | Retouched, Omnimage, CogniX, Fitting Room all draw from this. |
| 4 | **Deep Learning & Neural Networks (4)** | High | Foundation for VLM, CV, and GenAI. Focus on Transformers, ViT, U-Net, attention. |
| 5 | **Behavioral + Resume Talking Points (Section 0 + 18)** | High | Write full STAR answers for every project in Section 0. Practice speaking them aloud. |
| 6 | **MLOps + System Design (11 + 12)** | High | Your FastAPI/Docker/GCP/Redis production stack. Walk through Retouched.ai and Fitting Room architectures. |
| 7 | **Python Programming (1)** + DSA warm-up | Medium-High | Code fluency. Focus on generators, decorators, NumPy vectorization, async. Start LeetCode. |
| 8 | **DSA (13)** — 2 medium LeetCode per day | Medium | Array/string/tree/graph/DP/hash. Aim for 60–80 mediums total. |
| 9 | **ML Fundamentals (3) + Math (2)** | Medium | Brush up theory behind things you use. Probability, bias-variance, regularization. |
| 10 | **Software Engineering (14) + SQL (15)** | Medium | SOLID, testing, design patterns. SQL window functions. pgvector for your vector DB work. |
| 11 | **AI Ethics + EU AI Act + GDPR (17 + 19)** | Medium | Required for EU market. Your hallucination research connects directly to AI safety topics. |
| 12 | **Mock interviews + Cloud (16) + RL-RLHF only (8)** | Polish | Full mock interviews. Cloud = GCP focus (your stack). RL = only RLHF/DPO/GRPO subset. |

---

## Your Specific Tech Stack Reference (from Resume)

> When asked "what tools/frameworks do you use?" — answer from this list only.

| Category | Your Stack |
|----------|-----------|
| Core ML | PyTorch, Diffusers (HuggingFace), Transformers, PEFT (LoRA/QLoRA) |
| Vision | OpenCV, U²-Net-architecture, COLMAP, Open3D, NeRF, 3D Gaussian Splatting |
| LLMs | Llama 2, Qwen, SeamlessM4T |
| Generative | Stable Diffusion variants, ComfyUI, LoRA fine-tuning |
| Experiment Tracking | Weights & Biases (W&B) |
| Backend | FastAPI, Nginx |
| Infra | Docker, Redis, CI/CD (GitHub Actions inferred from deploy.yml) |
| Cloud | GCP, Google Cloud Storage, AWS S3, DynamoDB |
| Database | SQL Server, (Redis for cache) |
| Evaluation | Offline evaluation pipelines, production A/B testing |

> **Do NOT claim:** TensorFlow, Kubernetes (K8s), Spark, Kafka, MLflow, SageMaker, Terraform, Airflow — unless you've actually used them outside what's on your resume.

---

*Good luck — your combination of production scale (4.5M+ images), published VLM research, and engineering leadership is a genuinely strong profile for Munich/Amsterdam/Berlin AI roles.*
