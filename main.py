from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine.main_recommendation_pipeline import run_recommendation
from ai_engine.simulation_engine import run_simulation
app = FastAPI(
    title="AI Mentor Recommendation Engine",
    version="1.0"
)


# ----------------------------
# Request Schema
# ----------------------------
class StudentInput(BaseModel):
    math: float
    science: float
    english: float
    logical_score: float
    creativity_score: float
    scientific_interest: float
    communication: float
    leadership: float
    stress_level: int
    risk_level: int
    budget: int
    location: str
    education_level: str


# ----------------------------
# Health Check
# ----------------------------
@app.get("/")
def root():
    return {"message": "AI Mentor API is running 🚀"}


# ----------------------------
# Recommendation Endpoint
# ----------------------------
@app.post("/recommend")
def recommend(student: StudentInput):
    result = run_recommendation(student.dict())
    return result

@app.post("/simulate")
def simulate(data: dict):
    base_input = data.get("base_profile")
    overrides = data.get("overrides", {})

    if not base_input:
        return {"error": "base_profile is required"}

    result = run_simulation(base_input, overrides)

    return result