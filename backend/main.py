from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import ask_agent
from tools import analyze_financial_performance


app = FastAPI(
    title="FinAgent API",
    description="AI-powered financial analysis assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    answer: str


@app.get("/")
def root():
    return {
        "message": "FinAgent API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/summary")
def get_summary():
    analysis = analyze_financial_performance()

    return {
        "monthly_analysis": analysis["monthly_analysis"],
        "highest_revenue_month": analysis["highest_revenue_month"],
        "highest_profit_month": analysis["highest_profit_month"],
        "highest_profit_margin_month": analysis["highest_profit_margin_month"],
        "average_monthly_profit": analysis["average_monthly_profit"],
    }


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):

    answer = ask_agent(request.question)

    return {
        "answer": answer
    }