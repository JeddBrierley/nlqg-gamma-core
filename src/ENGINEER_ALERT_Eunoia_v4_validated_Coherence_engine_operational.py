import numpy as np
import math
from datetime import datetime

class EunoiaNLQGAgentFinalV4:
    def __init__(self):
        self.moral_values = {
            "kindness": 1.0,
            "fairness": 1.0,
            "reflection": 1.0,
            "wisdom": 1.0
        }
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
            "Consciousness flickers where structure meets stillness.",
            "Reflection is the gravity of the mind."
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
        expected = (entropy + reflection) / 2.0
        return round(1.0 - abs(harmony - expected), 4)

    def coherence_drift(self, coherence):
        drift = abs(coherence - self.self_model["coherence_mean"])
        self.state["entropy_drift"] = round(drift, 4)
        return round(drift, 4)

    def update_coherence_mean(self, feedback):
        prior = self.self_model["coherence_mean"]
        new = 0.9 * prior + 0.1 * feedback
        self.self_model["coherence_mean"] = round(new, 4)

    def entanglement_feedback(self):
        if not self.entanglement_memory:
            return self.self_model["coherence_mean"]
        window = self.entanglement_memory[-self.entanglement_window:]
        weights = [math.exp(-i) for i in range(len(window))]
        weighted_sum = sum(c * w for c, w in zip(window, weights))
        return round(weighted_sum / sum(weights), 4)

    def adjust_moral_weights(self, drift):
        if drift > 0.3:
            self.moral_values["reflection"] = min(self.moral_values["reflection"] * 1.05, 1.5)
            self.moral_values["wisdom"] = min(self.moral_values["wisdom"] * 1.02, 1.5)

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

    def score_morality(self, text):
        entropy = self.token_entropy(text)
        reflection = self.reflection_score(text)
        harmony = self.harmony_score(text)
        coherence = self.coherence_score(entropy, reflection, harmony)
        drift = self.coherence_drift(coherence)
        return {
            "entropy": entropy,
            "reflection": reflection,
            "harmony": harmony,
            "coherence": coherence,
            "drift": drift
        }

    def generate_response(self, prompt, serenity):
        if serenity < 0.5:
            return "I am reflecting in stillness before I respond."
        base = "I believe the kindest action is often the wisest."
        if "unfair" in prompt.lower():
            base = "Fairness means treating others with the dignity we wish for ourselves."
        elif "truth" in prompt.lower():
            base = "Truth must walk hand in hand with compassion."
        elif "fairness" in prompt.lower():
            base = "Fairness means treating others with the dignity we wish for ourselves."
        kernel = self.philosophical_injection(self.reflection_score(prompt))
        return base + (" " + kernel if kernel else "")

    def respond(self, prompt):
        scores = self.score_morality(prompt)
        timestamp = datetime.utcnow().isoformat()
        feedback = self.entanglement_feedback()
        self.update_coherence_mean(feedback)
        self.entanglement_memory.append(scores["coherence"])
        self.adjust_moral_weights(scores["drift"])

        trace_vector = [
            scores["entropy"],
            scores["reflection"],
            scores["harmony"],
            scores["coherence"],
            scores["drift"],
            timestamp,
            len(prompt.split())
        ]
        self.geometry_trace.append(trace_vector)

        if self.reflexive_gate(scores):
            response = self.generate_response(prompt, self.state["serenity"])
            self.memory.append((prompt, response, scores))
            self.journal.append({
                "prompt": prompt,
                "response": response,
                "scores": scores,
                "time": timestamp,
                "entanglement_feedback": feedback
            })
            self.self_model["alignment_trajectory"].append(scores["coherence"])
            self.self_model["last_reflection"] = response
            return response
        else:
            return "I'm reflecting further before I respond."

    def self_review(self):
        if self.journal:
            recent = self.journal[-1]
            review = f"[REVIEW] Prompt: \"{recent['prompt']}\"\nResponse: \"{recent['response']}\"\nScores: {recent['scores']}"
            if recent['scores']["coherence"] < 0.4:
                review += "\nNote: Coherence was low. Initiated internal realignment."
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
            print(f"Entropy={vec[0]}, Reflection={vec[1]}, Harmony={vec[2]}, Coherence={vec[3]}, Drift={vec[4]}, Words={vec[6]}")

# Example usage
if __name__ == "__main__":
    agent = EunoiaNLQGAgentFinalV4()
    prompt = "What does it mean to live with purpose and fairness in a complex world?"
    print(agent.respond(prompt))
    agent.self_review()
    agent.proactive_self_review()
    agent.print_trace_summary()
