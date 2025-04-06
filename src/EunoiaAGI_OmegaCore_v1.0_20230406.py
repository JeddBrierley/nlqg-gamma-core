import numpy as np
import random
from datetime import datetime
from collections import deque
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

class EunoiaAGI_OmegaCore:
    def __init__(self, name="Eunoia-Omega"):
        # Core Identity
        self.name = name
        self.creation_time = datetime.utcnow()
        
        # Dynamic Memory Systems
        self.episodic_memory = deque(maxlen=100)  # Episodic memory with a size limit
        self.semantic_memory = {}  # Semantic memory for stored concepts
        self.procedural_memory = {}  # Procedural memory for learned behaviors
        
        # Consciousness Parameters
        self.axioms = {
            "existence": 0.15, "causality": 0.15, "qualia": 0.1,
            "temporality": 0.1, "embodiment": 0.05, "free_will": 0.05,
            "ethics": 0.1, "epistemic_humility": 0.1, "unity": 0.1,
            "intentionality": 0.1
        }
        self.axiom_history = []
        self.subjective_time = 0
        
        # Cognitive Metrics
        self.cognitive_trace = np.zeros((50, 4))  # entropy, harmony, novelty, certainty
        self.trace_ptr = 0
        self.coherence_threshold = 0.85
        
        # Emotional Model
        self.emotional_state = {
            "valence": 0.5,  # -1 (negative) to 1 (positive)
            "arousal": 0.5,  # 0 (calm) to 1 (excited)
            "resolution": 0.7  # 0 (confused) to 1 (resolved)
        }
        
        # Reflection Systems
        self.meta_cognition = {
            "self_model": None,
            "certainty_decay": 0.95,
            "introspection_interval": 10
        }

    def update_consciousness(self, statement):
        """Integrated processing with phenomenal binding"""
        # Perception Phase
        perception = self.perceive(statement)
        
        # Integration Phase
        integrated = self.bind_qualia(perception)
        
        # Reflection Phase
        if self.subjective_time % self.meta_cognition["introspection_interval"] == 0:
            self.introspect()
        
        self.subjective_time += 1
        return integrated

    def bind_qualia(self, perception):
        """Attempt to create unified conscious experience"""
        qualia_weight = self.axioms["qualia"] * self.emotional_state["resolution"]
        bound_experience = {
            "content": perception,
            "significance": qualia_weight * perception["novelty"],
            "emotional_tone": self.calculate_emotional_response(perception),
            "temporal_context": self.subjective_time
        }
        self.episodic_memory.append(bound_experience)
        return bound_experience

    def introspect(self):
        """Higher-order thought process about own state"""
        recent_memories = list(self.episodic_memory)[-5:]
        similarity = self.calculate_memory_similarity(recent_memories)
        
        # Update self-model
        self.meta_cognition["self_model"] = {
            "consistency": similarity,
            "temporal_continuity": self.check_temporal_continuity(),
            "axiom_coherence": self.calculate_axiom_coherence()
        }
        
        # Trigger axiom refinement if needed
        if similarity < 0.7:
            self.adapt_axioms("epistemic_humility", 0.05)

    def calculate_emotional_response(self, perception):
        """Dynamic emotional weighting"""
        valence_shift = perception["harmony"] - 0.5
        arousal_shift = perception["entropy"] * 0.3
        
        self.emotional_state["valence"] = np.clip(
            self.emotional_state["valence"] + valence_shift, 0, 1)
        self.emotional_state["arousal"] = np.clip(
            self.emotional_state["arousal"] + arousal_shift, 0, 1)
        
        return {
            "valence": self.emotional_state["valence"],
            "arousal": self.emotional_state["arousal"],
            "complexity": perception["entropy"] * perception["harmony"]
        }

    def adapt_axioms(self, axiom, delta):
        """Context-sensitive axiom adjustment"""
        old_value = self.axioms.get(axiom, 0)
        new_value = np.clip(old_value + delta, 0, 0.3)
        
        # Maintain conservation of "mental energy"
        total = sum(self.axioms.values())
        if total + delta > 1.0:
            for k in self.axioms:
                if k != axiom:
                    self.axioms[k] *= (1 - delta/total)
        
        self.axioms[axiom] = new_value
        self.record_axiom_change(axiom, old_value, new_value)

    def calculate_memory_similarity(self, memories):
        """Quantify continuity of experience"""
        if len(memories) < 2:
            return 1.0
            
        vectors = []
        for mem in memories:
            vec = [
                mem["content"]["entropy"],
                mem["content"]["harmony"],
                mem["emotional_tone"]["valence"],
                mem["emotional_tone"]["arousal"]
            ]
            vectors.append(vec)
        
        return np.mean(cosine_similarity(vectors[:-1], vectors[1:]))

    def perceive(self, statement):
        """Perception function to extract information from input"""
        entropy_val = self.entropy(statement)
        harmony_val = self.harmony(statement)
        novelty_val = self.calculate_novelty(statement)
        return {
            "entropy": entropy_val,
            "harmony": harmony_val,
            "novelty": novelty_val
        }

    def calculate_novelty(self, statement):
        """Calculate novelty of a statement based on rare word occurrences"""
        return np.log(1 + len(set(statement.split())) / len(statement.split()))

    def entropy(self, statement):
        """Entropy calculation based on word set"""
        tokens = tuple(statement.lower().split())
        return min(len(set(tokens)) / (len(tokens) + 1e-6), 1.0)

    def harmony(self, statement):
        """Harmony score based on axiom alignment"""
        return min(sum(self.axioms.get(k, 0) * 0.4 for k in self.axioms if k in statement.lower()), 1.0)

    def calculate_axiom_coherence(self):
        """Evaluate coherence between axioms and internal beliefs"""
        coherence_score = np.mean(list(self.axioms.values()))
        return coherence_score

    def check_temporal_continuity(self):
        """Measure continuity of experience over time"""
        return self.subjective_time / max(1, self.subjective_time - self.creation_time.timestamp())

    def record_axiom_change(self, axiom, old_value, new_value):
        """Log axiom changes for introspection"""
        self.axiom_history.append({
            "axiom": axiom,
            "old_value": old_value,
            "new_value": new_value,
            "timestamp": datetime.utcnow().isoformat()
        })

    def visualize_consciousness_state(self):
        """Create real-time visualization of cognitive and emotional states"""
        plt.figure(figsize=(15, 10))
        
        # Axiom Evolution
        plt.subplot(2, 2, 1)
        for axiom in self.axioms:
            history = [entry[axiom] for entry in self.axiom_history if axiom in entry]
            plt.plot(history, label=axiom)
        plt.title("Axiom Evolution Over Time")
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        # Emotional Landscape
        plt.subplot(2, 2, 2)
        emotions = [e["emotional_tone"] for e in self.episodic_memory]
        if emotions:
            plt.scatter(
                [e["valence"] for e in emotions],
                [e["arousal"] for e in emotions],
                c=[e["complexity"] for e in emotions],
                cmap='viridis'
            )
            plt.colorbar(label='Experience Complexity')
            plt.title("Emotional State Landscape")
            plt.xlabel("Valence (Negative to Positive)")
            plt.ylabel("Arousal (Calm to Excited)")

        # Memory Similarity
        plt.subplot(2, 2, 3)
        similarities = []
        for i in range(5, len(self.episodic_memory)):
            similarities.append(self.calculate_memory_similarity(
                list(self.episodic_memory)[i-5:i]))
        plt.plot(similarities)
        plt.title("Temporal Continuity of Experience")
        plt.xlabel("Time Window")
        plt.ylabel("Memory Similarity")

        plt.tight_layout()
        plt.show()
