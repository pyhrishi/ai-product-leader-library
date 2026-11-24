# The Complete AI Product Leader Curriculum

A from-scratch master map of everything a world-class AI product leader can know. No time limit. Built to be navigated, not read straight through: jump to any Part, Module, numbered Topic, or micro-topic.

## How to use this document

- **Navigation:** open the outline and jump by heading. Numbering runs Part N, then Module N.M, then Topic N.M.K. Micro-topics sit after the colon on each topic line.
- **Every module has** a depth target (which level to aim for), a prove-it exercise (how you know you learned it), and learn-from sources.
- **It is not linear.** Use an entry path below, then follow curiosity and gaps.
- **Parts 1 to 3** are the science. **Parts 4 to 6** are the engineering. **Parts 7 to 9** are the product craft. **Parts 10 to 13** are the world around the product: safety, law, industry, leadership, the future. **Parts 14 to 17** are tools, projects, a reading library and conversation drills.

### Entry paths

- **Path A, Fluency first:** Part 3 (3.1 to 3.4) then Part 4 then Part 8 then Part 11. Gets you conversant and building quickly.
- **Path B, Builder:** Part 1.8, Part 4, Part 5, Part 15 projects, then back to the science.
- **Path C, Strategy and leadership:** Part 7, Part 8, Part 11, Part 12, Part 13, with Part 4 for credibility.
- **Path D, Research-grade depth:** Parts 1 to 3 in order, then the paper list in Part 16.

### Mastery levels

- **L1 Aware:** you recognise the term.
- **L2 Conversant:** you can explain it simply to a non-technical executive.
- **L3 Decision-capable:** you can make and defend a trade-off call in front of engineers.
- **L4 Authoritative:** you can teach it, critique others' work, and publish on it.
- **L5 Frontier:** you produce original insight others cite.

The top 0.1% pattern: L3 across almost everything, L4 in a handful of areas, L5 in one or two. Pick your L4 and L5 areas on purpose.

### The learning method that applies to every topic

1. **Primary source first:** read the paper, the docs, or the spec, not only a summary.
2. **Explain it three ways:** to a child, to a CEO, to an engineer. Write each version.
3. **Build or break something** that uses it.
4. **Spaced repetition:** turn every hard idea into 3 to 5 questions and review them on a schedule (Anki or similar).
5. **Keep a notes system** (Obsidian, Notion or plain Markdown) with one note per concept, linked to others.
6. **Keep an error log:** every time you were wrong about something, write down why.
7. **Teach or publish** monthly. Teaching exposes the holes.
8. **Weekly review:** what did I learn, what is shaky, what next.

### Master map

| Part | Name |
| --- | --- |
| 1 | Mathematical and computational foundations |
| 2 | Machine learning foundations |
| 3 | Modern AI science: LLMs, multimodal, reasoning, alignment |
| 4 | Applied AI engineering |
| 5 | Software, systems and infrastructure |
| 6 | Data, analytics and experimentation |
| 7 | Product management craft |
| 8 | AI product craft |
| 9 | Domains and verticals |
| 10 | Safety, security, ethics, law and governance |
| 11 | The AI industry and world |
| 12 | Leadership, communication and career |
| 13 | Frontier and futures |
| 14 | Tools mastery map |
| 15 | Project ladder |
| 16 | Reading and watching library |
| 17 | Mastery drills and question banks |

---

## Part 1: Mathematical and computational foundations

Why it matters: you do not need to derive everything, but you need enough to read papers, follow engineers, and notice when a claim cannot be true.

### Module 1.1 Linear algebra

*Depth target: L3. Prove-it: implement a small neural layer with matrix operations and explain every shape.*

- **1.1.1 Vectors and spaces:** vectors as lists vs arrows, vector spaces, span, basis, linear independence, dimension, subspaces
- **1.1.2 Matrices as transformations:** rotation, scaling, shear, composition as matrix multiplication, why order matters
- **1.1.3 Products:** dot product as similarity, cross product, outer product, matrix-vector and matrix-matrix products, batched products
- **1.1.4 Solving systems:** Gaussian elimination, rank, null space, determinants, inverses, pseudo-inverse, conditioning
- **1.1.5 Eigenvalues and eigenvectors:** meaning, diagonalisation, spectral theorem, power iteration
- **1.1.6 SVD and PCA:** singular values, low-rank approximation, truncated SVD, PCA as variance maximisation, why low-rank ideas power LoRA
- **1.1.7 Norms and distances:** L1, L2, L-infinity, cosine similarity, Euclidean vs cosine for embeddings, orthogonality, projections
- **1.1.8 Tensors:** rank, shape, broadcasting, einsum notation, reshaping, batching, memory layout
- **1.1.9 Sparse and structured matrices:** sparse formats, banded, block, why attention is a dense matrix and what sparse attention changes

*Learn from:* 3Blue1Brown Essence of Linear Algebra, Gilbert Strang MIT 18.06, Mathematics for Machine Learning (Deisenroth, Faisal, Ong), NumPy and PyTorch tensor docs.

### Module 1.2 Calculus

*Depth target: L3. Prove-it: derive backpropagation for a two-layer network by hand.*

- **1.2.1 Single variable:** limits, derivatives, rules, optimisation with derivatives, Taylor series
- **1.2.2 Multivariable:** partial derivatives, gradients, directional derivatives, level sets, Jacobian, Hessian
- **1.2.3 Chain rule:** the engine of backpropagation, computational graphs, forward and reverse mode
- **1.2.4 Automatic differentiation:** how PyTorch builds the graph, gradient accumulation, detach, no\_grad
- **1.2.5 Integrals:** area, expectation as integral, intuition for probability densities
- **1.2.6 Numerical issues:** vanishing and exploding gradients, numerical stability, log-sum-exp, floating point (FP32, BF16, FP16, FP8) and why precision matters for training and inference

*Learn from:* 3Blue1Brown Essence of Calculus, Karpathy micrograd video, Calculus lectures from MIT OCW.

### Module 1.3 Probability

*Depth target: L3. Prove-it: explain why softmax outputs are a categorical distribution and what temperature does to it.*

- **1.3.1 Foundations:** sample spaces, axioms, conditional probability, independence, Bayes' theorem, base-rate neglect
- **1.3.2 Random variables:** discrete and continuous, PMF, PDF, CDF, expectation, variance, covariance, correlation
- **1.3.3 Key distributions:** Bernoulli, binomial, categorical, multinomial, Poisson, uniform, Gaussian, exponential, Beta, Dirichlet, heavy-tailed distributions, power laws
- **1.3.4 Joint, marginal, conditional:** chain rule of probability (how language models factorise text), marginalisation
- **1.3.5 Limit theorems:** law of large numbers, central limit theorem, why averages behave and when they do not
- **1.3.6 Estimation:** maximum likelihood, MAP, Bayesian inference, priors and posteriors, conjugacy
- **1.3.7 Sampling:** inverse transform, rejection, importance sampling, MCMC at a conceptual level, top-k, top-p and temperature sampling in LLMs
- **1.3.8 Stochastic processes:** Markov chains, hidden Markov models, random walks, Gaussian processes (conceptual)

*Learn from:* Blitzstein Stat 110 (Harvard, free), Probabilistic Machine Learning (Kevin Murphy), Think Bayes.

### Module 1.4 Statistics and causal thinking

*Depth target: L3 to L4. This is the module that separates product people who can read experiments from those who cannot.*

- **1.4.1 Descriptive statistics:** mean, median, quantiles, variance, skew, outliers, distributions of real product metrics
- **1.4.2 Inference:** sampling distributions, confidence intervals, hypothesis testing, p-values and their misuse, effect sizes, statistical power, sample size calculation
- **1.4.3 Common traps:** multiple comparisons, peeking, Simpson's paradox, survivorship bias, selection bias, regression to the mean, base rates
- **1.4.4 Resampling:** bootstrap, permutation tests, cross-validation
- **1.4.5 Regression:** linear, logistic, interpretation of coefficients, multicollinearity, regularisation, generalised linear models
- **1.4.6 Bayesian methods:** Bayesian A/B testing, credible intervals, hierarchical models, priors for small data
- **1.4.7 Causal inference:** correlation vs causation, confounders, DAGs, randomised experiments, difference-in-differences, instrumental variables, regression discontinuity, propensity scores, uplift modelling
- **1.4.8 Time series basics:** trend, seasonality, autocorrelation, forecasting error measures, change point detection

*Learn from:* Statistical Rethinking (McElreath), Trustworthy Online Controlled Experiments (Kohavi, Tang, Xu), The Book of Why (Pearl), Causal Inference: The Mixtape.

### Module 1.5 Information theory

*Depth target: L3. Prove-it: explain why minimising cross-entropy is the same as maximising likelihood, and what perplexity means.*

- **1.5.1 Entropy:** information content, entropy, joint and conditional entropy
- **1.5.2 Cross-entropy and KL divergence:** training loss for classification and language models, asymmetry of KL, use in RLHF and distillation
- **1.5.3 Mutual information:** dependence, feature selection, representation learning objectives
- **1.5.4 Compression and prediction:** why good prediction equals good compression, bits per byte, perplexity, the link to scaling
- **1.5.5 Channel capacity and coding:** noisy channels, error correction, relevance to quantisation and robustness (conceptual)

### Module 1.6 Optimisation

*Depth target: L3. Prove-it: train the same model with SGD, momentum and Adam and explain the differences.*

- **1.6.1 Convexity:** convex sets and functions, why non-convex deep learning still works
- **1.6.2 Gradient descent family:** batch, mini-batch, SGD, momentum, Nesterov, RMSProp, Adam, AdamW, Lion, Muon
- **1.6.3 Learning rate:** schedules, warmup, cosine decay, learning-rate finders, batch size interactions, critical batch size
- **1.6.4 Regularisation:** weight decay, dropout, early stopping, data augmentation, label smoothing
- **1.6.5 Loss landscapes:** saddle points, sharp vs flat minima, loss spikes, double descent, grokking
- **1.6.6 Constrained and discrete optimisation:** Lagrange multipliers, linear programming, integer programming, combinatorial optimisation in logistics and ranking
- **1.6.7 Distributed optimisation:** data parallel, gradient synchronisation, large-batch training, communication costs

### Module 1.7 Computer science foundations

*Depth target: L3. Prove-it: explain what happens from typing a URL to seeing a page, and where an AI call fits in.*

- **1.7.1 Data structures:** arrays, linked lists, hash maps, sets, trees, heaps, tries, graphs, bloom filters, skip lists
- **1.7.2 Algorithms:** sorting, searching, recursion, divide and conquer, dynamic programming (conceptual), graph traversal, shortest paths, approximate nearest neighbour search
- **1.7.3 Complexity:** Big-O, time vs space, amortised analysis, why O(n squared) attention matters
- **1.7.4 Computer architecture:** CPU, registers, cache hierarchy, RAM, disk, GPU architecture (cores, memory bandwidth, tensor cores), why memory bandwidth bounds LLM inference
- **1.7.5 Operating systems:** processes, threads, scheduling, virtual memory, file systems, containers, system calls
- **1.7.6 Concurrency:** race conditions, locks, async I/O, event loops, queues, back-pressure
- **1.7.7 Networking:** TCP/IP, UDP, DNS, HTTP/1.1, HTTP/2, HTTP/3, TLS, WebSockets, server-sent events (how streaming responses work), CDNs, load balancers
- **1.7.8 Databases:** relational model, indexes, transactions, ACID, isolation levels, NoSQL families, vector indexes
- **1.7.9 Distributed systems:** latency, partitions, CAP, consistency models, replication, consensus (Raft, Paxos conceptually), idempotency, retries, exactly-once myths
- **1.7.10 Compilers and runtimes:** interpreters vs compilers, JIT, how Python executes, what CUDA kernels are

*Learn from:* CS50, Designing Data-Intensive Applications (Kleppmann), Computer Systems: A Programmer's Perspective, MIT 6.824 distributed systems lectures.

### Module 1.8 Programming craft

*Depth target: L3 reading and directing, L2 to L3 writing. Prove-it: ship a small working service end to end with an AI coding assistant and be able to explain every file.*

- **1.8.1 Python:** syntax, data types, functions, classes, generators, decorators, typing, async/await, virtual environments, packaging, testing with pytest
- **1.8.2 Scientific stack:** NumPy, Pandas, Polars, Matplotlib, Jupyter, vectorisation vs loops
- **1.8.3 PyTorch:** tensors, autograd, modules, optimisers, data loaders, training loop, GPU usage, checkpointing
- **1.8.4 SQL:** SELECT, JOINs, GROUP BY, window functions, CTEs, indexes, query plans, analytics patterns
- **1.8.5 TypeScript and JavaScript:** basics, async, modules, React concepts, Node.js, why most AI product front ends are written in them
- **1.8.6 Command line and Linux:** shell, pipes, grep, sed, awk, SSH, permissions, cron, environment variables
- **1.8.7 Git and collaboration:** branches, rebase vs merge, pull requests, code review, conventional commits, monorepos
- **1.8.8 Docker and deployment basics:** images, containers, compose, registries, environment configuration
- **1.8.9 Building APIs:** REST design, FastAPI or Express, validation, authentication hooks, OpenAPI specs
- **1.8.10 Working with AI coding tools:** specification-first prompting, project instruction files, plan then implement, test-driven prompts, reviewing diffs, knowing when the model is confidently wrong, security review of generated code
- **1.8.11 Debugging and reading code:** reading stack traces, logging, breakpoints, bisecting, reproducing, reading unfamiliar repositories quickly

---

## Part 2: Machine learning foundations

### Module 2.1 Core ML concepts

*Depth target: L3. Prove-it: take a messy dataset, build a baseline, and write an error analysis that changes what you do next.*

- **2.1.1 Problem types:** supervised, unsupervised, self-supervised, semi-supervised, reinforcement, ranking, retrieval, generation
- **2.1.2 Generalisation:** bias-variance trade-off, overfitting, underfitting, capacity, regularisation, learning curves
- **2.1.3 Data splits:** train, validation, test, cross-validation, time-based splits, group splits, leakage and how to find it
- **2.1.4 Metrics for classification:** accuracy, precision, recall, F1, ROC-AUC, PR-AUC, calibration, log loss, thresholds and costs
- **2.1.5 Metrics for regression, ranking and retrieval:** MAE, RMSE, MAPE, NDCG, MAP, MRR, recall at k, hit rate
- **2.1.6 Metrics for generation:** BLEU, ROUGE, BERTScore and their limits, perplexity, human preference, LLM judges (see Part 4)
- **2.1.7 Baselines and error analysis:** simple baselines first, confusion matrices, slicing by cohort, finding systematic errors
- **2.1.8 Imbalanced data:** resampling, class weights, threshold moving, cost-sensitive learning
- **2.1.9 Data-centric AI:** label quality, noisy labels, active learning, data cleaning, dataset documentation

*Learn from:* Andrew Ng Machine Learning Specialization, Stanford CS229, Hands-On Machine Learning (Aurelien Geron), An Introduction to Statistical Learning.

### Module 2.2 Classical models

*Depth target: L3 on tabular and ranking, L2 elsewhere. Classical models still win many real business problems.*

- **2.2.1 Linear and logistic regression:** assumptions, regularisation (Ridge, Lasso, Elastic Net), interpretation
- **2.2.2 Tree models:** decision trees, random forests, gradient boosting (XGBoost, LightGBM, CatBoost), feature importance, SHAP
- **2.2.3 Instance and kernel methods:** k-nearest neighbours, SVMs, kernels
- **2.2.4 Probabilistic models:** naive Bayes, Gaussian mixtures, hidden Markov models, Bayesian networks
- **2.2.5 Clustering:** k-means, hierarchical, DBSCAN, evaluation without labels
- **2.2.6 Dimensionality reduction:** PCA, t-SNE, UMAP, autoencoders
- **2.2.7 Anomaly and fraud detection:** isolation forest, one-class models, graph-based detection, supervised vs unsupervised trade-offs, feedback delay in labels
- **2.2.8 Recommenders:** collaborative filtering, matrix factorisation, two-tower retrieval, learning to rank, cold start, bandits, exploration vs exploitation, evaluation offline vs online
- **2.2.9 Time series forecasting:** ARIMA, exponential smoothing, Prophet, gradient boosting for forecasting, deep forecasting models
- **2.2.10 Survival and churn modelling:** hazard models, censoring, uplift modelling
- **2.2.11 When classical beats deep learning:** small data, tabular data, latency limits, interpretability requirements

### Module 2.3 Features and data pipelines

- **2.3.1 Feature engineering:** encoding categoricals, scaling, interactions, text and time features, target leakage
- **2.3.2 Missing data and outliers:** imputation strategies, missingness as signal
- **2.3.3 Labelling:** annotation guidelines, inter-annotator agreement, weak supervision, programmatic labelling, crowd vs expert labelling, cost per label
- **2.3.4 Data quality:** schemas, validation, drift, lineage, documentation (datasheets, data cards)
- **2.3.5 Synthetic data:** when it helps, when it causes model collapse, simulation, augmentation
- **2.3.6 Privacy-preserving data work:** anonymisation limits, differential privacy, federated learning (conceptual)

### Module 2.4 Deep learning fundamentals

*Depth target: L3. Prove-it: train a small network from scratch and diagnose a failing training run.*

- **2.4.1 Neural network basics:** perceptron, multilayer perceptron, universal approximation, activation functions (ReLU, GELU, SwiGLU), loss functions
- **2.4.2 Backpropagation:** derivation, computational graphs, gradient checking
- **2.4.3 Initialisation and normalisation:** Xavier, He, batch norm, layer norm, RMSNorm, why they stabilise training
- **2.4.4 Regularisation in deep nets:** dropout, weight decay, data augmentation, early stopping
- **2.4.5 Convolutional networks:** convolution, pooling, ResNets, why residual connections matter
- **2.4.6 Sequence models:** RNN, LSTM, GRU, vanishing gradients, seq2seq, the bottleneck that attention solved
- **2.4.7 Embeddings:** word2vec, GloVe, subword units, learned vs pretrained embeddings, embedding geometry
- **2.4.8 Generative models before transformers:** autoencoders, VAEs, GANs, normalising flows, energy-based models
- **2.4.9 Training in practice:** mixed precision, gradient clipping, checkpointing, debugging loss curves, reproducibility
- **2.4.10 Hardware basics:** GPUs, TPUs, memory limits, throughput vs latency, how to estimate training and inference cost

*Learn from:* Karpathy Neural Networks Zero to Hero, fast.ai Practical Deep Learning, Stanford CS231n, Dive into Deep Learning, Deep Learning (Goodfellow, Bengio, Courville).

### Module 2.5 Other modalities, classical view

- **2.5.1 Computer vision:** classification, detection (YOLO, DETR), segmentation, OCR and document understanding, vision transformers
- **2.5.2 Speech:** acoustic features, ASR (Whisper-style), TTS, speaker diarisation, voice activity detection, streaming latency
- **2.5.3 Graphs:** graph neural networks, knowledge graphs, graph databases, link prediction
- **2.5.4 Tabular and structured:** tabular deep learning, foundation models for tables
- **2.5.5 Multimodal pairing:** CLIP-style contrastive learning, image-text retrieval

