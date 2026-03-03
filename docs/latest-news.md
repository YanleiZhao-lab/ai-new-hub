# Latest AI News

> Last Updated: 2026-03-03 08:01:20

## Most Recent

# AI News Briefing - 2026-03-03

> Updated: 2026-03-03 08:00:00  
> Source: arXiv cs.AI  

---

## 📊 Today's Highlights

- **6 new papers** from arXiv Artificial Intelligence
- Focus areas: LLM Benchmarking, Theorem Proving, Uncertainty Quantification, RL

---

## 🔬 Research Papers

### 1. DARE-bench: LLM Data Science Benchmark

**Title:** DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in Data Science  
**Source:** arXiv:2602.24288  
**Authors:** Fan Shu et al.  
**Published:** ICLR 2026  

**Abstract:**  
Introduces DARE-bench, a benchmark for machine learning modeling and data science instruction following. Unlike existing benchmarks relying on human- or model-based judges, all tasks have verifiable ground truth for objective evaluation. Consists of 6,300 Kaggle-derived tasks with both training and evaluation sets. Even highly capable models like gpt-o4-mini struggle, especially in ML modeling tasks. Fine-tuning on DARE-bench data improves Qwen3-32B accuracy by 1.83x (supervised) and Qwen3-4B by 8x (RL).

**Key Points:**
- 6,300 verifiable tasks from Kaggle
- Process-aware evaluation capturing instruction adherence
- Significant performance gains through fine-tuning
- Addresses lack of standardized LLM evaluation in data science

**Links:** [arXiv](https://arxiv.org/abs/2602.24288) | [PDF](https://arxiv.org/pdf/2602.24288) | [HTML](https://arxiv.org/html/2602.24288v1)

---

### 2. Minimal Agent for Automated Theorem Proving

**Title:** A Minimal Agent for Automated Theorem Proving  
**Source:** arXiv:2602.24273  
**Authors:** Leopoldo Sarra  
**Published:** 2026-02-27  

**Abstract:**  
Proposes a minimal agentic baseline for systematic comparison across AI-based theorem prover architectures. Implements core features of state-of-the-art systems: iterative proof refinement, library search, and context management. Demonstrates competitive performance with significantly simpler architecture. Shows consistent advantages of iterative approaches over single-shot generation in sample efficiency and cost-effectiveness.

**Key Points:**
- Simplified architecture for theorem proving
- Iterative refinement vs single-shot generation
- Open-source implementation released
- Competitive with state-of-the-art methods

**Links:** [arXiv](https://arxiv.org/abs/2602.24273) | [PDF](https://arxiv.org/pdf/2602.24273)

---

### 3. UMPIRE: Uncertainty Quantification for MLLMs

**Title:** Uncertainty Quantification for Multimodal Large Language Models with Incoherence-adjusted Semantic Volume  
**Source:** arXiv:2602.24195  
**Authors:** Gregory Kang Ruey Lau et al.  
**Published:** 2026-02-27 (ICLR 2025 Question Workshop, ICML 2025 R2-FM Workshop)  

**Abstract:**  
Introduces UMPIRE, a training-free uncertainty quantification framework for Multimodal LLMs. Works across various input/output modalities without external tools, using only internal model features. Computes incoherence-adjusted semantic volume of sampled responses, capturing global semantic diversity and local incoherence. Consistently outperforms baselines in error detection and uncertainty calibration across image, audio, and video-text benchmarks, including adversarial and OOD settings.

**Key Points:**
- Training-free uncertainty quantification
- Cross-modal support (image, audio, video)
- No external tools required
- Better error detection and calibration
- Generalizes to non-text outputs

**Links:** [arXiv](https://arxiv.org/abs/2602.24195) | [PDF](https://arxiv.org/pdf/2602.24195)

---

### 4. Deep RL for Flexible Job Shop Scheduling

**Title:** Learning Flexible Job Shop Scheduling under Limited Buffers and Material Kitting Constraints  
**Source:** arXiv:2602.24180  
**Authors:** Shishun Zhang et al.  
**Published:** 2026-02-27  

**Abstract:**  
Addresses the Flexible Job Shop Scheduling Problem (FJSP) with limited buffers and material kitting - a more realistic production scenario. Uses deep reinforcement learning with heterogeneous graph networks to model global state. Constructs efficient message passing among machines, operations, and buffers to avoid decisions causing frequent pallet changes. Outperforms traditional heuristics and advanced DRL methods on both synthetic and real production datasets.

**Key Points:**
- Realistic production scheduling constraints
- Heterogeneous graph neural networks in DRL
- Reduces pallet changes in long-sequence scheduling
- Better makespan and computational cost balance
- Includes supplementary simulation video

**Links:** [arXiv](https://arxiv.org/abs/2602.24180) | [PDF](https://arxiv.org/pdf/2602.24180)

---

### 5. LemmaBench: Live Math Benchmark

**Title:** LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics  
**Source:** arXiv:2602.24173  
**Authors:** Amaury Hayat et al.  
**Published:** 2026-02-27  

**Abstract:**  
Presents an updatable benchmark for LLM mathematics capabilities using latest research results. Automatic pipeline extracts lemmas from arXiv and rewrites them into self-contained statements. Can be updated regularly with new problems from human research, while previous instances can be used for training. Current state-of-the-art LLMs achieve 10-15% accuracy in theorem proving (pass@1), showing large room for improvement to reach human-level capabilities.

**Key Points:**
- Live benchmark from latest math research
- Automatic lemma extraction from arXiv
- Self-contained problem statements
- Regular updates possible
- Current SOTA LLMs at 10-15% accuracy

**Links:** [arXiv](https://arxiv.org/abs/2602.24173) | [PDF](https://arxiv.org/pdf/2602.24173)

---

### 6. SCOPE: RLVR with Fine-Grained Guidance

**Title:** Recycling Failures: Salvaging Exploration in RLVR via Fine-Grained Off-Policy Guidance  
**Source:** arXiv:2602.24110  
**Authors:** Yanwei Ren et al.  
**Published:** 2026-02-27  

**Abstract:**  
Addresses limitations in Reinforcement Learning from Verifiable Rewards (RLVR). Standard outcome-based supervision penalizes partially correct trajectories as heavily as completely wrong ones, degrading rollout diversity. Proposes SCOPE (Step-wise Correction for On-Policy Exploration), which uses Process Reward Models to pinpoint first erroneous step and applies fine-grained rectification. Increases diversity score by 13.5%, achieving SOTA results with 46.6% accuracy on math reasoning and 53.4% on OOD tasks.

**Key Points:**
- Salvages partially correct rollouts
- Step-wise off-policy correction
- 13.5% increase in diversity
- SOTA: 46.6% math reasoning accuracy
- 53.4% OOD reasoning accuracy

**Links:** [arXiv](https://arxiv.org/abs/2602.24110) | [PDF](https://arxiv.org/pdf/2602.24110)

---

## 📈 Research Trends

- **LLM Evaluation:** Multiple benchmarks emerging for specific domains (data science, math)
- **Uncertainty Quantification:** Growing focus on reliable MLLM deployment
- **RL for Reasoning:** RLVR and process reward models showing promise
- **Theorem Proving:** Minimal architectures achieving competitive results

---

## 🏷️ Tags

`LLM` `Benchmark` `Reinforcement Learning` `Multimodal` `Theorem Proving` `Uncertainty` `arXiv`

---

*Auto-generated by OpenClaw AI News Agent*


---

## Archive

See [news archive](./news/) for more.
