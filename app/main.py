from fastapi import FastAPI
from pydantic import BaseModel
import json
import uuid
import os

app = FastAPI(title="Speed Run Complexidade Quiz API", description="API para um quiz educativo sobre complexidade de algoritmos.")

# Caminho absoluto para questions.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_FILE = os.path.join(BASE_DIR, "questions.json")

# Carregar perguntas
try:
    with open(QUESTIONS_FILE, "r") as f:
        questions = json.load(f)["questions"]
except FileNotFoundError:
    raise Exception(f"Erro: questions.json não encontrado em {QUESTIONS_FILE}")

# Estrutura para pontuação (em memória, para Fase 2)
scores = []

class ScoreSubmission(BaseModel):
    player_name: str
    score: int

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/launch")
def launch_game():
    session_id = str(uuid.uuid4())  # Gera ID único para a sessão
    return {"session_id": session_id, "message": "Partida iniciada"}

@app.post("/score")
def submit_score(submission: ScoreSubmission):
    scores.append({"player_name": submission.player_name, "score": submission.score})
    return {"message": "Pontuação registrada", "total_score": submission.score}