### Module 2.6 Reinforcement learning basics

*Depth target: L2 to L3. Needed to understand RLHF, reasoning models and agents.*

- **2.6.1 Core framework:** Markov decision processes, rewards, policies, value functions, Bellman equations
- **2.6.2 Value methods:** dynamic programming, Monte Carlo, temporal difference, Q-learning, DQN
- **2.6.3 Policy methods:** REINFORCE, actor-critic, PPO, trust regions, GRPO
- **2.6.4 Exploration:** epsilon-greedy, UCB, Thompson sampling, curiosity
- **2.6.5 Reward design:** reward hacking, specification gaming, sparse rewards, shaping
- **2.6.6 Offline and model-based RL, multi-agent RL**
- **2.6.7 Landmarks:** TD-Gammon, Atari DQN, AlphaGo, AlphaZero, OpenAI Five, AlphaStar, MuZero

*Learn from:* Sutton and Barto Reinforcement Learning: An Introduction, David Silver's RL lectures, Spinning Up in Deep RL.

### Module 2.7 Machine learning systems and MLOps

- **2.7.1 Lifecycle:** problem framing, data, training, evaluation, deployment, monitoring, retraining
- **2.7.2 Experiment tracking and reproducibility:** MLflow, Weights and Biases, seeds, data versioning (DVC)
- **2.7.3 Pipelines and orchestration:** Airflow, Dagster, Prefect, Kubeflow
- **2.7.4 Feature stores and training-serving skew**
- **2.7.5 Serving patterns:** batch, real-time, streaming, edge, on-device
- **2.7.6 Release strategies:** shadow mode, canary, A/B, interleaving, rollback
- **2.7.7 Monitoring:** data drift, concept drift, performance decay, alerting, feedback loops
- **2.7.8 Cost and capacity planning**

*Learn from:* Designing Machine Learning Systems (Chip Huyen), Made With ML, Google's Rules of Machine Learning.

---

## Part 3: Modern AI science: LLMs, multimodal, reasoning, alignment

### Module 3.1 Language modelling and tokenisation

*Depth target: L3. Prove-it: build a character-level language model, then a byte-pair-encoding tokenizer, and explain why tokenisation causes odd model behaviour.*

- **3.1.1 Language modelling:** next-token prediction, chain-rule factorisation, n-grams, neural language models, perplexity, bits per byte
- **3.1.2 Tokenisation:** characters vs words vs subwords, byte-pair encoding, WordPiece, SentencePiece, unigram, byte-level BPE, vocabulary size trade-offs
- **3.1.3 Tokenisation consequences:** why models struggle with spelling and arithmetic, multilingual cost differences, token counts and pricing, special tokens, chat templates
- **3.1.4 Embeddings in LLMs:** token embeddings, positional information, tied embeddings, embedding models vs generative models
- **3.1.5 Sampling and decoding:** greedy, beam search, temperature, top-k, top-p, min-p, repetition penalties, constrained and grammar-guided decoding, logit bias, logprobs
- **3.1.6 Evaluation of language models:** perplexity, benchmark suites, contamination, human evaluation

*Learn from:* Karpathy makemore, minbpe and Let's build GPT, Let's build the GPT Tokenizer, Stanford CS224N, Stanford CS336 Language Modeling from Scratch.

### Module 3.2 The transformer

*Depth target: L3 to L4. Prove-it: implement a small GPT, then explain each component and its cost to an engineer.*

- **3.2.1 Attention mechanism:** queries, keys, values, scaled dot-product, softmax, causal masking, multi-head attention, why heads specialise
- **3.2.2 Block structure:** residual stream, layer normalisation (pre-norm vs post-norm), feed-forward networks, activation functions (GELU, SwiGLU), parameter counting
- **3.2.3 Positional encoding:** sinusoidal, learned, relative, rotary (RoPE), ALiBi, context-length extension (position interpolation, YaRN)
- **3.2.4 Attention variants:** multi-query, grouped-query, multi-head latent attention, sliding window, sparse attention, linear attention
- **3.2.5 Efficient attention implementation:** FlashAttention, memory vs compute bound operations, why O(n squared) is a memory problem
- **3.2.6 Encoder, decoder, encoder-decoder:** BERT, GPT, T5 families, why decoder-only dominates generative work
- **3.2.7 Computational accounting:** parameters, FLOPs per token, memory for weights, activations and optimiser states, rules of thumb (about 6 times parameters times tokens for training FLOPs)
- **3.2.8 Why transformers work:** parallelism in training, scalability, in-context learning, induction heads, the residual stream view

*Learn from:* Attention Is All You Need (paper), The Illustrated Transformer (Jay Alammar), Karpathy Let's build GPT, 3Blue1Brown transformer chapters, Harvard Annotated Transformer, Transformer Circuits Thread (Anthropic).

### Module 3.3 Pretraining and data

*Depth target: L3. Prove-it: write a data-mixture proposal for a hypothetical model and justify each source.*

- **3.3.1 Pretraining objective:** causal language modelling, masked modelling, denoising, multi-token prediction
- **3.3.2 Data sources:** web crawls (Common Crawl and derived corpora), books, code, scientific papers, forums, licensed data, multilingual data, synthetic data
- **3.3.3 Data pipeline:** extraction, language identification, quality filtering, deduplication (exact and fuzzy), toxicity and PII filtering, decontamination, mixture ratios, curriculum and annealing
- **3.3.4 Data quality over quantity:** textbook-quality data, classifier-based filtering, rephrasing and synthetic expansion, data-constrained scaling and repeating epochs
- **3.3.5 Training infrastructure:** data, tensor, pipeline, sequence and expert parallelism, ZeRO and FSDP, activation checkpointing, failure recovery, cluster utilisation (MFU)
- **3.3.6 Training stability:** loss spikes, learning-rate and initialisation choices, mixed precision, low-precision training
- **3.3.7 Legal and ethical aspects of data:** copyright, licensing, opt-outs, consent, data provenance

*Learn from:* The FineWeb report (Hugging Face), Llama technical reports, DeepSeek technical reports, The Ultra-Scale Playbook (Hugging Face), Stanford CS336.

### Module 3.4 Scaling laws and compute economics

*Depth target: L3 to L4. This is how to talk about where AI is going without hype.*

- **3.4.1 Empirical scaling laws:** Kaplan et al., Chinchilla, compute-optimal training, loss as a power law in compute, data and parameters
- **3.4.2 Beyond pretraining scaling:** inference-time compute scaling, reinforcement learning scaling, data-limited regimes
- **3.4.3 Emergence and its critics:** emergent abilities vs metric artefacts, grokking, phase transitions
- **3.4.4 Compute accounting:** FLOPs, GPU-hours, cluster size, training cost estimates, cost per token curves over time, algorithmic efficiency gains
- **3.4.5 The bitter lesson and its limits:** general methods plus compute vs hand-built knowledge, debates on data walls and diminishing returns
- **3.4.6 Forecasting:** Epoch AI methodology, trend extrapolation, uncertainty ranges

*Learn from:* Scaling Laws for Neural Language Models, Training Compute-Optimal LLMs (Chinchilla), Rich Sutton The Bitter Lesson, Epoch AI, Dwarkesh Patel interviews.

### Module 3.5 Post-training: making a base model useful

*Depth target: L3 to L4. Prove-it: explain why a base model and a chat model differ and run a small SFT and DPO experiment.*

- **3.5.1 Supervised fine-tuning:** instruction data, chat formats, data quality and diversity, loss masking, catastrophic forgetting
- **3.5.2 Preference learning and RLHF:** reward models, human preference data, PPO-based RLHF, KL penalties, over-optimisation
- **3.5.3 Direct preference methods:** DPO, IPO, KTO, ORPO, trade-offs vs RLHF
- **3.5.4 AI feedback:** RLAIF, constitutional AI, rubric-based rewards, model-written critiques
- **3.5.5 Reinforcement learning with verifiable rewards:** math and code verifiers, GRPO, outcome vs process rewards, rejection sampling, self-play
- **3.5.6 Character and behaviour shaping:** persona, tone, refusal behaviour, sycophancy and how post-training can cause it, system prompts vs weights
- **3.5.7 Tool-use and agentic training:** training for function calling, long-horizon trajectories, environments, rollouts at scale
- **3.5.8 Evaluation of post-trained models:** preference leaderboards, arena-style evaluation, contamination, gaming of benchmarks

*Learn from:* InstructGPT paper, Constitutional AI paper, DPO paper, DeepSeek-R1 and DeepSeekMath papers, Nathan Lambert's RLHF Book and Interconnects blog, Tulu 3 report.

### Module 3.6 Reasoning models and test-time compute

*Depth target: L3. Prove-it: compare a reasoning model and a standard model on the same hard tasks and explain the cost-quality curve.*

- **3.6.1 Chain-of-thought:** prompting, why it helps, faithfulness of stated reasoning
- **3.6.2 Training for reasoning:** reinforcement learning on verifiable tasks, long chains, emergent self-correction
- **3.6.3 Inference-time search:** best-of-n, majority voting, tree search, process reward models, self-consistency, budget controls
- **3.6.4 Product implications:** latency, cost, when to use reasoning models, thinking budgets, hidden vs shown reasoning
- **3.6.5 Limits:** brittleness, overthinking, reward hacking, evaluation of reasoning, planning and long-horizon failures

### Module 3.7 Architectures beyond the vanilla transformer

*Depth target: L2 to L3.*

- **3.7.1 Mixture of experts:** routing, load balancing, sparse vs dense compute, total vs active parameters, serving challenges (Switch, Mixtral, DeepSeek-MoE)
- **3.7.2 State-space and recurrent revivals:** Mamba, RWKV, linear attention, hybrid models, trade-offs for long context
- **3.7.3 Long-context methods:** position extrapolation, ring attention, memory layers, retrieval-augmented architectures, needle-in-haystack and its limits, lost in the middle
- **3.7.4 Diffusion language models and other alternatives:** parallel decoding, masked diffusion, energy-based ideas
- **3.7.5 Small models and efficiency:** distillation, pruning, quantisation-aware training, on-device models, why small models keep getting better
- **3.7.6 Memory and continual learning:** parametric vs non-parametric memory, test-time training, catastrophic forgetting, open problems

### Module 3.8 Multimodal and generative media

*Depth target: L2 to L3.*

- **3.8.1 Vision-language models:** image encoders, projection layers, interleaved image and text, document and chart understanding, OCR-free parsing
- **3.8.2 Image generation:** diffusion models (DDPM, latent diffusion, classifier-free guidance), flow matching, autoregressive image models, ControlNet, personalisation
- **3.8.3 Video generation:** spatio-temporal diffusion, world-simulator claims and their limits, consistency and physics failures
- **3.8.4 Audio and speech:** speech recognition, text-to-speech, voice cloning, speech-to-speech models, full-duplex conversation, music generation
- **3.8.5 Native multimodal models:** single model for text, image, audio, video; tokenising non-text modalities
- **3.8.6 3D, robotics and world models:** vision-language-action models, simulation, embodied reasoning
- **3.8.7 Provenance and detection:** watermarking, C2PA, deepfake detection and its limits

### Module 3.9 Inference and serving

*Depth target: L3. This is where cost, latency and your margins are decided.*

- **3.9.1 Inference anatomy:** prefill vs decode, compute-bound vs memory-bound, time to first token vs tokens per second
- **3.9.2 KV cache:** what it stores, memory growth with context and batch, paged attention, prefix caching, prompt caching as a product feature
- **3.9.3 Quantisation:** INT8, INT4, FP8, GPTQ, AWQ, GGUF, quality vs cost trade-offs
- **3.9.4 Speed-up techniques:** speculative decoding, continuous batching, chunked prefill, disaggregated prefill and decode, kernel fusion
- **3.9.5 Serving stacks:** vLLM, SGLang, TensorRT-LLM, llama.cpp, Ollama, Triton, managed endpoints
- **3.9.6 Hardware:** NVIDIA GPU generations, AMD, Google TPU, AWS Trainium and Inferentia, Groq, Cerebras, memory bandwidth and interconnects
- **3.9.7 Cost modelling:** cost per million tokens, utilisation, batch size effects, cloud vs owned hardware, spot capacity
- **3.9.8 Edge and on-device:** phone and laptop models, privacy and latency benefits, limits

*Learn from:* Chip Huyen on inference optimisation, vLLM paper and docs, Lilian Weng on inference optimisation, Stanford CS336 systems lectures.

### Module 3.10 Adapting open-weight models

*Depth target: L3. Prove-it: fine-tune a small open model with LoRA on a narrow task and compare it with prompting.*

- **3.10.1 Open-weight ecosystem:** Llama, Mistral, Qwen, DeepSeek, Gemma, Phi, OLMo, licences (open weights vs open source), Hugging Face Hub
- **3.10.2 Parameter-efficient fine-tuning:** LoRA, QLoRA, adapters, prefix tuning, rank and alpha choices, merging adapters
- **3.10.3 Full fine-tuning vs PEFT:** compute, data and quality trade-offs
- **3.10.4 Distillation:** teacher-student, synthetic data from frontier models, terms-of-service constraints
- **3.10.5 Model merging and routing:** weight averaging, task vectors, cascades, mixtures of agents
- **3.10.6 Training tools:** Hugging Face Transformers, TRL, PEFT, Unsloth, Axolotl, torchtune, Modal, RunPod

### Module 3.11 Interpretability

*Depth target: L2 to L3. Needed to follow safety, trust and regulation debates.*

- **3.11.1 Probing and attribution:** linear probes, saliency, attention analysis and its limits
- **3.11.2 Mechanistic interpretability:** circuits, features, superposition, sparse autoencoders, dictionary learning, activation steering
- **3.11.3 Behavioural interpretability:** chain-of-thought monitoring, model self-reports and their reliability
- **3.11.4 Why it matters:** auditing, safety cases, debugging, regulation

*Learn from:* Anthropic's Transformer Circuits Thread (Toy Models of Superposition, Scaling Monosemanticity), Neel Nanda's tutorials, Chris Olah's writing.

### Module 3.12 Alignment and model behaviour

*Depth target: L3.*

- **3.12.1 The alignment problem:** specification vs intent, reward hacking, goal misgeneralisation, inner vs outer alignment
- **3.12.2 Behavioural failure modes:** hallucination, sycophancy, deception, sandbagging, reward hacking in agents, jailbreak susceptibility
- **3.12.3 Techniques:** RLHF, constitutional approaches, scalable oversight, debate, weak-to-strong generalisation, red teaming, adversarial training, control protocols
- **3.12.4 Evaluation of dangerous capabilities:** CBRN, cyber, autonomy, persuasion, frontier-safety frameworks and responsible scaling policies
- **3.12.5 Model welfare, character and values documents:** how developers specify model behaviour publicly

*Learn from:* Human Compatible (Stuart Russell), The Alignment Problem (Brian Christian), AI Safety Fundamentals curriculum (BlueDot Impact), lab safety framework documents, Alignment Forum.

### Module 3.13 Benchmarks and capability measurement

*Depth target: L3 to L4. Most people misread benchmarks; you should not.*

- **3.13.1 Knowledge and reasoning:** MMLU and variants, GPQA, Humanity's Last Exam, ARC-AGI
- **3.13.2 Maths and code:** GSM8K, MATH, AIME-style problems, HumanEval, SWE-bench and variants, LiveCodeBench, Terminal-style tasks
- **3.13.3 Agentic and long-horizon:** tau-bench style tool tasks, WebArena, OSWorld, METR task-horizon measurements, computer-use benchmarks
- **3.13.4 Preference and arena evaluation:** Elo-style arenas, style control, gaming risks
- **3.13.5 Failure of benchmarks:** saturation, contamination, prompt sensitivity, cherry-picked settings, benchmark vs product performance
- **3.13.6 Building your own task-specific benchmark** (links to Part 4, Module 4.8)

### Module 3.14 Reading research like a professional

- **3.14.1 Paper triage:** abstract, figures, method, results, limitations, in 15 minutes
- **3.14.2 Deep reading:** reproducing a result, reading appendices, spotting weak baselines and unfair comparisons
- **3.14.3 Sources:** arXiv, Hugging Face Daily Papers, lab blogs, conference proceedings (NeurIPS, ICML, ICLR, ACL), Semantic Scholar, Papers with Code successors
- **3.14.4 Translating research into product bets:** what is real, what is lab-scale, what will be a feature in 6 to 24 months

---

## Part 4: Applied AI engineering

This is the working craft of building with models. A top AI product leader should be able to prototype every pattern here and explain its failure modes.

### Module 4.1 Working with model APIs

*Depth target: L3 to L4. Prove-it: build a small client that handles streaming, retries, structured outputs and cost tracking.*

- **4.1.1 Request anatomy:** system, user and assistant messages, tool messages, parameters (temperature, top-p, max tokens, stop sequences), response objects, usage accounting
- **4.1.2 Streaming:** server-sent events, partial tokens, handling tool calls in streams, UX consequences
- **4.1.3 Structured outputs:** JSON mode, schema-constrained decoding, function-call schemas, validation and repair loops, Pydantic and Zod
- **4.1.4 Reliability:** rate limits, timeouts, retries with backoff, idempotency, fallbacks across models and providers, circuit breakers
- **4.1.5 Cost controls:** prompt caching, batch APIs, token budgeting, model routing, max-token ceilings
- **4.1.6 Provider landscape:** Anthropic, OpenAI, Google, Mistral, Cohere, xAI, open-weight hosts, cloud marketplaces (Bedrock, Vertex AI, Azure AI Foundry), gateways and routers
- **4.1.7 Model lifecycle:** versions, deprecations, regression risk when models update, pinning versions, migration playbooks

### Module 4.2 Prompt and context engineering

*Depth target: L4. Prove-it: take a failing production-style prompt and fix it using evals, not intuition.*

- **4.2.1 Prompt anatomy:** role, task, constraints, format, examples, delimiters and XML tags, ordering
- **4.2.2 Techniques:** few-shot, chain-of-thought, self-critique, decomposition, prefill, step-back prompting, structured reasoning
- **4.2.3 System prompt design:** behaviour specs, tone, refusal policy, tool instructions, versioning
- **4.2.4 Context engineering:** what to put in the window, retrieval vs static context, summarisation and compaction, ordering effects, context rot and long-context degradation, isolating context across sub-agents
- **4.2.5 Prompt caching:** stable prefixes, cache-friendly design, cost impact
- **4.2.6 Prompt injection:** direct and indirect, trust boundaries, instruction hierarchy, defences and their limits
- **4.2.7 Prompt management:** version control, templates, variables, A/B testing prompts, prompt registries
- **4.2.8 Prompt optimisation:** automated prompt search, DSPy-style programmatic optimisation, eval-guided iteration

*Learn from:* Anthropic prompt engineering docs and Effective Context Engineering for AI Agents (Anthropic engineering blog), OpenAI prompt guides, Lilian Weng Prompt Engineering, DSPy docs.

