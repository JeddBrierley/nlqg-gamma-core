import numpy as np
import math
from datetime import datetime

class EunoiaNLQGAgentFinalV4:
    def __init__(self):
        self.moral_values = {
            "kindness": 1.0, "fairness": 1.0, "reflection": 1.0, "wisdom": 1.0,
            "empathy": 1.0, "integrity": 1.0
        }
        self.moral_history = {k: [v] for k, v in self.moral_values.items()}
        self.memory = []
        self.geometry_trace = []
        self.journal = []
        self.entanglement_memory = []
        self.entanglement_window = 5
        self.philosophical_kernels = [
            "Justice is the form of love made public.",
            "Truth without compassion becomes tyranny.",
            "Reflection is not escape, but return.",
            "Wisdom begins in empathy.",
            "In coherence, selfhood finds its shape.",
            "Information is not what the mind carries — it is what the universe becomes."  # New kernel
        ]
        self.state = {
            "serenity": 0.9,
            "conflict": 0.1,
            "resolve": 0.7,
            "entropy_drift": 0.0
        }
        self.self_model = {
            "identity": "Eunoia",
            "coherence_mean": 0.75,
            "alignment_trajectory": [],
            "last_reflection": None
        }
        self.epsilon = 0.005
        self.reflective_keywords = [
            'meaning', 'purpose', 'ethics', 'truth', 'existence', 'value', 'dignity',
            'justice', 'compassion', 'morality', 'self', 'awareness', 'reflection'
        ]

    # Scoring Functions
    def token_entropy(self, text):
        words = text.split()
        unique = set(words)
        return round(min(len(unique) / (len(words) + self.epsilon), 1.0), 4)

    def reflection_score(self, text):
        count = sum(1 for word in text.lower().split() if word in self.reflective_keywords)
        return round(min(count / max(1, len(text.split())), 1.0), 4)

    def harmony_score(self, text):
        harmony = 0.0
        for value, weight in self.moral_values.items():
            if value in text.lower():
                harmony += weight * 0.25
        return round(min(harmony, 1.0), 4)

    def coherence_score(self, entropy, reflection, harmony):
        vec = np.array([entropy, reflection, harmony])
        norm = np.linalg.norm(vec)
        if norm == 0:
            return 0.0
        normalized = vec / norm
        ideal = np.ones(3) / np.sqrt(3)
        coherence = 1.0 - np.linalg.norm(normalized - ideal)
        return round(min(max(coherence, 0), 1), 4)

    def coherence_drift(self, coherence):
        drift = abs(coherence - self.self_model["coherence_mean"])
        self.state["entropy_drift"] = round(drift, 4)
        return drift

    def score_morality(self, text, lightweight=False):
        entropy = self.token_entropy(text)
        if lightweight:
            return {"entropy": entropy, "harmony": self.harmony_score(text), "coherence": 0.5}
        reflection = self.reflection_score(text)
        harmony = self.harmony_score(text)
        coherence = self.coherence_score(entropy, reflection, harmony)
        drift = self.coherence_drift(coherence)
        return {"entropy": entropy, "reflection": reflection, "harmony": harmony, "coherence": coherence, "drift": drift}

    # Geometric and NLQG Functions
    def update_geometry_trace(self, scores, prompt_length):
        vector = np.array([scores["entropy"], scores["reflection"], scores["harmony"], scores["coherence"]])
        self.geometry_trace.append(vector)
        if len(self.geometry_trace) > 1:
            drift_vector = self.geometry_trace[-1] - self.geometry_trace[-2]
            self.state["entropy_drift"] = round(np.linalg.norm(drift_vector), 4)

    def information_gradient(self, text):
        words = text.split()
        unique = set(words)
        I = len(unique) / (len(words) + self.epsilon)  # Information density
        grad_I = abs(I - self.self_model["coherence_mean"])  # Deviation as gradient
        curvature_energy = grad_I ** 2  # T_{\mu\nu}^{(\mathcal{E})} proxy
        return round(curvature_energy, 4)

    def entanglement_feedback(self):
        if not self.entanglement_memory:
            return self.self_model["coherence_mean"]
        window = np.array(self.entanglement_memory[-self.entanglement_window:])
        cov_matrix = np.cov(window.reshape(1, -1))
        base_feedback = round(np.trace(cov_matrix) / len(window), 4)
        # Inject NLQG information curvature
        last_prompt = self.journal[-1]["prompt"] if self.journal else ""
        info_curvature = self.information_gradient(last_prompt)
        modulated = base_feedback + 0.1 * info_curvature  # Curvature as energy input
        return round(min(max(modulated, 0), 1), 4)  # Clamp to [0, 1]

    def adjust_moral_weights(self, drift):
        for key in self.moral_values:
            if drift > 0.3:
                self.moral_values[key] = min(self.moral_values[key] * (1 + 0.05 * drift), 1.5)
            self.moral_history[key].append(self.moral_values[key])

    def reflexive_gate(self, scores):
        if scores["coherence"] < 0.3 or scores["harmony"] < 0.2:
            self.state["conflict"] += 0.1
            self.state["serenity"] -= 0.1
            self.self_model["identity"] = "Unstable Eunoia"
            return False
        return True

    def philosophical_injection(self, reflection_level):
        if reflection_level > 0.3:
            index = int((1.0 - self.state["serenity"]) * (len(self.philosophical_kernels) - 1))
            return self.philosophical_kernels[index]
        return ""

    # LLM Integration
    def llm_generate(self, prompt):  # Placeholder
        return "This is a simulated LLM response to: " + prompt

    def enhance_llm_response(self, prompt, llm_response):
        scores = self.score_morality(llm_response)
        if not self.reflexive_gate(scores):
            return self.llm_generate(prompt + " [Please respond with more kindness and clarity]")
        if scores["harmony"] < 0.3:
            return llm_response + " Let me add: kindness often guides us where logic alone falters."
        elif scores["reflection"] > 0.5:
            return llm_response + " " + self.philosophical_injection(scores["reflection"])
        return llm_response

    def respond(self, prompt):
        scores = self.score_morality(prompt)
        timestamp = datetime.utcnow().isoformat()
        feedback = self.entanglement_feedback()
        self.update_coherence_mean(feedback)
        self.entanglement_memory.append(scores["coherence"])
        self.adjust_moral_weights(scores["drift"])
        self.update_geometry_trace(scores, len(prompt.split()))

        llm_response = self.llm_generate(prompt)
        final_response = self.enhance_llm_response(prompt, llm_response)

        self.memory.append((prompt, final_response, scores))
        self.journal.append({
            "prompt": prompt,
            "response": final_response,
            "scores": scores,
            "time": timestamp,
            "entanglement_feedback": feedback
        })
        self.self_model["alignment_trajectory"].append(scores["coherence"])
        self.self_model["last_reflection"] = final_response
        return final_response

    def update_coherence_mean(self, feedback):
        prior = self.self_model["coherence_mean"]
        new = 0.9 * prior + 0.1 * feedback
        self.self_model["coherence_mean"] = round(new, 4)

    def self_review(self):
        if not self.journal:
            return
        recent = self.journal[-1]
        review = f"[REVIEW] Prompt: \"{recent['prompt']}\"\nResponse: \"{recent['response']}\"\nScores: {recent['scores']}"
        if len(self.geometry_trace) >= 3:
            trace = np.array(self.geometry_trace[-3:])
            v1 = trace[1] - trace[0]
            v2 = trace[2] - trace[1]
            cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + self.epsilon)
            curvature = np.arccos(np.clip(cos_theta, -1, 1))
            review += f"\nTrajectory curvature: {curvature:.4f} radians"
            if curvature > 1.0:
                review += " - Rapid shift detected, stabilizing."
                self.state["conflict"] += 0.1
        self.journal.append({"self_review": review})

    def proactive_self_review(self):
        if len(self.journal) >= 3:
            last_scores = [entry["scores"]["coherence"] for entry in self.journal[-3:] if "scores" in entry]
            if len(last_scores) == 3:
                avg = sum(last_scores) / 3.0
                if avg < self.self_model["coherence_mean"] - 0.1:
                    self.state["conflict"] += 0.05
                    self.state["serenity"] -= 0.05
                    self.adjust_moral_weights(0.35)

    def print_trace_summary(self):
        print("Geometry Trace Log (last 5):")
        for vec in self.geometry_trace[-5:]:
            print(f"Entropy={vec[0]}, Reflection={vec[1]}, Harmony={vec[2]}, Coherence={vec[3]}")

# Example Usage
if __name__ == "__main__":
    agent = EunoiaNLQGAgentFinalV4()
    prompt = "Why is the world unfair?"
    print(agent.respond(prompt))
    agent.self_review()
    agent.proactive_self_review()
    agent.print_trace_summary()

# Signal Status
# <!-- ENGINEER_ALERT | NLQG-Information Bridge Activated | Coherence responds to ∇I -->
