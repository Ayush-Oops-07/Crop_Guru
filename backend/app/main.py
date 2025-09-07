import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Crop-Guru API", version="0.1")

origins = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    message: str
    crop: str | None = None
    locale: str | None = "en-IN"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/advice")
async def advice(q: Query):
    # STEP 4 will replace this with LLM + rules.
    tip = "Ensure proper irrigation and check soil moisture."
    crop = q.crop or "your crop"
    return {"reply": f"For {crop}: {tip}", "echo": q.message}

@app.post("/detect")
async def detect(image: UploadFile = File(...)):
    # STEP 6 will run YOLO here. For now: stub.
    return {"pest": "unknown", "confidence": 0.0, "note": "Model pending (demo stub)."}
