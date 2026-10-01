from fastapi import FastAPI

app = FastAPI(
    title="AgentFlow",
    description="Agentic Research Platform",
    version="0.1.0",

)

@app.get("/api/health")
async def heaith_check():
    return {
        "status" : "healthy",
        "service" : "AgentFlow backend",
    }