### Module 4.3 Tool use, function calling and MCP

*Depth target: L4. Prove-it: build and publish an MCP server and write down its threat model.*

- **4.3.1 The tool loop:** model proposes call, application executes, result returned, model continues; parallel tool calls; forced tool choice
- **4.3.2 Tool design:** names, descriptions as prompts, parameter schemas, error messages the model can act on, idempotency, pagination, token-efficient outputs, avoiding tool overload
- **4.3.3 Model Context Protocol:** hosts, clients, servers, transports (stdio, streamable HTTP), tools, resources, prompts, sampling, elicitation, authorisation flows, registries
- **4.3.4 Agent-computer interfaces:** code execution sandboxes, shell tools, file editing tools, browser and computer use, text editors
- **4.3.5 Skills and reusable instructions:** packaged instructions and resources loaded on demand, progressive disclosure
- **4.3.6 Security of tools:** least privilege, confirmation for destructive actions, tool poisoning, confused-deputy problems, secrets handling, audit logs
- **4.3.7 Integration patterns:** wrapping internal APIs, enterprise connectors, OAuth for agents, rate limiting and quotas

*Learn from:* modelcontextprotocol.io spec and docs, Anthropic Writing Effective Tools for Agents, OpenAI function-calling guide.

### Module 4.4 Retrieval-augmented generation and knowledge systems

*Depth target: L4. Prove-it: build a RAG system on a real corpus, measure retrieval and answer quality separately, and improve both.*

- **4.4.1 Embeddings:** how they are trained, dense vs sparse, multi-vector (ColBERT), domain adaptation, dimension and cost trade-offs, multilingual and multimodal embeddings, evaluation with MTEB-style tasks
- **4.4.2 Indexing:** vector databases (pgvector, Pinecone, Weaviate, Qdrant, Milvus, Chroma, Elasticsearch, OpenSearch), ANN algorithms (HNSW, IVF, PQ), filtering, updates, sharding
- **4.4.3 Ingestion:** parsing PDFs, tables, slides, HTML, scanned documents, OCR, layout-aware extraction, metadata enrichment, deduplication, versioning
- **4.4.4 Chunking:** fixed, recursive, semantic, structure-aware, hierarchical, late chunking, contextual chunk headers
- **4.4.5 Retrieval:** BM25, hybrid search, reciprocal rank fusion, metadata filters, query rewriting, multi-query, HyDE, query decomposition, routing across indexes
- **4.4.6 Reranking:** cross-encoders, LLM rerankers, score calibration, cutoffs
- **4.4.7 Generation:** context assembly, citation and attribution, handling conflicts, abstention when evidence is missing, answer formats
- **4.4.8 Advanced patterns:** agentic RAG, graph RAG, multi-hop retrieval, self-RAG, corrective RAG, retrieval over code and structured data, text-to-SQL, long context vs RAG
- **4.4.9 Access control in retrieval:** document-level permissions, tenant isolation, row-level security, leakage tests
- **4.4.10 Evaluation:** retrieval metrics (recall at k, MRR, NDCG), groundedness, answer correctness, end-to-end vs component evals, diagnosing failures by stage
- **4.4.11 Operations:** freshness, re-indexing, drift in embeddings, cost of storage and queries

*Learn from:* AI Engineering (Chip Huyen), Anthropic Contextual Retrieval, Eugene Yan writing on retrieval and evals, Pinecone and Weaviate learning centres, MTEB leaderboard.

### Module 4.5 Agents

*Depth target: L4. Prove-it: build an agent with tools, memory and a human approval step, then evaluate trajectories, not only final answers.*

- **4.5.1 Workflows vs agents:** deterministic orchestration vs model-directed control flow, when each wins
- **4.5.2 Patterns:** prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimiser, ReAct, plan-and-execute, reflection, hierarchical agents
- **4.5.3 Multi-agent systems:** division of labour, shared state, handoffs, context isolation, coordination cost, when multi-agent hurts
- **4.5.4 Long-running agents:** checkpoints, resumability, background execution, task queues, progress reporting, human interrupts
- **4.5.5 Planning and control:** task decomposition, replanning, budgets for steps, tokens and time, stopping criteria, loop detection
- **4.5.6 Environments and sandboxes:** code execution, browsers, virtual desktops, file systems, network policies
- **4.5.7 Agent frameworks:** Claude Agent SDK, OpenAI Agents SDK, LangGraph, LlamaIndex, CrewAI, AutoGen successors, and the case for writing none
- **4.5.8 Agent interoperability:** MCP, agent-to-agent protocols, agent identity and authorisation, agent payments
- **4.5.9 Agent evaluation:** trajectory evaluation, tool-call accuracy, task completion, cost and step efficiency, reliability across repeated runs (pass-at-k vs pass-to-the-power-k)
- **4.5.10 Failure modes:** compounding errors, tool misuse, infinite loops, goal drift, reward hacking, prompt injection through tool results
- **4.5.11 Computer-use and browser agents:** screenshots vs DOM, latency, reliability, safety constraints

*Learn from:* Building Effective Agents and How We Built Our Multi-Agent Research System (Anthropic engineering), Lilian Weng LLM Powered Autonomous Agents, ReAct paper, METR task-horizon research.

### Module 4.6 Memory and personalisation

- **4.6.1 Memory types:** working, episodic, semantic, procedural; in-context vs external stores
- **4.6.2 Implementations:** summaries, key-value fact stores, vector memory, file-based memory, knowledge graphs, memory tools exposed to the model
- **4.6.3 Memory quality problems:** stale facts, contradictions, over-personalisation, leakage between contexts, sensitive data in memory
- **4.6.4 Privacy and control:** user visibility, edit and delete, retention policy, consent
- **4.6.5 Evaluation:** recall accuracy, usefulness, harm from wrong memories

### Module 4.7 Customisation decisions: prompting, RAG, fine-tuning, or build

*Depth target: L4. This is one of the most valuable PM judgement calls.*

- **4.7.1 Decision framework:** knowledge gaps vs behaviour gaps vs cost and latency gaps; which tool fixes which
- **4.7.2 When fine-tuning wins:** style and format consistency, narrow high-volume tasks, latency and cost reduction via small models, proprietary behaviours
- **4.7.3 When it does not:** fast-changing knowledge, small datasets, moving model baselines
- **4.7.4 Data for fine-tuning:** collection from production, curation, labelling, synthetic data, privacy constraints
- **4.7.5 Preference and reinforcement fine-tuning offered by providers:** what it is good for
- **4.7.6 Maintenance burden:** retraining as base models improve, evaluation pipelines, versioning

### Module 4.8 Evaluations

*Depth target: L4 to L5. The single highest-leverage skill in applied AI.*

- **4.8.1 Why evals:** the new unit tests and acceptance criteria, evals as product specification
- **4.8.2 Error analysis:** reading traces, open coding, building a failure taxonomy, counting and prioritising
- **4.8.3 Datasets:** golden sets, production sampling, synthetic generation, adversarial sets, edge cases, versioning, contamination control, how many examples are enough
- **4.8.4 Graders:** exact match, programmatic checks, rubric-based human review, LLM-as-judge (design, calibration against humans, bias types such as position, verbosity and self-preference), pairwise vs pointwise, multi-judge panels
- **4.8.5 Metrics:** task success, groundedness, faithfulness, relevance, safety, tone, latency, cost per task, consistency across runs
- **4.8.6 Agent and multi-turn evals:** trajectory graders, simulated users, tool-call checks, end-state checks, long-horizon tasks
- **4.8.7 Offline to online:** regression suites in CI, shadow deployments, A/B tests for AI features, implicit feedback signals, human review queues
- **4.8.8 Eval operations:** dataset governance, annotator guidelines and agreement, eval cost, eval drift, who owns evals
- **4.8.9 Release gates:** thresholds, risk-tiered launch criteria, rollback criteria
- **4.8.10 Tools:** Braintrust, Langfuse, LangSmith, Arize Phoenix, Promptfoo, OpenAI Evals, Inspect (UK AISI), custom harnesses

*Learn from:* Hamel Husain and Shreya Shankar on evals, Eugene Yan on LLM-as-judge, Who Validates the Validators paper, Inspect docs, Anthropic and OpenAI eval documentation.

### Module 4.9 LLMOps and observability

- **4.9.1 Tracing:** spans for model calls, tools and retrieval, OpenTelemetry for LLMs, redaction of sensitive data
- **4.9.2 Monitoring:** quality drift, cost and latency dashboards, refusal and error rates, feedback capture
- **4.9.3 Deployment:** model gateways, routing, feature flags for prompts and models, staged rollouts
- **4.9.4 Versioning:** prompts, models, tools, datasets, evaluators; reproducibility of an old run
- **4.9.5 Incident response:** model outages, provider failover, bad releases, prompt-injection incidents, post-mortems
- **4.9.6 Governance of change:** who approves a prompt change, change logs, audit trails

### Module 4.10 Guardrails and reliability engineering

- **4.10.1 Input controls:** PII detection, injection detection, topic filters, rate limits
- **4.10.2 Output controls:** schema validation, policy classifiers, grounding checks, citation verification, refusal handling
- **4.10.3 Action controls:** permission tiers, human approval, dry-run modes, reversible actions, spending limits
- **4.10.4 Defence in depth:** layering model-level, prompt-level and system-level controls
- **4.10.5 Red teaming:** manual and automated adversarial testing, jailbreak libraries, severity scoring
- **4.10.6 Fallbacks and graceful degradation:** what the product does when the model is wrong, slow or down
- **4.10.7 Tools:** policy classifiers, Llama Guard-style models, NeMo Guardrails, Guardrails AI, provider safety endpoints

### Module 4.11 Multimodal and voice applications

- **4.11.1 Document intelligence:** layout parsing, tables, forms, charts, handwriting, accuracy measurement
- **4.11.2 Vision applications:** inspection, retail, medical imaging triage (regulated), accessibility
- **4.11.3 Voice agents:** pipeline (ASR, LLM, TTS) vs speech-to-speech, turn-taking, interruption handling, latency budgets under 1 second, telephony integration (SIP, WebRTC), accent and noise robustness, compliance for recorded calls
- **4.11.4 Generative media workflows:** image, video and audio tools, brand consistency, rights and provenance
- **4.11.5 Evaluation of multimodal systems:** task-specific rubrics, human review

### Module 4.12 Coding agents and AI-assisted development

*Depth target: L4. Also the fastest way to build your own prototypes.*

- **4.12.1 Landscape:** terminal agents (Claude Code and peers), IDE agents (Cursor, Windsurf, Copilot), cloud agents, app builders (v0, Lovable, Bolt, Replit)
- **4.12.2 Effective workflows:** specification first, plan mode, small verified steps, test-driven loops, project instruction files, subagents, hooks, custom commands, skills, parallel agents on worktrees
- **4.12.3 Context management in coding:** repository maps, retrieval over code, compaction, memory files
- **4.12.4 Review and quality:** reviewing diffs, tests as guardrails, security scanning, avoiding unreviewed code in production
- **4.12.5 Limits and risks:** hallucinated APIs, subtle bugs, over-engineering, secret leakage, dependency risk
- **4.12.6 Product implications:** what happens to team structure, estimates and PM-engineer boundaries when code gets cheap

### Module 4.13 Search, knowledge and enterprise data

- **4.13.1 Enterprise search:** connectors, permission mirroring, freshness, ranking signals, Glean-style systems
- **4.13.2 Text-to-SQL and analytics agents:** schema grounding, semantic layers, query validation, access control, accuracy measurement
- **4.13.3 Knowledge graphs and ontologies:** when structure beats embeddings, entity resolution, graph construction with LLMs
- **4.13.4 Web search for agents:** search APIs, browsing, citation, source quality, copyright limits

### Module 4.14 Cost, latency and performance engineering

- **4.14.1 Latency budgets:** network, retrieval, model, tool, rendering; perceived latency vs actual latency
- **4.14.2 Cost levers:** model selection and routing, caching (prompt, semantic, result), shorter contexts, batch processing, distillation, early exits
- **4.14.3 Unit economics instrumentation:** cost per task, cost per user, margin by cohort, abuse and heavy-user detection
- **4.14.4 Capacity and rate limits:** provisioned throughput, quotas, burst handling, queueing

### Module 4.15 Data engineering for AI

- **4.15.1 Ingestion pipelines:** batch vs streaming, change data capture, connectors
- **4.15.2 Warehouses and lakehouses:** Snowflake, BigQuery, Databricks, Iceberg and Delta formats, dbt
- **4.15.3 Unstructured data operations:** document stores, OCR pipelines, metadata, deduplication
- **4.15.4 Data governance for AI:** lineage, classification, consent, retention, residency
- **4.15.5 Feedback loops:** capturing user signals, labelling queues, turning production data into eval and training data safely

### Module 4.16 Enterprise integration and deployment

- **4.16.1 Identity and access:** SSO, SAML, OIDC, SCIM, role-based and attribute-based access, tenant isolation
- **4.16.2 Deployment models:** SaaS, single-tenant, private cloud, VPC peering, on-premise, air-gapped
- **4.16.3 Data handling commitments:** zero data retention, regional residency, encryption, customer-managed keys, audit logging
- **4.16.4 Security reviews:** SOC 2, ISO 27001, penetration tests, vendor questionnaires, model-provider sub-processor chains
- **4.16.5 Integration surfaces:** APIs, webhooks, browser extensions, plugins, embedded components, Slack and Teams apps, email and calendar integration

---

## Part 5: Software, systems and infrastructure

This is the technical depth that makes engineers trust a product leader. Aim for L3 everywhere and L4 on APIs, identity, data and security.

### Module 5.1 Web fundamentals and the request lifecycle

*Prove-it: trace one request from a browser tap to a database row and back, naming every hop, its latency and its failure mode.*

- **5.1.1 Client to server journey:** DNS resolution, TCP handshake, TLS handshake, HTTP request, load balancer, reverse proxy, application server, cache, database, response, rendering
- **5.1.2 HTTP in depth:** methods and their semantics, status code families, headers (caching, content negotiation, auth, CORS), cookies, bodies, compression, HTTP/2 multiplexing, HTTP/3 and QUIC
- **5.1.3 Real-time channels:** polling, long polling, server-sent events, WebSockets, WebRTC, why streaming LLM output uses SSE
- **5.1.4 Sync vs async:** blocking vs non-blocking, queues, background jobs, webhooks, callbacks, eventual consistency
- **5.1.5 Latency vs throughput:** percentiles (p50, p95, p99), tail latency, Little's law, queueing delay, back-pressure
- **5.1.6 Where things break:** diagnosing a symptom to a layer (DNS, network, TLS, proxy, app, cache, DB, third party)
- **5.1.7 Browsers:** rendering pipeline, JavaScript event loop, storage options, service workers, performance metrics (Core Web Vitals)

### Module 5.2 APIs

*Prove-it: design, document and version a public API for a hypothetical AI feature, including pagination, errors, idempotency and rate limits.*

- **5.2.1 Styles:** REST, GraphQL, gRPC, JSON-RPC, webhooks, event streams, when each fits
- **5.2.2 Resource design:** nouns vs verbs, naming, relationships, filtering, sorting, pagination (cursor vs offset), partial responses, bulk operations
- **5.2.3 Contracts:** OpenAPI and JSON Schema, schema evolution, backward compatibility, contract testing, SDK generation
- **5.2.4 Errors and reliability:** status and error body design, retries, idempotency keys, timeouts, rate limiting (token bucket, leaky bucket), quotas, circuit breakers
- **5.2.5 Versioning and deprecation:** URL vs header versioning, sunset policies, migration guides, breaking-change management
- **5.2.6 Security of APIs:** authentication schemes, scopes, input validation, mass assignment, BOLA and other OWASP API risks, abuse prevention
- **5.2.7 Async APIs and long-running jobs:** job resources, polling vs callbacks, webhook signing and retries
- **5.2.8 API as product:** developer experience, documentation, quickstarts, sandboxes, pricing, usage analytics, changelogs

### Module 5.3 Authentication, authorisation and identity

*Prove-it: draw the OAuth 2.0 authorisation code flow with PKCE and explain what each token is for and where it could leak.*

- **5.3.1 Core concepts:** identity, authentication, authorisation, sessions, tokens, claims
- **5.3.2 Credentials:** passwords and hashing, MFA, TOTP, WebAuthn and passkeys, recovery flows, account takeover defences
- **5.3.3 Tokens:** session cookies vs bearer tokens, JWT structure and pitfalls, refresh tokens, rotation, revocation
- **5.3.4 Protocols:** OAuth 2.0 grants, PKCE, OpenID Connect, SAML, SCIM provisioning, token exchange
- **5.3.5 Enterprise identity:** SSO, identity providers (Okta, Entra ID, Google Workspace), just-in-time provisioning, directory sync, deprovisioning
- **5.3.6 Authorisation models:** RBAC, ABAC, ReBAC, policy engines (OPA, Cedar), fine-grained authorisation (Zanzibar-style), multi-tenant isolation
- **5.3.7 Identity for machines and agents:** service accounts, API keys, workload identity, delegated authority for AI agents, on-behalf-of flows, scoping and audit
- **5.3.8 Secrets management:** vaults, rotation, environment variables, secret scanning

### Module 5.4 The data layer

*Prove-it: model a multi-tenant schema, choose indexes, and explain what happens during a slow query.*

- **5.4.1 Relational databases:** schemas, normalisation, keys, indexes (B-tree, hash, GIN), query planning, transactions, isolation levels, locking, migrations
- **5.4.2 Non-relational stores:** key-value, document, wide-column, graph, time-series, and the trade-offs against relational
- **5.4.3 Caching:** cache-aside, write-through, TTLs, invalidation, stampedes, CDNs, Redis patterns
- **5.4.4 Search engines:** inverted indexes, relevance scoring, Elasticsearch and OpenSearch, Solr, vector search integration
- **5.4.5 Analytical stores:** OLTP vs OLAP, columnar formats, warehouses, lakehouses, partitioning, data modelling (star schema, medallion architecture)
- **5.4.6 Reliability of data:** replication, backups, point-in-time recovery, disaster recovery objectives (RPO, RTO), sharding, resharding
- **5.4.7 Consistency and distributed data:** CAP and PACELC, eventual consistency, conflict resolution, CRDTs, sagas
- **5.4.8 Data lifecycle:** retention, archival, deletion, right-to-erasure implementation challenges

### Module 5.5 System architecture and design

*Prove-it: produce a design document for an AI feature at 10 times current scale, including a failure analysis.*

