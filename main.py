from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from ai.gemini_client import ask_gemini  # Gemini model handler

app = FastAPI()

# Serve static files like CSS/JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set template folder for HTML pages
templates = Jinja2Templates(directory="templates")

# Request model for POST requests
class CodeRequest(BaseModel):
    code: str

# Home page route
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Dynamic chapter route (arrays, linkedlists, etc.)
@app.get("/{chapter}")
async def chapter(request: Request, chapter: str):
    try:
        return templates.TemplateResponse(f"{chapter}.html", {"request": request})
    except:
        return templates.TemplateResponse("404.html", {"request": request})

# POST route for AI-based explanation
@app.post("/api/explain")
async def explain_code(code_request: CodeRequest):
    explanation = await asyncio.to_thread(ask_gemini, f"Please explain this Java code:\n{code_request.code}")
    return JSONResponse({"explanation": explanation})
