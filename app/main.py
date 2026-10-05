from fastapi import FastAPI

app = FastAPI(title="Machine Service")


@app.get("/machine")
def health():
    return {
        "service": "machine-service",
        "status": "running"
    }