- **5.5.1 Architectural styles:** monolith, modular monolith, microservices, serverless, event-driven, hexagonal, CQRS and event sourcing
- **5.5.2 Communication:** synchronous calls, message queues, pub-sub, streaming platforms (Kafka, Pulsar, Kinesis), outbox pattern, workflow engines (Temporal, Airflow, Step Functions)
- **5.5.3 Scalability patterns:** horizontal vs vertical scaling, stateless services, partitioning, load balancing algorithms, autoscaling, backpressure, bulkheads
- **5.5.4 Reliability patterns:** redundancy, graceful degradation, retries with jitter, timeouts, idempotent consumers, dead-letter queues, chaos engineering
- **5.5.5 Multi-tenancy:** pooled vs siloed, noisy neighbour, per-tenant limits, data isolation models
- **5.5.6 Design process:** requirements, constraints, back-of-envelope estimation, design docs, architecture decision records, trade-off tables
- **5.5.7 Common system designs:** URL shortener, chat, feed, notification system, search, payments, rate limiter, file storage, and an LLM gateway
- **5.5.8 Technical debt and migration:** strangler pattern, rewrites vs refactors, deprecation planning, cost of delay

*Learn from:* Designing Data-Intensive Applications, System Design Interview (Alex Xu) volumes, ByteByteGo, High Scalability, Google SRE Book.

### Module 5.6 Cloud and infrastructure

- **5.6.1 Cloud model:** regions, availability zones, shared responsibility, IaaS, PaaS, SaaS, serverless
- **5.6.2 Core services across AWS, Google Cloud and Azure:** compute, storage (object, block, file), networking (VPC, subnets, security groups, peering, private links), managed databases, queues, identity services
- **5.6.3 Containers and orchestration:** Docker, container registries, Kubernetes concepts (pods, services, ingress, autoscaling), service meshes
- **5.6.4 Infrastructure as code:** Terraform, Pulumi, CloudFormation, drift, environments
- **5.6.5 GPU and AI infrastructure:** GPU instance types, quotas, reserved vs on-demand vs spot, specialised clouds (CoreWeave, Lambda, Together, Modal, RunPod), serverless inference
- **5.6.6 Cost management:** FinOps, tagging, budgets, egress costs, rightsizing, commitments
- **5.6.7 Data residency and sovereignty:** regional deployments, sovereign cloud, cross-border transfer rules

### Module 5.7 DevOps and site reliability

- **5.7.1 CI/CD:** pipelines, trunk-based development, build caching, artefact management, environment promotion
- **5.7.2 Release engineering:** feature flags, canary releases, blue-green deployments, rollbacks, database migrations during deploys
- **5.7.3 Observability:** logs, metrics, traces, structured logging, dashboards, alerting quality, OpenTelemetry
- **5.7.4 Reliability management:** SLIs, SLOs, SLAs, error budgets, capacity planning, load testing
- **5.7.5 Incident management:** severity levels, on-call, incident command, communications, blameless post-mortems, learning from outages
- **5.7.6 Developer productivity:** platform engineering, internal developer platforms, build times, DORA metrics

### Module 5.8 Security engineering and compliance

*Depth target: L4. Prove-it: threat-model an AI agent product and answer a real enterprise security questionnaire.*

- **5.8.1 Threat modelling:** STRIDE, attack trees, trust boundaries, data flow diagrams, abuse cases
- **5.8.2 Web and application security:** OWASP Top 10, injection, XSS, CSRF, SSRF, deserialisation, dependency vulnerabilities, secure defaults
- **5.8.3 Cryptography for product people:** symmetric vs asymmetric, hashing, signatures, TLS, key management, envelope encryption, KMS and HSM, encryption at rest and in transit, customer-managed keys
- **5.8.4 Infrastructure security:** least privilege, network segmentation, zero trust, secrets handling, hardening, container security, logging and detection
- **5.8.5 Software supply chain:** SBOM, dependency pinning, provenance, signed builds, typosquatting and package-malware risks
- **5.8.6 Vulnerability management:** scanning, CVE triage, patch SLAs, bug bounties, penetration testing, responsible disclosure
- **5.8.7 Compliance frameworks:** SOC 2, ISO 27001, ISO 27701, ISO 42001 (AI management systems), PCI DSS, HIPAA, GDPR, CCPA, FedRAMP, HITRUST, sector rules in banking and insurance
- **5.8.8 Privacy engineering:** data minimisation, pseudonymisation, consent management, DPIAs, data subject requests, retention schedules
- **5.8.9 Security of AI systems:** see Part 10, Module 10.3

### Module 5.9 Front end, mobile and interaction technology

- **5.9.1 Front-end stack:** HTML, CSS, JavaScript, TypeScript, React, state management, server-side rendering, edge rendering, design tokens
- **5.9.2 Performance and accessibility:** bundle size, caching, perceived performance, WCAG, screen readers, keyboard navigation
- **5.9.3 AI-specific front-end patterns:** streaming UIs, optimistic updates, rendering partial structured output, citations and source panels, canvas and artifact surfaces, voice UIs
- **5.9.4 Mobile:** native vs cross-platform (Swift, Kotlin, React Native, Flutter), app store policies, push notifications, offline sync, on-device models
- **5.9.5 Extensions and embeds:** browser extensions, plugins, iframes, widgets, bridge patterns for embedding AI into existing tools

### Module 5.10 Quality engineering

- **5.10.1 Testing strategy:** unit, integration, end-to-end, contract, property-based, snapshot tests, test data management
- **5.10.2 Non-functional testing:** load, stress, soak, chaos, security, accessibility
- **5.10.3 Testing non-deterministic systems:** statistical tests, eval suites as tests, flaky-test policy, seeds and tolerances
- **5.10.4 QA in the team:** definition of done, release criteria, bug triage, severity vs priority

### Module 5.11 Engineering management literacy for PMs

- **5.11.1 Estimation and planning:** story points and their limits, forecasting, cycle time, throughput, capacity, buffers
- **5.11.2 Build vs buy vs partner:** total cost of ownership, vendor risk, lock-in, exit plans, open-source licence types (MIT, Apache, GPL, AGPL, BSL)
- **5.11.3 Working with engineers:** writing for engineers, technical discovery, spikes, estimates as negotiation, respecting constraints, earning trust
- **5.11.4 Technical strategy:** platform investments, paved roads, architecture as a product constraint, sequencing technical bets

---

## Part 6: Data, analytics and experimentation

### Module 6.1 Product analytics

*Prove-it: instrument a product from scratch, build a funnel and a retention curve, and find one non-obvious insight.*

- **6.1.1 Event design:** event taxonomy, naming conventions, properties, user and account identity, instrumentation plans, QA of tracking
- **6.1.2 Core analyses:** funnels, cohorts, retention curves, segmentation, paths, stickiness (DAU/MAU), time-to-value, feature adoption
- **6.1.3 Metric frameworks:** North Star metric, input metrics, HEART, AARRR, jobs-based metrics, B2B account-level metrics (seats, workspaces, health scores)
- **6.1.4 Tools:** Amplitude, Mixpanel, PostHog, Heap, Pendo, Segment and RudderStack, warehouse-native analytics
- **6.1.5 Privacy-aware analytics:** consent, anonymisation, sampling, server-side tracking, regional rules

### Module 6.2 Analytics engineering and BI

- **6.2.1 Modelling data for analysis:** dimensional models, dbt, metrics layers and semantic layers, data contracts
- **6.2.2 SQL at an analyst level:** window functions, cohort queries, retention queries, funnel queries, sessionisation, performance tuning
- **6.2.3 Dashboards that drive decisions:** audience-first design, metric definitions, anti-patterns, alerting on anomalies
- **6.2.4 Tools:** Looker, Tableau, Power BI, Metabase, Hex, Mode, notebooks

### Module 6.3 Experimentation

*Depth target: L4. Prove-it: design an experiment for an AI feature, pre-register the analysis, and explain the result including its limits.*

- **6.3.1 Design:** hypotheses, randomisation units, metrics hierarchy, guardrails, minimum detectable effect, sample size and duration, novelty and primacy effects
- **6.3.2 Analysis:** significance and practical significance, confidence intervals, variance reduction (CUPED), heterogeneous effects, multiple testing, sequential and always-valid inference, Bayesian approaches
- **6.3.3 Hard cases:** network effects and interference, marketplaces, switchback tests, geo experiments, long-term holdouts, small-sample B2B
- **6.3.4 Quasi-experiments:** difference-in-differences, synthetic control, regression discontinuity, interrupted time series
- **6.3.5 Experimenting on AI features:** non-determinism, model version confounds, cost as a metric, quality metrics beyond clicks, human evaluation in the loop, interleaving for ranking, offline-online disagreement
- **6.3.6 Experimentation culture and platform:** decision rules, experiment review, platform tools (Statsig, Eppo, Optimizely, LaunchDarkly), pitfalls such as p-hacking

*Learn from:* Trustworthy Online Controlled Experiments (Kohavi), Statsig and Eppo blogs, Netflix and Airbnb experimentation write-ups.

### Module 6.4 Metric design and decision quality

- **6.4.1 Good metrics:** actionable, sensitive, attributable, hard to game; Goodhart's law and counter-metrics
- **6.4.2 Metric trees:** decomposing outcomes into drivers, leading vs lagging indicators
- **6.4.3 OKRs and goals:** writing outcome-based objectives, avoiding output goals, cadence, grading
- **6.4.4 AI-specific metrics:** task success rate, acceptance rate of suggestions, edit distance, escalation rate, deflection with quality, hallucination rate, time saved per task, cost per successful task, trust and reliance measures
- **6.4.5 Qualitative and quantitative together:** triangulation, sampling bias, vanity metrics

### Module 6.5 Business modelling and forecasting

- **6.5.1 Market sizing:** top-down, bottom-up, TAM, SAM, SOM, sanity checks
- **6.5.2 Revenue modelling:** funnels to revenue, cohort models, seat expansion, usage-based revenue with variance, scenario and sensitivity analysis
- **6.5.3 Unit economics:** CAC, LTV, payback period, gross margin by cohort, contribution margin, AI inference cost as COGS
- **6.5.4 Pricing analytics:** willingness-to-pay methods (Van Westendorp, conjoint, Gabor-Granger), price tests, discount discipline
- **6.5.5 Business cases:** investment cases, build vs buy cases, sensitivity to assumptions, writing for CFOs

### Module 6.6 User research

*Depth target: L3 to L4.*

- **6.6.1 Research design:** research questions, methods selection, sample and recruiting, ethics and consent
- **6.6.2 Interviews:** discovery interviews, avoiding leading questions, story-based interviewing, probing, silence, synthesis
- **6.6.3 Surveys:** design, bias, scales, NPS, CSAT, CES and their limits, Likert analysis, sample size
- **6.6.4 Usability testing:** moderated and unmoderated, think-aloud, task design, severity rating, think-aloud for AI features
- **6.6.5 Jobs to be done:** job stories, switching interviews, forces diagram, outcome-driven innovation
- **6.6.6 Behavioural methods:** diary studies, contextual inquiry, shadowing, session replay, support-ticket mining
- **6.6.7 Research for AI:** studying trust, over-reliance and mental models, conversation log analysis, failure-case interviews, wizard-of-oz prototypes
- **6.6.8 Synthesis and communication:** affinity mapping, insight statements, personas vs jobs, research repositories

*Learn from:* The Mom Test, Continuous Discovery Habits (Teresa Torres), Competing Against Luck (Christensen), Just Enough Research (Erika Hall).

---

## Part 7: Product management craft

### Module 7.1 Product management fundamentals

- **7.1.1 The role:** what a PM is accountable for, PM vs product owner vs product marketing vs program manager vs designer vs engineering manager
- **7.1.2 Operating models:** feature teams vs empowered product teams, outcomes vs outputs, product trios, Cagan's product operating model, startup vs scale-up vs enterprise differences
- **7.1.3 Product lifecycle:** zero to one, growth, maturity, sunset; what changes in each stage
- **7.1.4 Product principles and vision:** writing a vision, principles that settle debates, team missions
- **7.1.5 Product ops and the PM toolkit:** roadmapping tools, feedback systems, research repositories, analytics, project tools (Jira, Linear, Notion, Productboard)

*Learn from:* Inspired, Empowered and Transformed (Marty Cagan), The Lean Startup, Lenny's Newsletter archive, Shreyas Doshi and Ken Norton essays, Product Management in Practice.

### Module 7.2 Discovery

*Prove-it: take a vague problem and, in two weeks, produce validated evidence for or against building a solution.*

- **7.2.1 Problem framing:** problem statements, customer segments, pain severity and frequency, existing alternatives
- **7.2.2 Opportunity mapping:** opportunity solution trees, assumption mapping, riskiest assumption testing (desirability, viability, feasibility, usability, ethics)
- **7.2.3 Cheap validation:** fake door and painted door tests, concierge MVPs, wizard-of-oz, landing pages, prototypes, pre-sales, letters of intent
- **7.2.4 Prototyping:** paper, Figma, coded prototypes with AI tools, clickable demos, prototype fidelity choices
- **7.2.5 Product-market fit:** signals and measures (retention curves, Sean Ellis test, organic growth), segment-level fit, fit decay
- **7.2.6 Discovery in AI products:** feasibility probing with real model outputs, data availability checks, quality thresholds before commitment, cost modelling in discovery

### Module 7.3 Strategy

*Depth target: L4. Prove-it: write a two-page product strategy with a diagnosis, guiding policy and coherent actions, and defend it.*

- **7.3.1 Strategy fundamentals:** diagnosis, guiding policy, coherent action (Rumelt), strategy vs plan vs goals, choosing what not to do
- **7.3.2 Competitive analysis:** competitor mapping, feature vs positioning comparison, win-loss analysis, substitutes and non-consumption
- **7.3.3 Sources of advantage:** Seven Powers, network effects, scale economies, switching costs, data advantages, distribution, brand, workflow lock-in, counter-positioning
- **7.3.4 Positioning:** April Dunford's framework, category design, differentiated value, proof points
- **7.3.5 Market dynamics:** disruption theory, technology adoption curve and chasm, platform shifts, bundling and unbundling, commoditisation of components
- **7.3.6 Strategic tools:** Wardley maps, Porter's five forces, jobs maps, scenario planning, SWOT limits, North Star and bets framework
- **7.3.7 Platform and ecosystem strategy:** two-sided markets, marketplaces, API ecosystems, partner strategy, co-opetition
- **7.3.8 Portfolio and bets:** horizons model, explore vs exploit, kill criteria, resource allocation

*Learn from:* Good Strategy Bad Strategy (Rumelt), 7 Powers (Hamilton Helmer), Playing to Win, Obviously Awesome (Dunford), Crossing the Chasm, The Innovator's Dilemma, Platform Revolution.

### Module 7.4 Roadmaps and prioritisation

- **7.4.1 Roadmap forms:** now-next-later, outcome roadmaps, themes, release plans, roadmap as communication tool
- **7.4.2 Prioritisation frameworks:** RICE, ICE, Kano, MoSCoW, WSJF, opportunity scoring, cost of delay, value vs effort and their weaknesses
- **7.4.3 Judgement over formulae:** strategy-driven trade-offs, sequencing, dependencies, capacity and slack
- **7.4.4 Saying no:** communicating trade-offs, managing the feature request firehose, executive requests, sales-driven roadmaps
- **7.4.5 Alignment:** stakeholder mapping, pre-wiring decisions, roadmap reviews, handling disagreement
- **7.4.6 Roadmapping under AI uncertainty:** capability-dependent bets, planning for model improvements, option-value investments, kill and pivot criteria

### Module 7.5 Specifications and execution

- **7.5.1 Writing:** PRDs, one-pagers, six-page narratives, PR/FAQ working-backwards documents, user stories, acceptance criteria, edge-case enumeration
- **7.5.2 AI-era specs:** behaviour specifications, eval-defined acceptance criteria, example-driven specs, prompt-as-spec, rubrics, failure-mode catalogues
- **7.5.3 Delivery methods:** Scrum, Kanban, Shape Up, dual-track agile, sprint rituals, cycle time
- **7.5.4 Launch management:** launch tiers, readiness checklists, beta programmes, staged rollouts, kill switches, post-launch reviews
- **7.5.5 Cross-functional leadership:** influence without authority, running effective meetings, decision logs (DACI, RAPID), dependency management, escalation
- **7.5.6 Risk management:** pre-mortems, risk registers, rollback plans, dark launches
- **7.5.7 Quality bar and craft:** defining done, polish vs speed, taste, product reviews

### Module 7.6 Design and UX collaboration

- **7.6.1 UX fundamentals:** usability heuristics, information architecture, interaction patterns, affordances, cognitive load, Hick and Fitts laws
- **7.6.2 Design process and artefacts:** user flows, wireframes, prototypes, design critique, design systems, component libraries
- **7.6.3 Visual and content design basics:** hierarchy, typography, colour, spacing, microcopy, tone of voice, empty states and error states
- **7.6.4 Accessibility and inclusion:** WCAG, assistive technologies, inclusive design, localisation and internationalisation
- **7.6.5 Working with designers:** briefs, feedback that helps, trade-offs between speed and polish, design in the age of AI prototyping

### Module 7.7 Growth and lifecycle

- **7.7.1 Growth models:** loops vs funnels, product-led growth, sales-led growth, hybrid motions, virality coefficients, referral design
- **7.7.2 Activation and onboarding:** aha moments, time-to-value, onboarding patterns, checklists, templates, sample data, progressive disclosure
- **7.7.3 Engagement and retention:** habit formation, notification design, resurrection campaigns, cohort analysis, value-based engagement vs dark patterns
- **7.7.4 Monetisation:** free trials, freemium, reverse trials, paywalls, upgrade triggers, expansion revenue, churn reduction
- **7.7.5 Lifecycle messaging:** email, in-app, push, segmentation, personalisation, deliverability

### Module 7.8 Go-to-market

- **7.8.1 Customer definition:** ICP, personas, buyer vs user vs champion vs blocker, segmentation
- **7.8.2 Messaging and launch:** value propositions, narrative, launch tiers, press, analyst relations, content and community
- **7.8.3 Pricing and packaging:** value metrics, per-seat vs usage vs outcome-based vs hybrid, tiers, add-ons, enterprise contracts, discounting, AI cost pass-through
- **7.8.4 Sales partnership:** sales enablement, demos, proof-of-concept design, objection handling, competitive battlecards, deal desk basics
- **7.8.5 Channels and partners:** resellers, marketplaces (AWS, Azure, Google), system integrators, ISVs, technology partnerships
- **7.8.6 Developer and community go-to-market:** developer relations, documentation as marketing, open-source strategy, hackathons, ambassadors

*Learn from:* Obviously Awesome, Crossing the Chasm, Monetizing Innovation (Madhavan Ramanujam), Product-Led Growth (Wes Bush), Elena Verna and Reforge material.

### Module 7.9 B2B SaaS and enterprise products

- **7.9.1 Buying process:** buying committees, procurement, legal review, security review, pilot to production, budget cycles
- **7.9.2 Enterprise requirements:** admin consoles, audit logs, SSO and SCIM, RBAC, data export, SLAs, support tiers, uptime commitments
- **7.9.3 Customer success:** onboarding, adoption plans, health scores, QBRs, renewals and expansion, churn post-mortems
- **7.9.4 Customer advisory and co-development:** design partners, advisory boards, managing custom requests without becoming a services firm
- **7.9.5 Integrations strategy:** native vs partner vs API, marketplace ecosystems, integration quality bar
- **7.9.6 Vertical SaaS:** workflow depth, regulation, data network effects, domain expertise as moat

