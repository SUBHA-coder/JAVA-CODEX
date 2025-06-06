# main.py (only AI logic part updated)

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import asyncio
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from ai.llama_client import ask_llama  # Updated to llama client

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class CodeRequest(BaseModel):
    code: str

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/{chapter}")
async def chapter(request: Request, chapter: str):
    try:
        return templates.TemplateResponse(f"{chapter}.html", {"request": request})
    except:
        return templates.TemplateResponse("404.html", {"request": request})

@app.post("/api/explain")
async def explain_code(code_request: CodeRequest):
    explanation = await asyncio.to_thread(ask_llama, f"Please explain this Java code:\n{code_request.code}")
    return JSONResponse({"explanation": explanation})
