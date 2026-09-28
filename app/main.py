from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import run_agent, self_improve_agent
from app.memory import init_db, get_recent_logs, get_success_rate

app = FastAPI(title="AI Automation Agent", version="1.0.0")
init_db()

class RequestPayload(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "AI Automation Agent is running",
        "endpoints": {
            "agent": "POST /agent",
            "logs": "GET /logs",
            "stats": "GET /stats",
            "improve": "GET /improve"
        }
    }

@app.post("/agent")
def agent_endpoint(payload: RequestPayload):
    """Process user request through AI agent."""
    response = run_agent(payload.text)
    return response

@app.get("/logs")
def logs_endpoint(limit: int = 10):
    """Get recent agent logs."""
    logs = get_recent_logs(limit)
    return {
        "count": len(logs),
        "logs": logs
    }

@app.get("/stats")
def stats_endpoint():
    """Get agent performance statistics."""
    return get_success_rate()

@app.get("/improve")
def improve_endpoint():
    """Get self-improvement suggestions."""
    return self_improve_agent()