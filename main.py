from fastapi import FastAPI
app = FastAPI(
    title="FIRETRACE",
    description="A satellite-based global fire intelligence platform",
    version="1.0.0")

@app.get("/")
def home():
    return {
        "project": "FIRETRACE",
        "status": "Online",
        "message": "Welcome to FIRETRACE!"}

@app.get("/health")
def health():
    return {
        "status": "healthy"}
