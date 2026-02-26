import faiss 
import numpy as np 
from sentence_transformers import SentenceTransformer
from app.config import EMBED_MODEL, TOP_K

class Retriever:
    def __init__(self):
        self.embedder = SentenceTransformer(EMBED_MODEL)
        self.index = faiss.IndexFlatL2(384)  # Assuming embedding dimension is 384
        self.documents = [] # To store original documents
        self.load_documents()
    
    def load_documents(self):
        # Load your documents and their embeddings here
        # For example, you can read from a file or database
        # Here we will just add some dummy documents for demonstration
        with open("data/knowledge.txt") as f:
            docs = f.readlines()
            
            for doc in docs:
                doc = doc.strip()
                embedding = self.embedder.encode(doc)
                self.index.add(np.array([embedding], dtype=np.float32))
                self.documents.append(doc)
    
    def retrieve(self,query):
        query_vac = self.embedder.encode(query) 
        distances, indices = self.index.search(np.array([query_vac]), TOP_K) 
        return [self.documents[i] for i in indices[0]]
    
    def add_document(self, text):
        embedding = self.embedder.encode(text)
        self.index.add(np.array([embedding]))
        self.documents.append(text)  
        