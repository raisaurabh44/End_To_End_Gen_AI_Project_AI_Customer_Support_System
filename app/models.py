from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = "anonymous"
    
class ChatResponse(BaseModel):
    response: str
    user_id: Optional[str] = "anonymous"

class IngestRequest(BaseModel):
    text: str
    
class HealthResponse(BaseModel):
    status: str
    