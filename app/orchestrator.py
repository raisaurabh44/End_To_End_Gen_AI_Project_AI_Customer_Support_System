from app.retriever import Retriever
from app.llm import LLM
from app.guardrails import Guardrails
from app.cache import Cache
from app.config import CONFIDENCE_THRESHOLD

class Orchestrator:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLM()
        self.guardrails = Guardrails()
        self.cache = Cache()
    
    def handle(self, query):
        # check cache first
        cached = self.cache.get(query)
        if cached:
            return cached
        # retrieve relevant data
        docs = self.retriever.retrieve(query)
        
        if len(docs) == 0:
            return "Escalating to human support: No relevant documents found."
        
        context = "\n".join(docs)
        
        prompt = f"""
        Answer only from context below.
        If unsure, say escalate to human support.
        
        Context:
        {context}
        
        Question:
        {query}
        
        Answer:
        """
        response = self.llm.generate(prompt)
        if self.guard.is_toxic(response):
            return "Escalated due to policy violation."
        
        self.cache.set(query, response)
        return response