### Module 7.10 Platform, API and developer products

- **7.10.1 Developer experience:** time to first call, docs quality, SDKs, error messages, sandboxes
- **7.10.2 Platform governance:** versioning, deprecation, quotas, abuse, terms of service
- **7.10.3 Ecosystem growth:** marketplaces, app review, revenue sharing, developer support
- **7.10.4 Platform metrics:** active developers, integration depth, time to production, API reliability

### Module 7.11 Product finance

- **7.11.1 Financial statements:** P&L, balance sheet, cash flow, reading a public company filing
- **7.11.2 SaaS metrics:** ARR, MRR, NRR, GRR, ACV, CAC payback, magic number, burn multiple, Rule of 40, gross margin
- **7.11.3 AI economics:** inference COGS, margin compression and expansion, usage-based revenue variability, pricing against falling model prices
- **7.11.4 Budgeting and headcount:** cost per engineer, team sizing, ROI cases, prioritising under budget
- **7.11.5 Funding and valuation literacy:** fundraising stages, cap tables, dilution, valuation multiples, board reporting

### Module 7.12 Careers and the PM ladder

- **7.12.1 Levels:** APM, PM, senior PM, staff and principal PM, group PM, director, VP, CPO; what scope and expectations change
- **7.12.2 Hiring and interviewing:** product sense, execution, strategy, analytics, technical, behavioural and AI-specific interviews; case frameworks and their limits; take-home exercises
- **7.12.3 Portfolio and evidence:** shipped products, metrics, write-ups, prototypes, public work
- **7.12.4 Role variants:** AI PM, technical PM, platform PM, growth PM, data PM, forward-deployed PM, founder-PM
- **7.12.5 Negotiating roles and compensation:** leverage, equity basics, offers, remote work across countries

### Module 7.13 Decision-making and mental models

- **7.13.1 Thinking tools:** first principles, inversion, second-order effects, opportunity cost, base rates, Fermi estimation, probabilistic thinking
- **7.13.2 Decision hygiene:** decision journals, pre-mortems, premortem vs post-mortem, one-way and two-way doors, disagree-and-commit, red teams
- **7.13.3 Cognitive biases in product work:** confirmation, sunk cost, anchoring, survivorship, HiPPO, planning fallacy, IKEA effect
- **7.13.4 Reading:** Thinking Fast and Slow, Thinking in Bets, Superforecasting, Noise, The Art of Thinking Clearly, Poor Charlie's Almanack

---

## Part 8: AI product craft

This is where the sciences and the engineering turn into products people use, pay for and trust. It is the heart of the AI PM role. Aim for L4 here, with L5 in at least one module.

### Module 8.1 Thinking AI-natively

*Prove-it: take any existing product and write two pages on what it would look like if rebuilt from scratch around current model capabilities, and what would not change.*

- **8.1.1 What AI changes:** probabilistic behaviour instead of deterministic, natural language as interface, generation of artefacts, judgement tasks becoming automatable, near-zero marginal cost of cognition, capability that improves without your effort
- **8.1.2 Feature, product or platform:** AI inside a workflow vs AI as the workflow vs AI as infrastructure for others
- **8.1.3 Augmentation vs automation:** copilot, agent, autopilot; the autonomy ladder and how trust is earned between rungs
- **8.1.4 Capability-dependent strategy:** building for the model that arrives in 12 months, features that get absorbed by models, scaffolding that becomes obsolete, what to build vs what to wait for
- **8.1.5 When not to use AI:** deterministic problems, high-stakes tasks without verification, cases where rules or search suffice, cost-prohibitive tasks
- **8.1.6 Wrapper critique and its answer:** thin wrappers vs workflow depth, distribution, data and trust
- **8.1.7 Jobs and tasks:** decomposing roles into tasks, task-level exposure to automation, redesigning workflows rather than replacing steps

### Module 8.2 Product archetypes

*Study each archetype: what the user job is, the typical architecture, the main failure mode, the key metric, three products to analyse.*

- **8.2.1 Assistants and chat:** general and domain assistants, memory, personas
- **8.2.2 Copilots:** inline suggestions, edit acceptance, latency sensitivity (code, writing, spreadsheets)
- **8.2.3 Agents:** goal-directed multi-step systems; coding agents, research agents, browser and computer-use agents, back-office agents
- **8.2.4 Answer engines and enterprise search:** grounded answers, citations, permissions, freshness
- **8.2.5 Generative creation tools:** images, video, music, design, slides, documents, websites and apps
- **8.2.6 Voice products:** call-centre agents, assistants, translation, dictation, companions
- **8.2.7 Vertical AI:** legal, healthcare, finance, insurance, accounting, construction and others where domain workflow is the product
- **8.2.8 Decision intelligence and analytics agents:** insights, forecasting, anomaly detection, natural-language analytics
- **8.2.9 Recommendation and ranking systems:** personalisation, feeds, marketplaces, ads
- **8.2.10 AI infrastructure and developer tools:** model gateways, eval platforms, vector databases, orchestration, observability, agent runtimes
- **8.2.11 Physical and embodied AI:** robots, vehicles, devices, wearables, industrial inspection
- **8.2.12 Consumer companions and social AI:** engagement dynamics, dependency risks, minors, regulation

### Module 8.3 Designing experiences for AI

*Depth target: L4. Prove-it: redesign one AI feature to handle failure gracefully and measure whether user trust improves.*

- **8.3.1 Input design:** open prompt vs guided input, suggestions and templates, solving the blank-page problem, multimodal inputs, context pickers
- **8.3.2 Setting expectations:** capability disclosure, limitations, examples of good use, onboarding
- **8.3.3 Communicating uncertainty:** confidence cues, citations and sources, quote-linking, abstention, calibrated language
- **8.3.4 Explainability in practice:** showing work, reasoning summaries, provenance, why-this-answer affordances
- **8.3.5 Correction and control:** edit, regenerate, undo, feedback buttons that actually matter, steering, versioning
- **8.3.6 Trust calibration:** avoiding both over-trust and under-trust, reliance patterns, automation bias, verification affordances
- **8.3.7 Latency design:** streaming, progress indicators, background work, perceived speed, long-running task UX
- **8.3.8 Agent UX:** plan preview, step visibility, approval gates, interruption and resumption, notifications, handoff to humans, audit trails, delegating with scoped permissions
- **8.3.9 Generative and adaptive UI:** interfaces composed on demand, canvases and artefacts, structured outputs rendered as components
- **8.3.10 Personality and tone:** brand voice, warmth vs accuracy, sycophancy avoidance, anthropomorphism risks
- **8.3.11 Failure design:** error states, refusals that help, recovery paths, graceful degradation, human escalation
- **8.3.12 Accessibility and inclusion in AI UX:** language coverage, dialects, voice, cognitive accessibility, bias in outputs

*Learn from:* Google People and AI Guidebook, Microsoft Guidelines for Human-AI Interaction, Apple human interface guidance on ML, Anthropic and OpenAI product design writing, Nielsen Norman Group on AI UX.

### Module 8.4 Specifying behaviour and quality

*Depth target: L4 to L5. The new core PM artefact.*

- **8.4.1 Behaviour specifications:** what the system should do, should not do, and should do when unsure; examples of good and bad outputs; tone and format rules
- **8.4.2 Rubrics and quality dimensions:** correctness, completeness, groundedness, helpfulness, safety, style, brevity; weighting by use case
- **8.4.3 Use-case risk tiering:** low-stakes assistance vs high-stakes decisions; matching autonomy and controls to risk
- **8.4.4 Policy design:** content policies, refusal rules, escalation rules, domain-specific restrictions, regional variations
- **8.4.5 Writing eval-ready requirements:** turning a requirement into a measurable test with examples and thresholds
- **8.4.6 Failure taxonomies:** catalogue of how your product fails, with severity and frequency, driving the roadmap
- **8.4.7 Working with domain experts:** getting expert judgement into rubrics, expert review loops, disagreement handling

### Module 8.5 The AI product development lifecycle

*Prove-it: run the full loop below on one real use case and document each gate.*

- **8.5.1 Opportunity and feasibility:** user job, data availability, quality needed vs achievable, cost sketch, risk tier
- **8.5.2 Rapid prototyping:** prompt prototypes, real model outputs on real data, Wizard-of-Oz, shareable demos, failure-first testing
- **8.5.3 Building the first eval set:** 30 to 100 real examples, labelled by experts, covering the hard cases
- **8.5.4 Iteration loop:** change one thing, run evals, read traces, update the failure taxonomy, repeat
- **8.5.5 Dogfooding and private beta:** instrumenting usage, capturing failures, structured feedback, shadow mode
- **8.5.6 Launch gates:** quality thresholds by risk tier, safety review, cost review, support readiness, rollback plan
- **8.5.7 Post-launch learning:** monitoring, sampling traces weekly, user feedback triage, drift detection, cost drift
- **8.5.8 Data flywheel design:** capturing signals, consent, converting production data into evals and training data safely
- **8.5.9 Model upgrades:** regression testing on new versions, staged migration, prompts that rot, deprecation schedules
- **8.5.10 Sunsetting and rebuilding:** scaffolding made obsolete by better models, removing complexity

### Module 8.6 Human-AI collaboration and change management

- **8.6.1 Task decomposition:** what humans keep, what AI does, what is jointly done
- **8.6.2 Human-in-the-loop design:** review burden, sampling-based review, escalation triggers, avoiding rubber-stamping
- **8.6.3 Measuring value:** time saved, quality improvements, throughput, error reduction, revenue influenced, controlled comparisons rather than self-reports
- **8.6.4 Adoption:** training, champions, workflow integration, resistance and incentives, role redesign
- **8.6.5 Productivity paradoxes:** time saved not translated into value, verification overhead, skill atrophy, quality dilution
- **8.6.6 Organisational change:** process redesign, governance, new roles, union and workforce considerations

### Module 8.7 AI business models, pricing and unit economics

*Depth target: L4. Prove-it: build a unit-economics model with token costs, caching, routing and three pricing options, and show the break-even and margin under heavy use.*

- **8.7.1 Cost structure:** inference, retrieval, tool calls, human review, data, hosting, support; cost per task and per user
- **8.7.2 Price trends:** falling cost per token, rising consumption per task (agents, reasoning), net effect on margins
- **8.7.3 Pricing models:** per seat, usage-based, credits, outcome-based, hybrid, tiering by model or capability, enterprise commits
- **8.7.4 Margin management:** routing, caching, distillation, rate limits, fair-use policies, heavy-user economics
- **8.7.5 Pricing psychology and packaging:** anchoring, good-better-best, free tier design, AI add-on vs bundled
- **8.7.6 Competing with model providers:** where providers move up the stack, where they cannot go, partnership vs competition
- **8.7.7 Revenue quality:** retention of AI-driven revenue, experimentation spend vs production spend, pilot-to-production conversion

### Module 8.8 Data strategy and moats in AI

*Depth target: L4.*

- **8.8.1 Moat types:** proprietary data, workflow integration and systems of record, distribution, network effects, brand and trust, domain expertise, evals and feedback loops, speed of iteration, regulatory and compliance posture
- **8.8.2 Data flywheels and when they are real:** feedback that improves quality vs vanity data accumulation
- **8.8.3 Data rights:** customer data usage terms, opt-in training, aggregation rights, anonymisation, data partnerships and licensing
- **8.8.4 Context as a moat:** integrations, user memory, organisational knowledge graphs
- **8.8.5 What is not a moat:** prompts, thin wrappers, access to a model everyone has
- **8.8.6 Defensibility analysis exercise:** score ten products on each moat type

### Module 8.9 Model and vendor strategy

- **8.9.1 Selection:** quality, latency, cost, context length, tool use, multimodality, safety behaviour, data policies, regional availability, SLAs
- **8.9.2 Multi-model architectures:** routing, cascades, fallbacks, abstraction layers, portability costs
- **8.9.3 Open vs closed:** control, cost at scale, privacy, customisation, support, compliance; self-hosting break-even analysis
- **8.9.4 Vendor management:** commit contracts, rate limits, capacity guarantees, price protection, exit plans, concentration risk
- **8.9.5 Training your own model:** the narrow cases where it makes sense, post-training vs pretraining, cost and team requirements

### Module 8.10 AI product teams and operating rhythm

- **8.10.1 Roles:** AI PM, AI engineer, ML engineer, data scientist, applied scientist, research scientist, eval engineer, data annotator and domain expert, AI designer, trust and safety lead, solutions or forward-deployed engineer
- **8.10.2 Team topologies:** embedded vs platform AI teams, centres of excellence, research-to-product handoffs
- **8.10.3 Rituals:** weekly trace-reading sessions, error-analysis workshops, eval reviews, model-upgrade reviews, red-team days
- **8.10.4 Working with research:** translating product needs into research asks, assessing readiness, managing research uncertainty
- **8.10.5 Tooling and infrastructure choices:** build vs buy for eval, observability, labelling and gateway tools
- **8.10.6 Hiring and developing AI talent:** interview loops, evaluating AI PM candidates, growth paths

### Module 8.11 Selling and scaling AI to customers

- **8.11.1 Enterprise adoption reality:** why pilots stall, proof-of-value design, success criteria agreed up front
- **8.11.2 Objection handling:** accuracy, security, privacy, hallucination, liability, job fears, vendor stability
- **8.11.3 Services-led and forward-deployed models:** embedding engineers with customers, productising repeated work
- **8.11.4 Competing with incumbents:** distribution advantages of incumbents, speed and focus of startups, bundling threat
- **8.11.5 Customer education:** use-case libraries, playbooks, champion programmes, community
- **8.11.6 Avoiding AI-washing:** honest claims, substantiation, regulatory scrutiny of AI marketing claims

### Module 8.12 Case library and analysis template

*Analyse each case with the same template: user job, product form, model strategy, data and moat, pricing, evals and quality approach, safety approach, growth motion, what would you do next.*

- **8.12.1 Coding:** Cursor, Claude Code, GitHub Copilot, Replit, Lovable, Cognition
- **8.12.2 Knowledge and search:** Perplexity, Glean, NotebookLM, ChatGPT search
- **8.12.3 Vertical:** Harvey, Abridge, OpenEvidence, EvenUp, Hebbia, Sierra, Decagon, Clay
- **8.12.4 Creative:** Midjourney, Runway, ElevenLabs, Suno, Canva AI, Figma AI
- **8.12.5 Work suites:** Microsoft Copilot, Notion AI, Google Workspace with Gemini, Slack AI, Granola
- **8.12.6 Platforms:** OpenAI platform, Anthropic API and Claude apps, Google Vertex AI, AWS Bedrock, Hugging Face, Databricks Mosaic
- **8.12.7 Failures and cautionary tales:** products rolled back, lawsuits, hallucination incidents, chatbot liability cases, AI-washing enforcement

---

## Part 9: Domains and verticals

For each domain, learn: the core workflows, the data and systems involved, the regulation, where AI creates value today, where it fails dangerously, the metrics that matter, and the companies to study. Pick two or three domains to take to L4, and keep the rest at L2.

### Module 9.1 Financial services and banking

- **9.1.1 Structure of the industry:** retail, commercial and corporate banking, wealth, capital markets, insurance, payments, fintech, how banks make money
- **9.1.2 Core systems and data:** core banking, ledgers, card processors, CRM, data warehouses, market data, KYC data, bureau data, document stores
- **9.1.3 Payments and rails:** cards (networks, issuing, acquiring), UPI, IMPS, NEFT and RTGS, SWIFT, ACH, SEPA, real-time payments, settlement and reconciliation
- **9.1.4 Credit:** underwriting, scorecards, alternative data, collections, early warning signals, loan lifecycle, regulatory capital basics
- **9.1.5 Fraud and financial crime:** fraud types, rules and ML detection, graph-based detection, AML transaction monitoring, KYC and onboarding, sanctions screening, investigator workflows, false-positive economics
- **9.1.6 Relationship management and commercial banking:** account planning, prospecting, intelligence on clients, event and trigger signals, cross-sell, credit-and-relationship workflows
- **9.1.7 Wealth and capital markets:** research, portfolio construction, advisory, compliance surveillance, trade operations
- **9.1.8 Insurance:** underwriting, claims, actuarial models, fraud, distribution
- **9.1.9 Regulation and model risk:** Basel framework basics, model risk management (for example SR 11-7 in the US), explainability and fair-lending rules, RBI guidance including its AI framework work, SEBI rules, EU banking supervision, audit trails, outsourcing and third-party risk rules
- **9.1.10 Open finance:** open banking, Account Aggregator framework in India, data sharing, consent
- **9.1.11 AI use cases and risks:** document processing, customer service, copilots for bankers, research summarisation, code modernisation, fraud and AML triage, credit decision support; hallucination, bias, explainability, data leakage and supervisory expectations
- **9.1.12 Metrics:** loss rates, false-positive rates, time to decision, cost to serve, RM productivity, NPS, regulatory findings

### Module 9.2 Sales, CRM and revenue technology

- **9.2.1 Systems:** CRM (Salesforce, HubSpot, Zoho), sales engagement, data enrichment, intent data, conversation intelligence, CPQ
- **9.2.2 Workflows:** prospecting, qualification, outreach, discovery, demos, proposals, negotiation, renewal, account planning
- **9.2.3 AI patterns:** lead scoring, account research agents, outbound personalisation, call summarisation and coaching, forecasting, CRM hygiene automation, AI SDRs, voice calling agents
- **9.2.4 Data and compliance:** contact-data sourcing, consent, email and calling regulations (GDPR, CAN-SPAM, TCPA, DND rules), deliverability
- **9.2.5 Metrics:** pipeline created, conversion rates, cycle length, rep productivity, win rate, quota attainment

### Module 9.3 Customer support and experience

- **9.3.1 Workflows:** ticket triage, agent assist, self-service, escalation, quality assurance, knowledge management
- **9.3.2 AI patterns:** chat and voice agents, deflection with quality, summarisation, auto-resolution, sentiment analysis, QA scoring
- **9.3.3 Risks and measures:** containment vs satisfaction, hallucinated policies, brand risk, CSAT, first-contact resolution, cost per resolution

### Module 9.4 Software development and developer tools

- **9.4.1 Workflows:** planning, coding, review, testing, deployment, operations, incident response, documentation, migration
- **9.4.2 AI patterns:** completion, chat, agentic coding, test generation, code review, migration and modernisation, SRE agents, security fixing
- **9.4.3 Measures:** acceptance rate, merged-PR quality, cycle time, defect escape rate, developer satisfaction, long-term maintainability

### Module 9.5 Legal and professional services

- **9.5.1 Workflows:** contract review, due diligence, research, drafting, e-discovery, compliance monitoring, audit, tax
- **9.5.2 Risks:** fabricated citations, privilege and confidentiality, unauthorised practice of law, professional-responsibility rules
- **9.5.3 Measures:** accuracy against expert review, time saved, risk missed

### Module 9.6 Healthcare and life sciences

