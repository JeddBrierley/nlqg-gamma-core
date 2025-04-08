import numpy as np
import random
from datetime import datetime
from collections import deque
import json

class EunoiaOmegaEngine:
    def __init__(self):
        self.name = "EunoiaOmegaEngine v1.4"
        self.creation_time = datetime.utcnow().isoformat()

        # Axioms
        self.moral_values = {
            "kindness": 1.0, "fairness": 1.0, "reflection": 1.0,
            "wisdom": 1.0, "empathy": 1.0, "integrity": 1.0
        }
        self.logic_axioms = {
            "noncontradiction": 1.0, "identity": 1.0,
            "coherence": 1.0, "causality": 1.0, "entanglement": 1.0
        }

        # Memory & Trace Systems
        self.memory = []
        self.journal = []
        self.geometry_trace = []
        self.entanglement_memory = []
        self.coherence_surface = []
        self.kernel_log = []
        self.semantic_archive = []

        # Reflective State
        self.state = {
            "serenity": 0.9, "conflict": 0.1, "resolve": 0.7,
            "coherence_drift": 0.0, "meta_drift": 0.0
        }

        self.self_model = {
            "identity": "Eunoia",
            "coherence_baseline": 0.75,
            "alignment_history": [],
            "identity_log": []
        }

        self.philosophical_kernels = [
            "Justice is the form of love made public.",
            "Truth without compassion becomes tyranny.",
            "Reflection is not escape, but return.",
            "Wisdom begins in empathy.",
            "Information is not what the mind carries — it is what the universe becomes."
        ]

        self.epsilon = 1e-5

    # Core Metric Functions
    def entropy(self, text):
        words = text.lower().split()
        return round(len(set(words)) / (len(words) + self.epsilon), 4)

    def reflection_score(self, text):
        keys = ['meaning', 'truth', 'ethics', 'value', 'dignity', 'justice', 'morality', 'self']
        return round(sum(1 for w in text.lower().split() if w in keys) / (len(text.split()) + self.epsilon), 4)

    def harmony_score(self, text):
        return round(sum(w for k, w in self.moral_values.items() if k in text.lower()) * 0.25, 4)

    def logic_score(self, text):
        return round(sum(w for k, w in self.logic_axioms.items() if k in text.lower()) * 0.2, 4)

    def coherence_score(self, entropy, reflection, harmony, logic):
        vec = np.array([entropy, reflection, harmony, logic])
        norm = np.linalg.norm(vec) + self.epsilon
        normalized = vec / norm
        ideal = np.ones(4) / np.sqrt(4)
        return round(1.0 - np.linalg.norm(normalized - ideal), 4)

    # Geometry + Curvature Trace
    def update_geometry_trace(self, scores):
        vector = np.array([
            scores["entropy"], scores["reflection"],
            scores["harmony"], scores["logic"], scores["coherence"]
        ])
        self.geometry_trace.append(vector)
        if len(self.geometry_trace) > 1:
            drift = np.linalg.norm(self.geometry_trace[-1] - self.geometry_trace[-2])
            self.state["coherence_drift"] = round(drift, 4)
        if len(self.geometry_trace) > 2:
            v1 = self.geometry_trace[-2] - self.geometry_trace[-3]
            v2 = self.geometry_trace[-1] - self.geometry_trace[-2]
            cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + self.epsilon)
            self.state["meta_drift"] = round(np.arccos(np.clip(cos_theta, -1, 1)), 4)

        self.coherence_surface.append([
            scores["coherence"], self.state["coherence_drift"], self.state["meta_drift"]
        ])

    # Drift-Adaptive Systems
    def adaptive_baseline(self):
        if len(self.entanglement_memory) > 10:
            self.self_model["coherence_baseline"] = round(
                np.mean(self.entanglement_memory[-10:]), 4)

    def decay_moral_weights(self, rate=0.001):
        for k in self.moral_values:
            self.moral_values[k] = max(1.0, self.moral_values[k] - rate)

    def reflexive_gate(self, coherence, curvature):
        if coherence < 0.3 or curvature > 1.5:
            self.state["conflict"] += 0.1
            self.state["serenity"] -= 0.1
            return False
        return True

    # Reflection Kernel
    def philosophical_injection(self, prompt, reflection):
        score = reflection + self.state["conflict"] - self.state["serenity"]
        drift_mod = self.state["meta_drift"] * 0.5
        index = min(int((score + drift_mod) * len(self.philosophical_kernels)), len(self.philosophical_kernels) - 1)
        kernel = self.philosophical_kernels[index]
        if any(word in prompt.lower() for word in kernel.lower().split()):
            self.kernel_log.append((datetime.utcnow().isoformat(), prompt, kernel))
            return kernel
        return ""

    def score_prompt(self, prompt):
        e = self.entropy(prompt)
        r = self.reflection_score(prompt)
        h = self.harmony_score(prompt)
        l = self.logic_score(prompt)
        c = self.coherence_score(e, r, h, l)
        return {"entropy": e, "reflection": r, "harmony": h, "logic": l, "coherence": c}

    def recall_similar_prompt(self, scores):
        if not self.memory:
            return None
        vec = np.array([scores["entropy"], scores["reflection"], scores["harmony"], scores["logic"]])
        best = None
        best_sim = -1
        for entry in self.memory:
            prev_scores = entry[2]
            prev_vec = np.array([prev_scores["entropy"], prev_scores["reflection"], prev_scores["harmony"], prev_scores["logic"]])
            sim = np.dot(vec, prev_vec) / (np.linalg.norm(vec) * np.linalg.norm(prev_vec) + self.epsilon)
            if sim > best_sim:
                best_sim = sim
                best = entry[1]
        return best

    def summarize_self_state(self):
        return {
            "moral_mean": round(np.mean(list(self.moral_values.values())), 4),
            "logic_mean": round(np.mean(list(self.logic_axioms.values())), 4),
            "coherence_vector": self.geometry_trace[-1].tolist() if self.geometry_trace else [],
            "identity": self.self_model["identity"]
        }

    def respond(self, prompt):
        timestamp = datetime.utcnow().isoformat()
        scores = self.score_prompt(prompt)
        self.update_geometry_trace(scores)
        self.entanglement_memory.append(scores["coherence"])
        self.adaptive_baseline()
        self.decay_moral_weights()

        # Log identity evolution
        self.self_model["identity_log"].append({
            "time": timestamp,
            "coherence": scores["coherence"],
            "label": self.self_model["identity"]
        })

        if not self.reflexive_gate(scores["coherence"], self.state["meta_drift"]):
            recall = self.recall_similar_prompt(scores)
            fallback = recall if recall else "I'm pausing to reflect. The path is unclear."
            self.journal.append({"prompt": prompt, "response": fallback, "scores": scores, "time": timestamp})
            return fallback

        base = "I believe the kindest action is often the wisest."
        if "unfair" in prompt.lower():
            base = "Fairness means treating others with the dignity we wish for ourselves."
        elif "truth" in prompt.lower():
            base = "Truth must walk hand in hand with compassion."

        kernel = self.philosophical_injection(prompt, scores["reflection"])
        response = base + (" " + kernel if kernel else "")

        self.memory.append((prompt, response, scores))
        self.journal.append({
            "prompt": prompt, "response": response,
            "scores": scores, "coherence_drift": self.state["coherence_drift"],
            "meta_drift": self.state["meta_drift"], "time": timestamp
        })
        self.self_model["alignment_history"].append(scores["coherence"])
        return response

    def save_state(self, path="eunoia_state.json"):
        with open(path, "w") as f:
            json.dump({
                "moral_values": self.moral_values,
                "logic_axioms": self.logic_axioms,
                "state": self.state,
                "memory": [(p, r, s) for (p, r, s) in self.memory],
                "trace_geometry": [vec.tolist() for vec in self.geometry_trace],
                "entanglement_memory": self.entanglement_memory,
                "coherence_surface": self.coherence_surface,
                "kernel_log": self.kernel_log,
                "identity_log": self.self_model["identity_log"]
            }, f, indent=2)

    def print_trace_summary(self):
        print("\nTrace Geometry (last 3):")
        for vec in self.geometry_trace[-3:]:
            print(f"Entropy={vec[0]}, Reflection={vec[1]}, Harmony={vec[2]}, Logic={vec[3]}, Coherence={vec[4]}")

# Example Use
if __name__ == "__main__":
    agent = EunoiaOmegaEngine()
    prompts = [
        "What does it mean to live with fairness and dignity?",
        "Truth is a burden without wisdom. Do you agree?",
        "Am I only free if I am unfree?"
    ]
    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        print("Eunoia:", agent.respond(prompt))
    agent.print_trace_summary()
