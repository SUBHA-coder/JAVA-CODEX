from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from ai.groq_client import ask_llama

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

class CodeRequest(BaseModel):
    code: str

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chapter/{topic}")
async def chapter(request: Request, topic: str):
    return templates.TemplateResponse(f"{topic}.html", {"request": request})

@app.post("/api/explain")
async def explain_code(code_request: CodeRequest):
    explanation = await ask_llama(f"Please explain this Java code:\n{code_request.code}")
    return JSONResponse({"explanation": explanation})