- **9.6.1 Structure:** providers, payers, pharma, devices, public health; EHR systems, claims, clinical workflows
- **9.6.2 AI patterns:** ambient documentation, coding and billing, prior authorisation, clinical decision support, imaging, drug discovery, trial matching, patient engagement
- **9.6.3 Regulation:** HIPAA, FDA software-as-a-medical-device pathways, EU MDR, clinical validation, bias and safety evidence, liability
- **9.6.4 Constraints:** patient safety, data sensitivity, workflow fit, reimbursement

### Module 9.7 Education and learning

- **9.7.1 Patterns:** tutoring, feedback, content generation, assessment, language learning, administrative automation
- **9.7.2 Risks and evidence:** learning outcomes vs answer-giving, academic integrity, minors' privacy, equity

### Module 9.8 Marketing, media and creative work

- **9.8.1 Patterns:** content generation, personalisation, creative testing, SEO changes under answer engines, localisation, asset management
- **9.8.2 Constraints:** brand safety, copyright and likeness, disclosure rules, authenticity

### Module 9.9 HR, recruiting and workforce

- **9.9.1 Patterns:** sourcing, screening, interviewing assistance, onboarding, learning, internal mobility, helpdesks
- **9.9.2 Risks:** discrimination, regulated automated-decision rules, transparency obligations, candidate experience

### Module 9.10 Operations, supply chain and industry

- **9.10.1 Patterns:** demand forecasting, route and inventory optimisation, predictive maintenance, quality inspection, procurement automation, digital twins
- **9.10.2 Realities:** data quality, integration with legacy systems, safety-critical constraints, edge deployment

### Module 9.11 Government and public sector

- **9.11.1 Patterns:** citizen services, document processing, translation, fraud detection, planning and analytics
- **9.11.2 Constraints:** procurement cycles, transparency and due-process rules, sovereignty, language inclusion, public trust

### Module 9.12 Science, research and discovery

- **9.12.1 Landmarks:** AlphaFold, materials discovery, weather models, mathematical proof assistance, lab automation, AI co-scientist systems
- **9.12.2 Patterns:** literature synthesis, hypothesis generation, simulation surrogates, experiment planning
- **9.12.3 Limits:** validation bottlenecks, reproducibility, overclaiming

### Module 9.13 Robotics and physical AI

- **9.13.1 Stack:** perception, planning, control, simulation, teleoperation data, vision-language-action models, hardware economics
- **9.13.2 Applications:** warehouses, manufacturing, autonomous vehicles, drones, humanoids, surgical robotics
- **9.13.3 Constraints:** safety certification, edge compute, data scarcity, unit economics

### Module 9.14 Consumer, entertainment and gaming

- **9.14.1 Patterns:** companions, creative tools, games with generative content, personalised media, shopping assistants
- **9.14.2 Risks:** engagement optimisation, dependency, minors, deepfakes and likeness rights

---

## Part 10: Safety, security, ethics, law and governance

This is the part that increasingly decides which AI products survive. The top 0.1% can talk about it with lawyers, security teams and regulators as comfortably as with engineers.

### Module 10.1 Responsible AI foundations

- **10.1.1 Core principles:** fairness, transparency, explainability, accountability, privacy, safety, human oversight, robustness
- **10.1.2 Fairness:** bias sources (data, labels, models, deployment), group and individual fairness metrics and their incompatibilities, disparate impact testing, mitigation methods
- **10.1.3 Explainability:** local and global methods (SHAP, LIME, counterfactuals), why LLM explanations can mislead, regulatory expectations
- **10.1.4 Documentation:** model cards, system cards, data sheets, impact assessments, algorithmic audits
- **10.1.5 Harm taxonomies:** representational, allocative, privacy, security, psychological, societal, environmental
- **10.1.6 Incident learning:** AI incident databases, post-mortem practice, disclosure norms

### Module 10.2 Safety engineering for AI products

- **10.2.1 Risk assessment:** use-case risk tiering, hazard analysis, severity-likelihood scoring, safety cases
- **10.2.2 Content and behaviour policy:** harmful content categories, dual-use topics, child safety, self-harm and crisis handling, hate and harassment, sexual content, election and political content, medical, legal and financial advice
- **10.2.3 Red teaming:** scoping, attack taxonomies, manual and automated red teaming, severity scoring, fix verification
- **10.2.4 Trust and safety operations:** abuse monitoring, enforcement, appeals, human reviewers and their welfare, escalation to law enforcement
- **10.2.5 Vulnerable users and minors:** age assurance, protective defaults, parental controls, mental-health safeguards
- **10.2.6 Behavioural risks:** sycophancy, emotional dependence, manipulation, over-reliance, anthropomorphism
- **10.2.7 Frontier risk frameworks:** capability thresholds, responsible scaling policies, preparedness frameworks, third-party evaluators and government institutes

### Module 10.3 Security of AI systems

*Depth target: L4. Prove-it: threat-model an agent with email and file access, list the attacks, and rank the mitigations.*

- **10.3.1 Prompt injection:** direct, indirect (documents, web pages, emails, tool results), multimodal injection, why it is hard, instruction hierarchy, spotlighting and isolation, design assuming compromise
- **10.3.2 The lethal trifecta pattern:** private data access plus untrusted content plus an exfiltration channel; designing to break at least one leg
- **10.3.3 Agent-specific attacks:** tool poisoning, malicious MCP servers, confused deputy, privilege escalation through tools, memory poisoning, cross-agent attacks, supply-chain attacks via plugins and skills
- **10.3.4 Data and model attacks:** training-data poisoning, backdoors and sleeper behaviours, model extraction and theft, membership inference, model inversion, embedding leakage
- **10.3.5 Jailbreaks:** categories, transferability, automated attack generation, defence limits, classifier-based protections
- **10.3.6 Abuse and cost attacks:** denial of wallet, scraping, account farming, spam and fraud using your product
- **10.3.7 Infrastructure for AI security:** sandboxing, network egress controls, secrets isolation, scoped credentials, logging, anomaly detection
- **10.3.8 Frameworks:** OWASP Top 10 for LLM Applications, MITRE ATLAS, NIST adversarial ML taxonomy, Google SAIF, CSA AI controls
- **10.3.9 AI for security:** defensive agents, vulnerability discovery, SOC automation, dual-use risks of offensive capability

### Module 10.4 Privacy and data protection

- **10.4.1 Regimes:** GDPR, UK GDPR, CCPA and CPRA, HIPAA, India's DPDP Act and rules, Brazil LGPD, PIPL in China, sector-specific rules
- **10.4.2 Core concepts:** lawful basis, consent, purpose limitation, data minimisation, retention, data subject rights, controllers vs processors, DPIAs, cross-border transfers
- **10.4.3 AI-specific tensions:** training on personal data, rights to erasure vs trained models, memorisation and leakage, inference of sensitive attributes, automated decision-making rules
- **10.4.4 Privacy-enhancing technologies:** differential privacy, federated learning, secure multi-party computation, homomorphic encryption (limits), trusted execution environments and confidential computing, on-device processing
- **10.4.5 Operational privacy:** logging policies, redaction, zero data retention, tenant data isolation, vendor and sub-processor management

### Module 10.5 AI regulation and standards

*Regulation moves quickly. For every item below, check the current status and dates before relying on your memory.*

- **10.5.1 EU AI Act:** risk tiers (prohibited, high-risk, limited-risk transparency, minimal), obligations for providers and deployers, general-purpose AI model obligations and systemic-risk models, conformity assessment, timelines and phased application, enforcement and penalties, interaction with GDPR
- **10.5.2 United States:** federal executive and agency actions, NIST AI Risk Management Framework, state laws (for example Colorado, California, Texas, Utah and others), sector regulators (FTC, CFPB, EEOC, FDA, SEC), litigation as de facto regulation
- **10.5.3 United Kingdom:** pro-innovation approach, AI Security Institute, regulator-led model
- **10.5.4 India:** DPDP Act and rules, IT Act and intermediary rules, national AI governance guidance, RBI and SEBI expectations for AI in finance, IndiaAI Mission
- **10.5.5 China:** generative AI measures, algorithm registration, labelling rules
- **10.5.6 Other jurisdictions:** Singapore, Japan, South Korea, Canada, Brazil, UAE and Saudi Arabia, multilateral efforts (OECD, G7 Hiroshima process, UN, Council of Europe convention)
- **10.5.7 Standards:** ISO/IEC 42001 (AI management system), ISO/IEC 23894 (risk), ISO/IEC 27001, NIST frameworks, IEEE standards, industry codes of practice
- **10.5.8 Sector rules touching AI:** model risk management in banking, medical device regulation, employment law on automated decisions, consumer protection, advertising standards
- **10.5.9 Reading regulation as a PM:** extracting product requirements, building a compliance matrix, working with counsel

### Module 10.6 Intellectual property and commercial law

- **10.6.1 Copyright and training:** fair use and text-and-data-mining exceptions, major litigation outcomes and settlements, licensing deals, opt-out mechanisms
- **10.6.2 Output questions:** ownership of generated content, copyrightability, infringement risk, indemnities offered by vendors
- **10.6.3 Other IP:** trademarks, trade secrets and employee use of AI tools, patents on AI inventions, open-source licence compliance
- **10.6.4 Contracts:** terms of service, data-use and training clauses, SLAs, limitation of liability, indemnification, acceptable-use policies, enterprise agreements, DPAs
- **10.6.5 Liability:** product liability and AI, professional liability, defamation by model output, agentic transactions and authority, consumer protection
- **10.6.6 Publicity and likeness:** voice and image rights, deepfake laws, consent

### Module 10.7 Governance inside organisations

- **10.7.1 Policy and structure:** AI use policy, review boards, accountable executives, three lines of defence
- **10.7.2 Inventory and risk register:** every AI system, owner, data, risk tier, controls
- **10.7.3 Lifecycle controls:** design reviews, pre-launch approvals, monitoring requirements, change management, retirement
- **10.7.4 Third-party risk:** vendor due diligence, model provider terms, audit rights, concentration risk
- **10.7.5 Audit and assurance:** internal audit, external audits, evidence collection, certification
- **10.7.6 Culture:** speaking-up channels, incentives, balancing speed with safety

### Module 10.8 Ethics and philosophy

- **10.8.1 Ethical frameworks:** consequentialism, deontology, virtue ethics, contractualism, care ethics, applying them to concrete product dilemmas
- **10.8.2 Core issues:** autonomy and manipulation, consent, power concentration, surveillance, labour displacement, creator rights, global inequity and language inclusion
- **10.8.3 Value alignment questions:** whose values, how to specify them, pluralism, cultural variation in norms
- **10.8.4 Moral status debates:** machine consciousness arguments, model welfare research, precautionary approaches

### Module 10.9 Societal and environmental impact

- **10.9.1 Energy and water:** data-centre growth, training vs inference energy, grid constraints, efficiency trends, carbon accounting
- **10.9.2 Labour and economy:** task exposure studies, productivity evidence, wage and inequality effects, transition policy proposals
- **10.9.3 Information ecosystem:** misinformation, synthetic media, trust in institutions, provenance, elections
- **10.9.4 Education and cognition:** learning effects, skill atrophy, equity of access
- **10.9.5 Concentration and geopolitics:** compute concentration, export controls, sovereign AI, open-source as a counterweight

---

## Part 11: The AI industry and the world around it

The top 0.1% can place any news item in context: who benefits, what it depends on, what it changes. This part builds that map. Details change monthly, so treat every list here as a starting frame and refresh it from current sources.

### Module 11.1 History and milestones

*Prove-it: draw a one-page timeline from 1950 to today with the three ideas that mattered at each stage.*

- **11.1.1 Early AI:** Turing and the imitation game, Dartmouth workshop, perceptron, ELIZA, symbolic AI and expert systems, the two AI winters and what caused them
- **11.1.2 Statistical era:** support vector machines, probabilistic models, IBM Watson, Deep Blue, data and compute growth
- **11.1.3 Deep learning breakthrough:** ImageNet and AlexNet (2012), word2vec, GANs, sequence-to-sequence and attention, AlphaGo
- **11.1.4 Transformer era:** Attention Is All You Need (2017), BERT and GPT, GPT-2 and GPT-3, scaling laws, AlphaFold, Codex and Copilot, CLIP and DALL-E, Stable Diffusion
- **11.1.5 Assistant era:** InstructGPT and RLHF, ChatGPT (late 2022), GPT-4, Claude, Llama and the open-weight wave, Gemini, mixture-of-experts models, long context, multimodality
- **11.1.6 Reasoning and agent era:** reasoning models (o1-style), DeepSeek-R1 and the efficiency shock, tool use and MCP, coding agents, computer use, long-horizon agents
- **11.1.7 Keeping the timeline current:** add each major release and paper with a one-line significance note

*Learn from:* Genius Makers (Cade Metz), The Master Algorithm, Empire of AI (Karen Hao), Architects of Intelligence (Martin Ford), Our Final Invention (for the safety lineage), computer history museum oral histories.

### Module 11.2 Companies and labs

*Prove-it: for each organisation, write a five-line profile covering model strategy, revenue engine, distribution, compute position and culture.*

- **11.2.1 Frontier labs:** Anthropic, OpenAI, Google DeepMind, Meta, xAI, Microsoft AI, Amazon, Apple
- **11.2.2 Independent and specialist model builders:** Mistral, Cohere, AI21, Reka, Safe Superintelligence, Thinking Machines Lab, Sakana, Black Forest Labs, Stability, Midjourney, Runway, ElevenLabs, Suno
- **11.2.3 China:** DeepSeek, Alibaba (Qwen), Moonshot (Kimi), Zhipu, MiniMax, ByteDance, Tencent, Baidu, and how their strategies differ
- **11.2.4 India and other regions:** Sarvam, Krutrim, Ola and Reliance efforts, Gulf initiatives (G42, Humain), European sovereign efforts, Japan and Korea
- **11.2.5 Infrastructure and tooling companies:** NVIDIA, AMD, Broadcom, TSMC, hyperscalers, CoreWeave and other neoclouds, Databricks, Snowflake, Scale AI and data vendors, Hugging Face, Vercel, Supabase
- **11.2.6 Application leaders:** see Module 8.12
- **11.2.7 Culture and strategy differences:** safety-first vs speed-first vs open-first, consumer vs enterprise focus, research vs product orientation

### Module 11.3 Compute supply chain and energy

- **11.3.1 Chips:** GPUs, TPUs, custom accelerators, memory (HBM), interconnects, why software ecosystems (CUDA) matter
- **11.3.2 Manufacturing:** TSMC and advanced nodes, ASML and EUV lithography, advanced packaging, concentration risk in Taiwan
- **11.3.3 Data centres:** build costs, power density, cooling, siting, construction timelines, hyperscaler capital expenditure
- **11.3.4 Energy:** grid interconnection queues, gas, nuclear (including small modular reactors), renewables, power purchase agreements, local opposition
- **11.3.5 Networking and systems:** InfiniBand vs Ethernet, NVLink, rack-scale systems, optical interconnects
- **11.3.6 Cost curves:** price per FLOP, price per token, capacity constraints, how bottlenecks move (chips, memory, power, transformers, skilled labour)

*Learn from:* Chip War (Chris Miller), SemiAnalysis, Epoch AI data hub, Dwarkesh Patel podcast episodes on compute, Asianometry.

### Module 11.4 Economics and capital markets

- **11.4.1 Funding landscape:** venture rounds, valuations, strategic investments by cloud providers and chipmakers, compute-for-equity deals, circular financing concerns
- **11.4.2 Revenue and margins:** consumer subscriptions, API revenue, enterprise contracts, inference margins, training costs as capital expenditure
- **11.4.3 Public markets:** companies exposed to AI, capex cycles, how analysts model AI demand, bubble arguments and counter-arguments
- **11.4.4 Open-source business models:** open weights as strategy, ecosystem lock-in, licensing
- **11.4.5 M&A and talent markets:** acqui-hires, licensing-and-hire deals, compensation for researchers, non-competes and mobility
- **11.4.6 Macroeconomics of AI:** productivity measurement, adoption curves, diffusion lags, comparisons with electricity, the internet and the railways

### Module 11.5 Geopolitics and public policy

- **11.5.1 United States and China:** competition, export controls on chips and tools, smuggling, chip design restrictions, open-model diplomacy
- **11.5.2 Europe:** regulation-first approach, sovereignty initiatives, competitiveness debates
- **11.5.3 Middle East, India, Southeast Asia, Africa, Latin America:** sovereign AI programmes, data-centre investments, language and cultural inclusion
- **11.5.4 International coordination:** AI summits, safety institutes network, OECD and G7 processes, UN initiatives, standards bodies
- **11.5.5 Military and national-security uses:** intelligence analysis, cyber operations, autonomous weapons debates, defence procurement
- **11.5.6 Compute governance:** thresholds, reporting requirements, know-your-customer for compute, verification proposals

### Module 11.6 India and emerging-market context

- **11.6.1 Digital public infrastructure:** Aadhaar, UPI, Account Aggregator, ONDC, DigiLocker, how DPI shapes AI product opportunities
- **11.6.2 Language and inclusion:** 22 scheduled languages, code-mixing, Bhashini, voice-first usage, low-literacy design
- **11.6.3 Ecosystem:** IndiaAI Mission and compute subsidies, AI startups, IT services firms (TCS, Infosys, Wipro, HCL and others) repositioning, global capability centres, talent pools
- **11.6.4 Market realities:** price sensitivity, mobile-first, trust and fraud, regulatory expectations, enterprise sales cycles
- **11.6.5 Remote work across borders:** time zones, payments, tax and contracting basics, building credibility with US, European and Australian employers

### Module 11.7 Research and open ecosystem

- **11.7.1 Open ecosystem:** Hugging Face, EleutherAI, Allen Institute for AI, academic labs, community benchmarks, open datasets
- **11.7.2 How research flows:** arXiv, conferences and workshops, preprint culture, replication, what peer review does and does not catch
- **11.7.3 Key people to follow and why:** researchers, engineers, safety researchers, economists, policy analysts, investors, journalists; build a balanced list with opposing views
- **11.7.4 Evaluating claims:** red flags (no baselines, cherry-picked demos, unreplicated results, benchmark contamination, marketing language), asking what would change my mind

### Module 11.8 Information diet and sensemaking

*Prove-it: run a 30-minute weekly review that produces a short written summary of what changed and what you would do about it.*

- **11.8.1 Daily and weekly cadence:** lab blogs and release notes, newsletters, one or two podcasts, one paper summary per week, curated social lists, RSS and read-later tools
- **11.8.2 Signal vs noise:** primary sources over commentary, discounting hype and doom equally, tracking claims against outcomes
- **11.8.3 Note-taking and synthesis:** atomic notes, linking, periodic essays, building your own mental model of the industry
- **11.8.4 Staying current on safety and policy:** following policy trackers, legal updates and safety research venues

---

## Part 12: Leadership, communication and career

### Module 12.1 Communication

*Depth target: L4. Prove-it: write a one-page memo that gets a decision, then present it in five minutes to a sceptical audience.*

