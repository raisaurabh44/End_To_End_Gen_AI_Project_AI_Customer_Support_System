import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from app.config import LLM_MODEL, MAX_TOKENS

class LLM:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL) 
        self.model = AutoModelForCausalLM.from_pretrained(LLM_MODEL, torch_dtype=torch.float32) 
        
    def generate(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_new_tokens=MAX_TOKENS, temperature=0.2)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    