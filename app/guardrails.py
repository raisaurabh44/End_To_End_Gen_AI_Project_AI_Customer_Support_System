from detoxify import Detoxify

class Guardrails:
    def __init__(self):
        self.detoxify = Detoxify('original')
        
    def is_toxic(self, text):
        result = self.detoxify.predict(text)
        # Check if any of the toxicity categories exceed a certain threshold
        return result["toxicity"] > 0.7
    
    