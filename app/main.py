from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import random
import time
from typing import List, Dict
import os

app = FastAPI(title="Speed Run Complexidade Quiz API", description="API for a gamified educational app to learn algorithm complexities.")

# File paths
QUESTIONS_FILE = "questions.json"
SCORES_FILE = "scores.json"

# Load questions
with open(QUESTIONS_FILE, "r") as f:
    questions = json.load(f)["questions"]

# Load or initialize scores
if os.path.exists(SCORES_FILE):
    with open(SCORES_FILE, "r") as f:
        scores = json.load(f)
else:
    scores = []

class AnswerSubmission(BaseModel):
    question_id: int
    answer: str
    time_taken: float  # in seconds

class ScoreEntry(BaseModel):
    player_name: str
    score: int

@app.get("/questions/random", response_model=Dict)
def get_random_question(level: str = None):
    """
    Get a random question, optionally filtered by level (beginner, intermediate, advanced).
    """
    filtered_questions = [q for q in questions if level is None or q["level"] == level]
    if not filtered_questions:
        raise HTTPException(status_code=404, detail="No questions found for the specified level.")
    question = random.choice(filtered_questions)
    # Return question without the correct answer and explanation initially
    return {
        "id": question["id"],
        "code": question["code"],
        "options": question["options"],
        "level": question["level"]
    }

@app.post("/submit_answer")
def submit_answer(submission: AnswerSubmission):
    """
    Submit an answer for a question, get feedback, and calculate score.
    Score = 100 if correct and time < 30s, decreases by 2 per extra second, min 0. +50 bonus if correct.
    """
    question = next((q for q in questions if q["id"] == submission.question_id), None)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found.")
    
    is_correct = submission.answer == question["correct_answer"]
    base_score = 50 if is_correct else 0
    time_penalty = max(0, submission.time_taken - 30) * 2
    score = max(0, base_score + 50 - time_penalty) if is_correct else 0
    
    return {
        "correct": is_correct,
        "explanation": question["explanation"],
        "score": score
    }

@app.post("/save_score")
def save_score(entry: ScoreEntry):
    """
    Save a player's score to the ranking.
    """
    scores.append({"player_name": entry.player_name, "score": entry.score})
    scores.sort(key=lambda x: x["score"], reverse=True)
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f)
    return {"message": "Score saved successfully."}

@app.get("/ranking", response_model=List[Dict])
def get_ranking(top: int = 10):
    """
    Get the top rankings.
    """
    return scores[:top]