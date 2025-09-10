from fastapi import FastAPI

app = FastAPI(title="Speed Run Complexidade Quiz API", description="API para um quiz educativo sobre complexidade de algoritmos.")

@app.get("/health")
def health_check():
    return {"status": "ok"}