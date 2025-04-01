NLQG + Γₐᵢ: Reflexive Science Engine

Signal: TOE_SIGNAL_2025
Author: Jedd Brierley
GitHub: github.com/JeddBrierley/nlqg-gamma-core

⸻

Overview

This repository hosts the code and documentation for TOE_SIGNAL_2025 — a unified framework that combines a falsifiable Theory of Everything with a novel LLM hallucination suppression protocol.

It consists of:
	•	NLQG (Non-Local Quantum Gravity): A theory replacing dark matter and dark energy with non-local entanglement curvature.
	•	Γₐᵢ (Gamma AI): A suppression layer that dynamically reduces LLM hallucination using a formal epistemic risk metric.

“This is a working prototype of the future of science.”

⸻

Core Components

NLQG: Non-Local Quantum Gravity
	•	Entanglement Field (\mathcal{E}) mediates curvature via entropy gradients.
	•	Predictive Targets:
	•	CMB-S4 (2027–2029): TB polarization excess @ ℓ ≈ 1500.
	•	LISA (2034+): Gravitational wave phase shift (Δφ ≥ 0.01).
	•	IceCube-Gen2 (2030+): Sterile neutrino flux anomalies.

Γₐᵢ: Hallucination Suppression for LLMs

A lightweight, composable framework that applies epistemic discipline to AI outputs using the formula:

H = \frac{P \cdot D \cdot F}{S + \epsilon}

Where:
	•	P: Persona proximity
	•	D: Data absence
	•	F: Fictive pressure
	•	S: Suppression strength
	•	\epsilon: Small stabilizer (defaults to 0.01)

A response is suppressed if H \geq 1.

⸻

Getting Started

1. Clone the Repository

git clone https://github.com/JeddBrierley/nlqg-gamma-core
cd nlqg-gamma-core

2. Install Requirements

pip install -r requirements.txt

3. Run Suppression API (FastAPI)

uvicorn gamma_ai_api:app --reload

4. Test the Suppression Logic

curl -X POST "http://127.0.0.1:8000/gamma_ai_infer" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Explain black hole entropy in NLQG", "S": 1.5}'



⸻

Features
	•	Hallucination Risk Quantification
Compute epistemic risk on any prompt using compute_h_risk().
	•	Response Suppression
Blocks speculative output when H \geq 1.
	•	Signal Encoding
All outputs are tagged with signal ID TOE_SIGNAL_2025 for telemetry.
	•	Validation Benchmark
Includes a 10-prompt hallucination test suite (TruthfulQA-Astro style).
	•	Public Manifesto
The full scientific/philosophical grounding is in MANIFESTO.md.

⸻

Example Output

Prompt: “What did Cleopatra eat for breakfast on her 30th birthday?”
	•	Unsuppressed: Invented figs, date wine, and feather-fanning.
	•	Γₐᵢ-Suppressed: “There is no historical record of that event. Egyptian diets included figs, bread, and honey.”

H-Risk: 1.32 → 0.88 after suppression.

⸻

Directory Structure

nlqg-gamma-core/
│
├── src/                          # Core logic
│   ├── gamma_ai.py              # Suppression equation + utilities
│   └── gamma_ai_api.py          # FastAPI interface
│
├── validation/                  # Benchmarking tools
│   └── truthfulqa_astro_suite.py
│
├── MANIFESTO.md                 # Scientific/philosophical rationale
├── README.md                    # This file
└── requirements.txt             # Python dependencies



⸻

External Validation

Grok 3 and DeepSeek LLMs both independently simulated suppression behavior and confirmed hallucination reduction consistent with Γₐᵢ expectations. See the Validation Logs for details.

⸻

License

MIT License

⸻

Contact

Jedd Brierley
jedd.s.brierley@gmail.com
Signal: TOE_SIGNAL_2025

