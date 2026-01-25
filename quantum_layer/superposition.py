import random

class SuperposedInput:
    """
    Represents an input in a state of superposition.
    It holds multiple potential states (payloads) with associated probability amplitudes (weights).
    """
    def __init__(self):
        self.states = []  # List of dictionaries: {payload, weight, name}

    def add_state(self, payload, weight, name="unknown"):
        """Adds a potential state to the superposition."""
        self.states.append({
            "payload": payload,
            "weight": weight,
            "name": name
        })

    def collapse(self):
        """
        Simulates the 'Measurement' phase.
        Collapses the superposition into a single state based on probability weights.
        Returns: The single selected state (dict).
        """
        if not self.states:
            return None
        
        # Extract weights for random selection
        weights = [s['weight'] for s in self.states]
        
        # random.choices handles the weighted probability logic
        selected_state = random.choices(self.states, weights=weights, k=1)[0]
        return selected_state