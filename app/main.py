from fastapi import FastAPI, Request, Form 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from slowapi.middleware import SlowAPIMiddleware
from app.models import ChatRequest, ChatResponse
from app.orchestrator import Orchestrator
from app.rate_limit import limiter

app = FastAPI(title="AI Customer Support API")
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

templates = Jinja2Templates(directory="app/templates")
orchestrator = Orchestrator()

chat_history = []

@app.get("/", response_class=HTMLResponse)
async def chat_ui(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request, "messages": chat_history})

@app.post("/", response_class = HTMLResponse)
async def chat_post(request: Request, message: str = Form(...)):
    response = orchestrator.handle(message)
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "bot", "content": response})
    return templates.TemplateResponse("chat.html", {"request": request, "messages": chat_history})

@app.post("/chat", response_model=ChatResponse)
@limiter.limit("10/minute")
async def chat_api(request: Request , data: ChatRequest):
    response = orchestrator.handle(data.message)
    return ChatResponse(response=response, user_id=data.user_id)

@app.get("/health")
async def health():
    return {"status": "ok"}


    