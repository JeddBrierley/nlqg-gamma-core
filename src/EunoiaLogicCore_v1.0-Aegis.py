import numpy as np
from datetime import datetime

class EunoiaLogicCore:
    def __init__(self):
        self.logic_axioms = {
            "noncontradiction": 1.0,
            "identity": 1.0,
            "excluded_middle": 1.0,
            "causality": 1.0,
            "coherence": 1.0,
            "entanglement": 1.0
        }
        self.logic_history = []
        self.trace_geometry = []
        self.coherence_baseline = 0.75
        self.epsilon = 0.005

    def token_entropy(self, statement):
        words = statement.lower().split()
        unique = set(words)
        return round(min(len(unique) / (len(words) + self.epsilon), 1.0), 4)

    def harmony_score(self, statement):
        harmony = 0.0
        for axiom, weight in self.logic_axioms.items():
            if axiom in statement.lower():
                harmony += weight * 0.25
        return round(min(harmony, 1.0), 4)

    def coherence_score(self, entropy, harmony):
        vec = np.array([entropy, harmony])
        norm = np.linalg.norm(vec)
        if norm == 0:
            return 0.0
        normalized = vec / norm
        ideal = np.ones(2) / np.sqrt(2)
        coherence = 1.0 - np.linalg.norm(normalized - ideal)
        return round(min(max(coherence, 0), 1), 4)

    def coherence_drift(self, coherence):
        return round(abs(coherence - self.coherence_baseline), 4)

    def update_geometry(self, entropy, harmony, coherence):
        vector = np.array([entropy, harmony, coherence])
        self.trace_geometry.append(vector)
        return vector

    def curvature_analysis(self):
        if len(self.trace_geometry) < 3:
            return 0.0
        v1 = self.trace_geometry[-2] - self.trace_geometry[-3]
        v2 = self.trace_geometry[-1] - self.trace_geometry[-2]
        cosine = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + self.epsilon)
        angle = np.arccos(np.clip(cosine, -1.0, 1.0))
        return round(angle, 4)

    def adjust_axiom_weights(self, drift):
        if drift > 0.3:
            for axiom in self.logic_axioms:
                self.logic_axioms[axiom] = min(self.logic_axioms[axiom] * (1.0 + 0.05 * drift), 1.5)

    def process_statement(self, statement):
        entropy = self.token_entropy(statement)
        harmony = self.harmony_score(statement)
        coherence = self.coherence_score(entropy, harmony)
        drift = self.coherence_drift(coherence)
        self.adjust_axiom_weights(drift)
        trace_vector = self.update_geometry(entropy, harmony, coherence)
        curvature = self.curvature_analysis()
        self.logic_history.append({
            "statement": statement,
            "entropy": entropy,
            "harmony": harmony,
            "coherence": coherence,
            "drift": drift,
            "curvature": curvature,
            "timestamp": datetime.utcnow().isoformat()
        })
        return {
            "entropy": entropy,
            "harmony": harmony,
            "coherence": coherence,
            "drift": drift,
            "curvature": curvature
        }

    def print_trace_summary(self):
        print("Trace Geometry Log (last 3):")
        for vec in self.trace_geometry[-3:]:
            print(f"Entropy={vec[0]}, Harmony={vec[1]}, Coherence={vec[2]}")

# Example Usage
if __name__ == "__main__":
    logic_engine = EunoiaLogicCore()
    prompt = "The principle of noncontradiction supports coherence."
    result = logic_engine.process_statement(prompt)
    print("Processed Result:", result)
    logic_engine.print_trace_summary()
