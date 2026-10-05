    # FinAgent

> AI-powered financial analysis assistant using Qwen3, Ollama, FastAPI and React.

FinAgent is an AI-powered financial analysis assistant that allows users to ask financial questions in natural language and receive data-backed, business-friendly answers.

The system combines an LLM for natural-language understanding and tool selection with deterministic Python functions for financial calculations.

---

## 🚀 Features

- Natural-language financial queries
- AI-powered intent recognition and tool selection
- Deterministic financial calculations using Python
- Revenue, expense and profit analysis
- Profit margin calculation
- Month-to-month growth analysis
- Overall financial performance analysis
- Missing-data handling without fabricating values
- Interactive React dashboard
- Revenue vs Profit visualization
- Local LLM execution using Ollama and Qwen3

---

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
               React Dashboard
                      │
                      ▼
                FastAPI API
                      │
                      ▼
              FinAgent Agent
                      │
                      ▼
                Qwen3 / Ollama
                      │
               Tool Selection
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
     Data Tools   Calculation   Analysis
          │           │           │
          └───────────┼───────────┘
                      ▼
              Financial Dataset
                      │
                      ▼
                Tool Results
                      │
                      ▼
                 Qwen3
                      │
                      ▼
              Final AI Response
                      │
                      ▼
               React Dashboard