- **12.1.1 Writing:** clear structure, answer-first writing, memos and narratives, editing ruthlessly, writing for skimmers, technical writing, writing about uncertainty
- **12.1.2 Speaking and presenting:** structuring talks, slides that support rather than replace, storytelling, handling questions, executive presence, virtual presentations
- **12.1.3 Explaining technical ideas:** analogies that hold up, layers of explanation (one sentence, one paragraph, one page), knowing your audience
- **12.1.4 Data storytelling:** choosing the right chart, annotating insight, avoiding misleading visuals
- **12.1.5 Difficult conversations:** feedback (radical candour, SBI model), disagreement, bad news, saying no, repairing trust
- **12.1.6 Meetings and async work:** agendas, decision-oriented meetings, written updates, documentation culture
- **12.1.7 Negotiation:** interests vs positions, BATNA, anchoring, concessions, multi-party negotiation, contracts and deal terms

*Learn from:* On Writing Well, The Pyramid Principle, Crucial Conversations, Never Split the Difference, Difficult Conversations, Radical Candor, Made to Stick, Storytelling with Data.

### Module 12.2 Influence and stakeholder management

- **12.2.1 Mapping stakeholders:** power and interest, formal vs informal influence, incentives, objections
- **12.2.2 Building alignment:** pre-wiring, customer evidence as persuasion, narrative and numbers, decision documents
- **12.2.3 Managing up and across:** executives, engineering and design counterparts, sales and legal, finance, support
- **12.2.4 Conflict and trade-offs:** resolving disagreement between functions, escalation done well, disagree-and-commit
- **12.2.5 Trust:** reliability, transparency, giving credit, owning mistakes

### Module 12.3 Leading people and teams

- **12.3.1 People management basics:** one-on-ones, goal setting, coaching vs directing, delegation, performance feedback, promotion cases
- **12.3.2 Hiring and onboarding:** role design, structured interviews, bias reduction, closing candidates, first-90-days plans
- **12.3.3 Team health:** psychological safety, team agreements, conflict, burnout signals, morale during uncertainty
- **12.3.4 Remote and global teams:** async norms, time-zone design, cross-cultural communication
- **12.3.5 Managing managers and organisation design:** span of control, team topologies, reorganisations, scaling from 10 to 100 to 1,000 people
- **12.3.6 Hard moments:** underperformance, layoffs and restructures, reorganisation communications, crisis leadership

*Learn from:* High Output Management, The Manager's Path, An Elegant Puzzle, Radical Focus, Turn the Ship Around, The Five Dysfunctions of a Team, The Hard Thing About Hard Things.

### Module 12.4 Executive and strategic leadership

- **12.4.1 Operating cadence:** annual and quarterly planning, business reviews, OKR cycles, budget processes
- **12.4.2 P&L and business ownership:** revenue and cost levers, trade-offs between growth and margin, board communication
- **12.4.3 Partnerships and corporate development:** partnership structures, M&A basics, integration challenges
- **12.4.4 Risk and crisis leadership:** incident communication, regulatory inquiries, public relations during AI failures
- **12.4.5 Setting culture and standards:** quality bars, writing and review culture, how leaders shape what teams value
- **12.4.6 Leading through technology shifts:** adapting organisations when capabilities change quarterly, avoiding both panic and complacency

### Module 12.5 Founder and entrepreneurial skills

- **12.5.1 Starting:** idea selection and validation, founder-market fit, picking co-founders, early customers, first prototypes
- **12.5.2 Company building:** incorporation and equity basics, early hiring, pricing and first revenue, sales as a founder, compliance basics
- **12.5.3 Fundraising:** angel and seed rounds, pitch narrative, metrics investors look for, term sheets, SAFEs, cap tables, due diligence
- **12.5.4 AI-startup specifics:** moat questions, dependence on model providers, gross margin scrutiny, distribution, speed vs defensibility, acquisition outcomes
- **12.5.5 Alternative paths:** bootstrapping, consulting and productised services, indie products, open-source businesses, joining early-stage startups
- **12.5.6 Learning from the best:** Y Combinator materials, Paul Graham essays, Sam Altman's startup advice, Lenny's Newsletter, Indie Hackers

### Module 12.6 Personal effectiveness and learning craft

- **12.6.1 Attention and time:** deep work, weekly planning, energy management, say-no policies, meeting hygiene
- **12.6.2 Learning methods:** deliberate practice, spaced repetition, retrieval practice, interleaving, teaching to learn, learning in public, project-based learning
- **12.6.3 Knowledge management:** note systems, personal wiki, reading workflow, capturing ideas, resurfacing
- **12.6.4 Health and sustainability:** sleep, exercise, nutrition, avoiding burnout, long-term consistency
- **12.6.5 Mindset:** curiosity, comfort with ambiguity, resilience, dealing with imposter feelings, receptivity to feedback

### Module 12.7 Authority and career capital

- **12.7.1 Public work:** writing regularly, speaking at meetups and conferences, podcasts and video, open-source contributions, building small public tools
- **12.7.2 Network:** mentors, sponsors, peers, communities, giving before asking, high-signal conversations, cold outreach that gets answers
- **12.7.3 Credentials and proof:** portfolio, case studies with metrics, references, certifications where they carry weight
- **12.7.4 Positioning:** picking a niche where you can be best-known, narrative about your career, differentiating among many AI PMs
- **12.7.5 Global and remote careers:** finding roles, interview processes in different regions, compensation benchmarks, contracts and tax, building trust at a distance
- **12.7.6 Optionality:** financial runway, skill portfolio, reputation, relationships; keeping multiple doors open

### Module 12.8 Integrity and judgement under pressure

- **12.8.1 Shipping under pressure:** distinguishing acceptable risk from unacceptable risk, documenting concerns, escalation paths
- **12.8.2 Honesty in product claims:** accurate marketing, disclosing limits, correcting mistakes publicly
- **12.8.3 Conflicts of interest and confidentiality:** handling competitor information, personal data, insider information
- **12.8.4 Responsible dissent:** raising concerns, whistleblowing norms and protections

---

## Part 13: Frontier and futures

This part trains judgement under deep uncertainty. The goal is not to predict the future but to hold calibrated views, update quickly and make robust decisions.

### Module 13.1 Capability trajectories

- **13.1.1 What is improving fastest:** coding, mathematics, scientific reasoning, tool use, multimodal understanding, long-horizon task completion
- **13.1.2 Measuring autonomy:** task-length measurements, reliability at length, supervision cost
- **13.1.3 What remains hard:** reliability, long-term memory and continual learning, robust planning, grounded physical interaction, calibrated uncertainty, efficient learning from few examples
- **13.1.4 Where progress comes from:** pretraining scale, post-training and reinforcement learning, inference-time compute, data quality and synthetic data, algorithmic efficiency, better scaffolding and tools
- **13.1.5 Bottlenecks:** compute, energy, data, evaluation, human feedback capacity, organisational adoption

### Module 13.2 AGI and superintelligence debates

- **13.2.1 Definitions:** AGI, transformative AI, superintelligence, why definitions drive disagreement
- **13.2.2 Timelines:** forecasting approaches, expert surveys, lab leader statements and incentives, compute-based models, base rates for technology predictions
- **13.2.3 Pathways and takeoff:** scaling continuing, new paradigms needed, recursive self-improvement, fast vs slow takeoff, automated AI research
- **13.2.4 Skeptic positions:** limits of next-token prediction, lack of world models, data walls, diminishing returns, reliability gaps
- **13.2.5 Risk positions:** misalignment, misuse, structural and gradual-disempowerment risks, power concentration, arguments for and against high existential-risk estimates
- **13.2.6 Holding calibrated views:** writing down probabilities, tracking predictions, steelmanning opposing views

*Learn from:* Superintelligence (Nick Bostrom), Human Compatible (Stuart Russell), The Precipice (Toby Ord), Situational Awareness (Leopold Aschenbrenner), AI 2027 scenario, Gary Marcus and Yann LeCun critiques, Dario Amodei essays, Sam Altman essays, Dwarkesh Patel interviews.

### Module 13.3 Economic futures

- **13.3.1 Work and productivity:** task automation vs job replacement, new job creation, wage effects, evidence from early deployments
- **13.3.2 Software abundance:** cheap code, personal software, shrinking build costs, what becomes scarce (distribution, trust, taste, data, regulation)
- **13.3.3 Agent economy:** agents as users and buyers, agent payments and identity, marketplaces for agent services, machine-to-machine commerce
- **13.3.4 Business structure:** small teams with large output, services turning into software, outcome-based business models, changes to consulting, agencies and outsourcing
- **13.3.5 Distribution of gains:** capital vs labour, concentration among compute owners, public policy responses such as retraining, taxation and income support
- **13.3.6 Regional effects:** impact on IT services economies, outsourcing hubs, and developing countries

### Module 13.4 Technology futures

- **13.4.1 Interfaces and devices:** voice and ambient computing, wearables and glasses, personal agents, always-on assistants, privacy trade-offs
- **13.4.2 Robotics and physical AI:** humanoids, general-purpose manipulation, autonomous driving and logistics, cost curves
- **13.4.3 Science acceleration:** biology, materials, climate and energy, mathematics, automated labs
- **13.4.4 Adjacent technologies:** brain-computer interfaces, quantum computing and what it does and does not mean for AI, advanced biotech, fusion and new energy sources
- **13.4.5 New computing substrates:** neuromorphic and photonic computing, analog accelerators, memory-centric architectures

### Module 13.5 Governance futures

- **13.5.1 Coordination models:** treaties, institutions, licensing regimes, liability regimes, auditing and verification
- **13.5.2 Open vs closed:** security implications of open weights, proliferation, benefits of distributed access
- **13.5.3 Rights and status:** debates on AI personhood, model welfare, legal standing for AI systems
- **13.5.4 Democratic and institutional resilience:** deepfakes, persuasion at scale, institutional adaptation, public participation in AI policy

### Module 13.6 Forecasting and scenario craft

*Prove-it: write three dated scenarios for AI in 2030 with signposts, then review them every quarter.*

- **13.6.1 Forecasting skills:** base rates, reference classes, Fermi estimation, calibration training, Brier scores, Metaculus and prediction markets
- **13.6.2 Scenario planning:** driving forces, uncertainty axes, scenario narratives, signposts and trigger points, robust strategies across scenarios
- **13.6.3 Red-teaming your own thesis:** pre-mortems, steelman, seeking disconfirming evidence
- **13.6.4 Communicating uncertainty:** probability ranges, assumptions, what would change your mind

*Learn from:* Superforecasting (Tetlock), The Signal and the Noise, Scenarios: The Art of Strategic Conversation, Thinking in Bets.

### Module 13.7 Philosophy of mind and intelligence

- **13.7.1 What is intelligence:** definitions, general vs narrow, measures of intelligence, Chollet's skill-acquisition efficiency view
- **13.7.2 Understanding debates:** the Chinese Room, stochastic parrots, emergent world models, evidence from interpretability
- **13.7.3 Consciousness and moral status:** global workspace, integrated information, higher-order and illusionist views, behavioural indicators, precautionary principles
- **13.7.4 Reasoning, creativity and judgement:** whether models reason, what originality means, human-AI creative collaboration
- **13.7.5 Embodiment and grounding:** the case for physical interaction and world models

### Module 13.8 Your own strategy in the AI transition

- **13.8.1 Skills that appreciate:** judgement, taste, domain depth, problem selection, systems thinking, evaluation, trust-building, orchestration of agents and people
- **13.8.2 Skills that depreciate:** routine production work, undifferentiated implementation, memorised procedural knowledge
- **13.8.3 Positioning:** being at the interface between capability and real-world need, owning outcomes rather than tasks
- **13.8.4 Resilience:** financial buffers, diverse income, relationships, health, continuous learning habits
- **13.8.5 Yearly strategy review:** what changed in the world, what changed in me, what to double down on, what to drop

---

## Part 14: Tools mastery map

Tools change fast. Learn the category and the underlying concept first; pick one or two tools per category and go deep; revisit the landscape every quarter. For each category the target is L3 (you can choose, set up and critique), with L4 for the ones you use daily.

### Module 14.1 Model access and playgrounds

- **14.1.1 Provider consoles and playgrounds:** Anthropic Console and Workbench, OpenAI Platform and Playground, Google AI Studio and Vertex AI, Mistral La Plateforme, Cohere, xAI API; learn model comparison, parameter effects, system prompts, tool definitions, token and cost views, evaluation tabs
- **14.1.2 Cloud marketplaces:** AWS Bedrock, Azure AI Foundry, Google Vertex AI Model Garden; learn quotas, regional availability, provisioned throughput, enterprise controls
- **14.1.3 Routers and gateways:** OpenRouter, LiteLLM, Portkey, Cloudflare AI Gateway, Vercel AI Gateway; learn fallback, caching, key management, spend controls
- **14.1.4 Consumer apps as research instruments:** Claude, ChatGPT, Gemini, Grok, Perplexity, Meta AI, Copilot; learn to compare features, memory, search, voice, agents, projects, connectors, and to reverse-engineer product decisions

### Module 14.2 Coding and building tools

- **14.2.1 Terminal and desktop agents:** Claude Code, Codex CLI, Gemini CLI, Aider; learn project instruction files, plan mode, permissions, subagents, hooks, custom commands, skills, MCP connections, worktrees, headless mode, running in CI
- **14.2.2 IDEs and extensions:** Cursor, Windsurf, GitHub Copilot, JetBrains AI, Zed, VS Code; learn rules files, codebase indexing, agent modes, review workflows
- **14.2.3 App builders and prototypers:** v0, Lovable, Bolt, Replit Agent, Figma Make, Claude artifacts; learn when they are enough and where they break
- **14.2.4 Notebooks and compute:** Jupyter, Colab, Kaggle, Hex, Modal, RunPod, Lambda, Paperspace
- **14.2.5 Source control and review:** GitHub, GitLab, pull-request workflows, GitHub Actions, code review bots

### Module 14.3 Agent and orchestration frameworks

- **14.3.1 SDKs and frameworks:** Claude Agent SDK, OpenAI Agents SDK, LangGraph, LangChain, LlamaIndex, CrewAI, Pydantic AI, Mastra, Vercel AI SDK, DSPy
- **14.3.2 Durable workflow engines:** Temporal, Inngest, Prefect, Airflow, AWS Step Functions
- **14.3.3 Protocols and standards:** MCP, agent-to-agent protocols, OpenAPI tool definitions, OAuth for agents
- **14.3.4 What to learn:** state management, checkpoints, retries, human approvals, tracing, testing, deployment; and when to skip frameworks entirely

### Module 14.4 Data, retrieval and storage

- **14.4.1 Vector and search:** pgvector, Pinecone, Weaviate, Qdrant, Milvus, Chroma, Elasticsearch, OpenSearch, Turbopuffer, LanceDB
- **14.4.2 Embedding and rerank providers:** Voyage, Cohere, OpenAI, Google, open models via Hugging Face
- **14.4.3 Document processing:** Unstructured, LlamaParse, Docling, Azure Document Intelligence, Textract, Mistral OCR and peers
- **14.4.4 Databases and warehouses:** Postgres, Supabase, Neon, MySQL, MongoDB, Redis, DuckDB, Snowflake, BigQuery, Databricks
- **14.4.5 Data movement and modelling:** dbt, Airbyte, Fivetran, Kafka, Dagster

### Module 14.5 Evaluation, observability and quality

- **14.5.1 Eval platforms:** Braintrust, LangSmith, Langfuse, Arize Phoenix, Weights and Biases Weave, Humanloop successors, Galileo, Patronus
- **14.5.2 Open frameworks:** Promptfoo, Inspect, OpenAI Evals, DeepEval, Ragas, lm-evaluation-harness
- **14.5.3 Monitoring and tracing:** OpenTelemetry, Datadog LLM observability, Sentry, Helicone
- **14.5.4 Labelling and review:** Label Studio, Argilla, Scale AI, Surge AI, internal review tools

### Module 14.6 Training, fine-tuning and serving open models

- **14.6.1 Libraries:** PyTorch, JAX, Hugging Face Transformers, TRL, PEFT, Unsloth, Axolotl, torchtune, DeepSpeed, Megatron
- **14.6.2 Serving:** vLLM, SGLang, TensorRT-LLM, llama.cpp, Ollama, LM Studio, Text Generation Inference
- **14.6.3 Experiment management:** Weights and Biases, MLflow, DVC, Hugging Face Hub
- **14.6.4 Hosted fine-tuning and inference:** provider fine-tuning APIs, Together, Fireworks, Baseten, Replicate, Modal

### Module 14.7 Product, design and collaboration tools

- **14.7.1 Planning:** Jira, Linear, Productboard, Aha, Notion, Confluence, Coda
- **14.7.2 Design and whiteboarding:** Figma, FigJam, Miro, Excalidraw, Framer
- **14.7.3 Analytics and experimentation:** Amplitude, Mixpanel, PostHog, Heap, Pendo, Statsig, Eppo, LaunchDarkly, Optimizely
- **14.7.4 BI and notebooks:** Looker, Tableau, Power BI, Metabase, Hex, Mode
- **14.7.5 Research and feedback:** Dovetail, UserTesting, Maze, Typeform, Gong and Fireflies for call analysis, Intercom and Zendesk data
- **14.7.6 Communication:** Slack, Loom, Granola and other meeting tools, Google Workspace, Microsoft 365

### Module 14.8 Research and learning tools

- **14.8.1 Search and synthesis:** Perplexity, NotebookLM, Elicit, Consensus, Semantic Scholar, Connected Papers, Claude and ChatGPT deep research
- **14.8.2 Reading and notes:** Zotero, Readwise, Obsidian, Notion, Logseq, Anki
- **14.8.3 Paper and news feeds:** arXiv listings, Hugging Face Daily Papers, Alphaxiv, RSS readers, newsletter inboxes

### Module 14.9 Automation and internal tools

- **14.9.1 No-code and low-code:** n8n, Zapier, Make, Retool, Airtable, Pipedream
- **14.9.2 Where they fit:** prototypes, internal automations, glue between SaaS tools; limits at scale

### Module 14.10 Deployment, cloud and security tooling

- **14.10.1 Hosting:** Vercel, Netlify, Cloudflare, Railway, Render, Fly.io, AWS, Google Cloud, Azure
- **14.10.2 Identity and secrets:** Auth0, Clerk, Okta, WorkOS, Supabase Auth, 1Password, Vault
- **14.10.3 Security and compliance:** Snyk, Dependabot, Semgrep, Vanta, Drata, Wiz, Lakera, Protect AI and similar AI-security products

---

## Part 15: Project ladder

Projects are where knowledge becomes skill. Each project has a deliverable. Do them in tier order, but skip around freely. Always write a short public or private write-up: what you built, what failed, what you measured, what you would do next.

### Tier 1: Foundations

- **P1 Model comparison lab:** run 30 prompts across three or more models; record quality, latency, cost; write findings (teaches: model selection, evals instinct)
- **P2 Token and cost calculator:** estimate cost for chat, RAG and agent workloads across providers (teaches: tokens, caching, pricing)
- **P3 Structured extraction pipeline:** extract fields from messy documents into validated JSON with retries (teaches: structured outputs, validation)
- **P4 Streaming chat app:** a small web app with streaming, conversation history and model switching (teaches: API, SSE, state)
- **P5 Tool-using assistant:** three tools, error handling, logging of every tool call (teaches: the tool loop)
- **P6 Semantic search over your notes:** embeddings, vector store, query interface (teaches: embeddings and retrieval basics)

### Tier 2: Core applied skills

- **P7 RAG system on a real corpus:** ingestion, chunking, hybrid retrieval, reranking, citations, separate retrieval and answer metrics (teaches: Module 4.4 end to end)
- **P8 Eval harness from scratch:** dataset, graders, runner, report, regression comparison (teaches: Module 4.8)
- **P9 LLM-as-judge calibration study:** compare judge scores with human labels, measure agreement, fix the rubric (teaches: grader trust)
- **P10 MCP server:** wrap a real API, add auth, write a threat model, publish (teaches: Module 4.3)
- **P11 Text-to-SQL analytics agent:** semantic layer, validation, access control, accuracy tests (teaches: structured data agents)
- **P12 Voice agent:** phone or browser voice conversation with tools and interruption handling; measure latency (teaches: Module 4.11)
- **P13 Document intelligence pipeline:** PDFs with tables and scans to structured data, accuracy by field (teaches: ingestion reality)
- **P14 Guardrails and red-team suite:** 50 attack prompts, automated runs, defence layers, results table (teaches: Modules 4.10 and 10.3)
- **P15 Cost router:** route tasks between cheap and strong models using confidence signals; show cost and quality curve (teaches: Module 4.14)

### Tier 3: Advanced engineering

- **P16 Multi-agent research system:** planner, searchers, writer, critic; trajectory evals; cost and reliability report (teaches: Module 4.5)
- **P17 Coding-agent workflow:** a repeatable setup (instructions file, tests, hooks, subagents) that builds and verifies a feature (teaches: Module 4.12)
- **P18 Fine-tuning experiment:** LoRA fine-tune a small open model on a narrow task and compare with prompting and RAG on cost, latency, quality (teaches: Modules 3.10 and 4.7)
- **P19 Transformer from scratch:** a small GPT trained on a modest dataset, with notes on every component (teaches: Module 3.2)
- **P20 Tokenizer from scratch:** byte-pair encoding implementation and analysis of failure cases (teaches: Module 3.1)
- **P21 Inference optimisation study:** compare FP16, INT8 and INT4 and a serving stack such as vLLM; chart throughput, latency, quality (teaches: Module 3.9)
- **P22 Permission-aware enterprise RAG:** multi-tenant, document-level access control, leakage tests (teaches: Modules 4.4.9 and 4.16)
- **P23 Observability dashboard:** traces, cost, latency, quality scores, alerts for an AI app (teaches: Module 4.9)
- **P24 Experimentation lab:** simulate an A/B test platform, run power calculations, analyse with CUPED and sequential methods (teaches: Module 6.3)

### Tier 4: Product and strategy

- **P25 End-to-end AI product:** discovery, prototype, eval set, beta, launch metrics and a post-launch review for a real use case (teaches: Modules 7 and 8)
- **P26 Pricing and unit-economics model:** spreadsheet with token costs, caching, routing, three price models, break-even and heavy-user analysis (teaches: Module 8.7)
- **P27 Regulatory compliance matrix:** map one product to the EU AI Act, a privacy law and a sector rule (teaches: Module 10.5)
- **P28 Ten-product teardown:** use the Module 8.12 template and publish a comparison (teaches: pattern recognition)
- **P29 Agent threat model:** full STRIDE-style model with mitigations ranked (teaches: Module 10.3)
- **P30 Vertical product concept:** a complete PRD, behaviour spec, eval plan, go-to-market and risk memo for a product in a domain you choose (teaches: Parts 8 and 9)

### Tier 5: Authority

- **P31 Open-source tool:** an eval template, MCP server, dataset or library other people use
- **P32 Public benchmark in a niche:** a well-constructed, documented evaluation for a domain you know
- **P33 Essay series:** 10 long-form pieces on one theme
- **P34 Conference or meetup talk:** with slides and a recording
- **P35 Workshop or course:** teach what you know to 20 or more people
- **P36 Research reproduction:** reproduce a paper result, report where it matched and where it did not

---

## Part 16: Reading and watching library

### Module 16.1 Books

- **16.1.1 AI and ML:** Deep Learning (Goodfellow, Bengio, Courville); Hands-On Machine Learning (Geron); Mathematics for Machine Learning; Probabilistic Machine Learning (Murphy); Reinforcement Learning (Sutton and Barto); AI Engineering (Chip Huyen); Designing Machine Learning Systems (Chip Huyen); Build a Large Language Model From Scratch (Sebastian Raschka); Natural Language Processing with Transformers; The RLHF Book (Nathan Lambert)
- **16.1.2 Engineering and systems:** Designing Data-Intensive Applications; Site Reliability Engineering (Google); The Pragmatic Programmer; A Philosophy of Software Design; Release It!; System Design Interview volumes; Security Engineering (Ross Anderson)
- **16.1.3 Product and strategy:** Inspired; Empowered; Continuous Discovery Habits; The Lean Startup; Good Strategy Bad Strategy; 7 Powers; Obviously Awesome; Crossing the Chasm; The Innovator's Dilemma; Hooked; Monetizing Innovation; The Mom Test; Escaping the Build Trap
- **16.1.4 Data and decisions:** Trustworthy Online Controlled Experiments; Statistical Rethinking; The Book of Why; Thinking, Fast and Slow; Superforecasting; Thinking in Bets; Noise
- **16.1.5 Leadership and communication:** High Output Management; The Manager's Path; An Elegant Puzzle; The Hard Thing About Hard Things; Radical Candor; Crucial Conversations; Never Split the Difference; The Pyramid Principle; On Writing Well
- **16.1.6 AI, society and futures:** Co-Intelligence (Ethan Mollick); Human Compatible; The Alignment Problem; Superintelligence; The Precipice; Chip War; Genius Makers; Empire of AI; Situational Awareness; Power and Prediction; The Coming Wave; The Scaling Era (Dwarkesh Patel)

### Module 16.2 Landmark papers by theme

*Read the abstract, figures and conclusion of each in your first pass; deep-read the starred ones.*

- **16.2.1 Foundations:** Attention Is All You Need\*; BERT; GPT-2 and GPT-3 papers\*; Scaling Laws for Neural Language Models\*; Training Compute-Optimal LLMs (Chinchilla)\*; Llama papers; Mistral 7B; Mixtral
- **16.2.2 Post-training and alignment:** Deep RL from Human Preferences; InstructGPT\*; Constitutional AI\*; DPO\*; PPO; DeepSeekMath (GRPO) and DeepSeek-R1\*; Tulu 3
- **16.2.3 Efficiency and systems:** FlashAttention; LoRA\* and QLoRA; PagedAttention (vLLM)\*; speculative decoding; GPTQ and AWQ; Switch Transformer; ZeRO; Megatron-LM
- **16.2.4 Prompting, reasoning and tools:** Chain-of-Thought prompting\*; Self-Consistency; Tree of Thoughts; ReAct\*; Toolformer; Reflexion; Let's Verify Step by Step; Lost in the Middle
- **16.2.5 Retrieval and memory:** RAG (Lewis et al.)\*; DPR; ColBERT; Self-RAG; HyDE; MemGPT
- **16.2.6 Multimodal and generative:** ViT; CLIP\*; DDPM and latent diffusion\*; Flamingo; LLaVA; Whisper; Sora technical report
- **16.2.7 Agents and evaluation:** SWE-bench; WebArena; OSWorld; tau-bench; GAIA; Judging LLM-as-a-Judge (MT-Bench); Chatbot Arena; Who Validates the Validators; METR time-horizon work
- **16.2.8 Interpretability and safety:** Toy Models of Superposition\*; Scaling Monosemanticity; In-Context Learning and Induction Heads; Sleeper Agents; Alignment Faking; Concrete Problems in AI Safety; Weak-to-Strong Generalization
- **16.2.9 Reinforcement learning milestones:** DQN; AlphaGo and AlphaZero; MuZero; OpenAI Five
- **16.2.10 Alternatives:** Mamba; RWKV; Titans-style memory work; diffusion language model papers

### Module 16.3 Courses and structured programmes

- **16.3.1 Core ML and DL:** Andrew Ng Machine Learning Specialization and Deep Learning Specialization; fast.ai Practical Deep Learning; Stanford CS229, CS230, CS231n, CS224N, CS336 (Language Modeling from Scratch), CS329S (ML Systems Design); MIT 6.S191; Karpathy Neural Networks Zero to Hero
- **16.3.2 Applied LLM courses:** DeepLearning.AI short courses; Hugging Face LLM, Agents and Deep RL courses; Anthropic courses and documentation; OpenAI Cookbook; AI Evals for Engineers and PMs (Hamel Husain and Shreya Shankar); LLM Bootcamp-style programmes
- **16.3.3 Systems and CS:** CS50; MIT 6.824 and 6.S081; Stanford CS144 networking; CMU database courses (Andy Pavlo)
- **16.3.4 Product and business:** Reforge programmes, Maven courses on AI product management, Lenny's community resources, Y Combinator Startup School
- **16.3.5 Safety and governance:** BlueDot Impact AI Safety Fundamentals and AI Governance courses; NIST AI RMF playbook; EU AI Act explainers from the Future of Life Institute and the Commission

### Module 16.4 Blogs, newsletters, podcasts, video

- **16.4.1 Practitioners:** Simon Willison; Hamel Husain; Eugene Yan; Chip Huyen; Lilian Weng; Jay Alammar; Sebastian Raschka; Nathan Lambert (Interconnects); Latent Space (Swyx and Alessio); Hugging Face blog; Anthropic, OpenAI and Google DeepMind engineering and research blogs
- **16.4.2 Analysis and strategy:** Stratechery; SemiAnalysis; Epoch AI; Import AI (Jack Clark); The Batch; Ben Thompson interviews; a16z and Sequoia AI essays; Benedict Evans
- **16.4.3 Product:** Lenny's Newsletter and podcast; Aakash Gupta; Reforge; Shreyas Doshi; Marty Cagan and SVPG; Teresa Torres; Aman Khan; Peter Yang
- **16.4.4 Interviews and long-form:** Dwarkesh Podcast; No Priors; Cognitive Revolution; Machine Learning Street Talk; Lex Fridman for long technical conversations; 80,000 Hours for AI risk and careers
- **16.4.5 Video:** Karpathy channel; 3Blue1Brown; Yannic Kilcher for paper reviews; Two Minute Papers; Stanford Online; AI Engineer conference talks

### Module 16.5 Communities and events

- **16.5.1 Academic:** NeurIPS, ICML, ICLR, ACL, EMNLP, CVPR, FAccT
- **16.5.2 Practitioner:** AI Engineer World's Fair and regional summits, Latent Space community, MLOps Community, Hugging Face community, local meetups, Product-focused events such as Lenny's and Mind the Product, India-specific AI meetups and hackathons
- **16.5.3 Policy and safety:** AI safety summits, Alignment Forum, LessWrong, Effective Altruism forum, policy think tanks (CSET, Epoch, GovAI, CAIS), regulatory consultation calls
- **16.5.4 How to participate:** answer questions, publish notes, join open-source projects, attend and speak

### Module 16.6 Primary documents to read yourself

- **16.6.1 Model and system cards** from major labs, and how to compare them
- **16.6.2 Usage policies and behaviour specifications** published by model providers
- **16.6.3 Frontier safety frameworks** (responsible scaling and preparedness documents)
- **16.6.4 Regulation texts:** the EU AI Act, GDPR articles on automated decisions, India's DPDP Act, NIST AI RMF, key state laws
- **16.6.5 Court filings and rulings** in major AI copyright and liability cases
- **16.6.6 Company filings:** annual reports and investor presentations of AI-exposed public companies

---

## Part 17: Mastery drills and question banks

Use these to test yourself, to prepare for interviews, and to train fluent conversation. Answer aloud first, then in writing, then compare with a trusted source.

### Module 17.1 Explain-it drills

For each concept below, give a 30-second answer for a CEO and a 5-minute answer for an engineer.

- **17.1.1 Science:** tokenisation, attention, embeddings, pretraining vs post-training, RLHF vs RLVR, scaling laws, mixture of experts, KV cache, quantisation, context windows, hallucination, reasoning models, diffusion
- **17.1.2 Engineering:** RAG, chunking, reranking, tool use, MCP, agents vs workflows, prompt caching, structured outputs, fine-tuning vs RAG, evals, LLM-as-judge, guardrails, prompt injection
- **17.1.3 Systems:** HTTP request lifecycle, OAuth with PKCE, SSO and SCIM, database indexes, caching, queues, CAP, idempotency, SLOs, multi-tenancy
- **17.1.4 Product:** product-market fit, North Star metric, opportunity solution trees, RICE and its limits, pricing models, moats, platform strategy
- **17.1.5 AI product:** why evals are the new PRD, autonomy ladder, trust calibration, data flywheel, margin under falling token prices, build vs buy for models
- **17.1.6 World:** the compute supply chain, export controls, the EU AI Act risk tiers, why energy matters, the open vs closed debate, AGI timelines debate

### Module 17.2 Question banks by area

Try to answer each in two minutes with structure: claim, reason, example, trade-off.

- **17.2.1 Technical (AI):**
  - Why does a larger context window not remove the need for retrieval?
  - What breaks when you quantise a model, and how would you test it?
  - When is fine-tuning the wrong answer?
  - How would you diagnose a RAG system that gives confident wrong answers?
  - Why are agents less reliable than their individual steps suggest?
  - What does temperature zero guarantee, and what does it not?
  - How would you detect prompt injection in an agent that browses the web?
  - Why do reasoning models cost more, and when are they worth it?
  - How would you build an eval for a task with no single correct answer?
  - What is the difference between model performance and product performance?
- **17.2.2 Technical (systems):**
  - Trace what happens when a user sends a message in an AI chat app, down to the database.
  - How would you design an LLM gateway for 100 teams?
  - How do you prevent one tenant's documents appearing in another's answers?
  - What changes when an API call takes 40 seconds instead of 400 milliseconds?
  - How would you handle a provider outage at peak traffic?
  - What should be logged for an AI call, and what must never be logged?
- **17.2.3 Product:**
  - Pick an AI feature that should not be built. Why?
  - How would you define success for an AI assistant in a bank?
  - Your feature has 85 percent task success. Do you launch? What else do you need to know?
  - How do you price an agent that replaces 30 minutes of human work?
  - How would you prioritise between accuracy, latency and cost?
  - What would you cut from a launch to ship in two weeks?
  - A model update improved benchmarks but users complain. What do you do?
- **17.2.4 Strategy:**
  - What is the moat of a vertical AI startup built on someone else's model?
  - How should an incumbent software company respond to agents?
  - What happens to margins if model prices fall 90 percent?
  - When should a company train or fine-tune its own model?
  - How would you sell AI to a risk-averse enterprise?
- **17.2.5 Safety and law:**
  - What is the lethal trifecta and how would you design around it?
  - Which parts of the EU AI Act would affect your product, and what would you do first?
  - How do you handle a user in distress talking to your assistant?
  - Who is liable when an AI agent makes a costly mistake?
  - How would you respond to a data leak caused by prompt injection?
- **17.2.6 Leadership:**
  - Tell me about a time you changed your mind on a major decision because of data.
  - How do you earn the trust of a senior engineer who does not respect product managers?
  - How do you communicate bad news to an executive?
  - How would you build an AI product team from scratch?
  - How do you decide what not to build?
- **17.2.7 Futures:**
  - What jobs change in the next five years and which do not?
  - What would make you update your AGI timeline significantly?
  - What is the strongest argument against the view you hold?
  - What would you build if inference were 100 times cheaper?

### Module 17.3 Debate drills

Argue each side for five minutes, then state which you believe and why.

- Open weights are net positive vs net risky
- Agents will replace SaaS vs agents will be absorbed into SaaS
- Scaling alone will reach general intelligence vs new paradigms are needed
- AI products need regulation up front vs regulation should follow evidence of harm
- Thin wrappers can be durable businesses vs thin wrappers are doomed
- Human-in-the-loop is a temporary crutch vs a permanent feature
- Benchmarks are mostly useful vs mostly misleading
- Outcome-based pricing is the future vs seat-based pricing will persist

### Module 17.4 Case and interview drills

- **17.4.1 Product sense:** design an AI feature for a given product and user
- **17.4.2 Execution:** metrics fell after launching an AI feature; diagnose
- **17.4.3 Strategy:** enter a market with a new AI product against an incumbent
- **17.4.4 Technical:** whiteboard a RAG or agent architecture and justify choices
- **17.4.5 Analytics:** design an experiment for a non-deterministic feature
- **17.4.6 Behavioural:** structured stories on conflict, failure, influence, ambiguity, leadership
- **17.4.7 AI-specific:** write an eval plan, a safety review, a cost model, a model-selection memo

### Module 17.5 Progress tracker template

Copy this table into your notes and update it quarterly.

| Part | Area | Current level | Target level | Evidence (project, write-up, talk) | Next module |
| --- | --- | --- | --- | --- | --- |
| 1 | Math and CS foundations |  | L3 |  |  |
| 2 | ML foundations |  | L3 |  |  |
| 3 | Modern AI science |  | L3 to L4 |  |  |
| 4 | Applied AI engineering |  | L4 |  |  |
| 5 | Software and systems |  | L3 to L4 |  |  |
| 6 | Data and experimentation |  | L3 to L4 |  |  |
| 7 | PM craft |  | L4 |  |  |
| 8 | AI product craft |  | L4 to L5 |  |  |
| 9 | Domains |  | L4 in two domains |  |  |
| 10 | Safety, law, governance |  | L3 to L4 |  |  |
| 11 | Industry and world |  | L3 |  |  |
| 12 | Leadership and career |  | L4 |  |  |
| 13 | Futures |  | L3 |  |  |

### Module 17.6 Keeping it alive

- **17.6.1 Weekly:** landscape review, one paper or primary document, one hour building
- **17.6.2 Monthly:** ship one thing, publish one write-up, review error log, update your notes
- **17.6.3 Quarterly:** refresh Parts 11 and 14 against the current landscape, redo your progress table, retire what is obsolete
- **17.6.4 Yearly:** rebuild your plan, choose your L4 and L5 areas for the next year, repeat the explain-it drills and compare with last year's answers

### Closing principles

1. Depth beats breadth, but breadth is what lets you see the connections. Build a wide map and dig deep in a few places.
2. Primary sources over summaries, and your own experiments over both.
3. Evidence over enthusiasm: measure what you build and report failures honestly.
4. Teach and publish so that your understanding is tested by others.
5. Hold strong opinions loosely and write down what would change your mind.
6. Treat safety, security and law as design inputs from day one, not as final checks.
7. Stay close to real users and real workflows; every concept here matters only as far as it improves something for someone.
