from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import json
import uuid
import os
from datetime import datetime

app = FastAPI(title="Speed Run Complexidade Quiz API", description="API para um quiz educativo sobre complexidade de algoritmos.")

# ===============================================
# CONFIGURAÇÃO CORS
# ===============================================
origins = [
    "*", 
    "http://localhost",
    "http://localhost:8080", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ===============================================

# Caminhos dos arquivos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "speedrun.db")
QUESTIONS_FILE = os.path.join(BASE_DIR, "questions.json")

# Carregar perguntas
try:
    with open(QUESTIONS_FILE, "r") as f:
        questions = json.load(f)["questions"]
except FileNotFoundError:
    raise Exception(f"Erro: questions.json não encontrado em {QUESTIONS_FILE}")

# Configurar banco SQLite
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS Jogador (
            id_jogador INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS Partida (
            id_partida INTEGER PRIMARY KEY,
            data DATETIME NOT NULL,
            id_jogador INTEGER,
            FOREIGN KEY (id_jogador) REFERENCES Jogador(id_jogador)
        );
        CREATE TABLE IF NOT EXISTS Pergunta (
            id_pergunta INTEGER PRIMARY KEY,
            texto TEXT NOT NULL,
            opcoes TEXT NOT NULL,
            resposta_correta TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS Resposta (
            id_resposta INTEGER PRIMARY KEY,
            id_partida INTEGER,
            id_pergunta INTEGER,
            resposta_dada TEXT NOT NULL,
            correta BOOLEAN NOT NULL,
            FOREIGN KEY (id_partida) REFERENCES Partida(id_partida),
            FOREIGN KEY (id_pergunta) REFERENCES Pergunta(id_pergunta)
        );
        CREATE TABLE IF NOT EXISTS Pontuacao (
            id_pontuacao INTEGER PRIMARY KEY,
            id_partida INTEGER,
            pontos INTEGER NOT NULL,
            tempo_total REAL NOT NULL,
            FOREIGN KEY (id_partida) REFERENCES Partida(id_partida)
        );
    """)
    # Inserir perguntas no banco (se vazio)
    cursor.execute("SELECT COUNT(*) FROM Pergunta")
    if cursor.fetchone()[0] == 0:
        for q in questions:
            cursor.execute(
                "INSERT INTO Pergunta (texto, opcoes, resposta_correta) VALUES (?, ?, ?)",
                (q["code"], ",".join(q["options"]), q["correct_answer"])
            )
    conn.commit()
    conn.close()

init_db()

class Answer(BaseModel):
    id_pergunta: int
    resposta_dada: str

class ScoreSubmission(BaseModel):
    player_name: str
    answers: list[Answer]
    tempo_total: float

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/questions")
def get_questions():
    """Retorna o código e opções das perguntas (sem resposta correta) para o frontend jogar."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id_pergunta, texto, opcoes FROM Pergunta")
    
    questions_list = []
    for row in cursor.fetchall():
        questions_list.append({
            "id_pergunta": row[0],
            "code": row[1],
            "options": row[2].split(","), 
        })
    conn.close()
    return {"questions": questions_list}

@app.get("/questions_full")
def get_questions_full():
    """Retorna todas as perguntas, incluindo a resposta correta, para a tela de resumo."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id_pergunta, texto, opcoes, resposta_correta FROM Pergunta")
    
    questions_list = []
    for row in cursor.fetchall():
        questions_list.append({
            "id_pergunta": row[0],
            "code": row[1],
            "options": row[2].split(","),
            "correct_answer": row[3],
        })
    conn.close()
    return {"questions": questions_list}


@app.post("/launch")
def launch_game():
    session_id = str(uuid.uuid4())
    return {"session_id": session_id, "message": "Partida iniciada"}

@app.post("/score")
def submit_score(submission: ScoreSubmission):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Criar ou buscar jogador
    cursor.execute("SELECT id_jogador FROM Jogador WHERE nome = ?", (submission.player_name,))
    result = cursor.fetchone()
    if result:
        id_jogador = result[0]
    else:
        cursor.execute("INSERT INTO Jogador (nome) VALUES (?)", (submission.player_name,))
        id_jogador = cursor.lastrowid
    
    # Criar partida
    cursor.execute("INSERT INTO Partida (data, id_jogador) VALUES (?, ?)", (datetime.now(), id_jogador))
    id_partida = cursor.lastrowid
    
    # Verificar respostas e calcular pontos
    pontos = 0
    for answer in submission.answers:
        cursor.execute("SELECT resposta_correta FROM Pergunta WHERE id_pergunta = ?", (answer.id_pergunta,))
        correct_answer = cursor.fetchone()
        if not correct_answer:
            conn.close()
            raise HTTPException(status_code=400, detail=f"Pergunta {answer.id_pergunta} não encontrada")
        is_correct = correct_answer[0] == answer.resposta_dada
        pontos += 20 if is_correct else 0
        cursor.execute(
            "INSERT INTO Resposta (id_partida, id_pergunta, resposta_dada, correta) VALUES (?, ?, ?, ?)",
            (id_partida, answer.id_pergunta, answer.resposta_dada, is_correct)
        )
    
    # Bônus por tempo (máx. 75s para 5 perguntas)
    tempo_bonus = max(0, 75 - submission.tempo_total)
    pontos += int(tempo_bonus)
    
    # Salvar pontuação
    cursor.execute("INSERT INTO Pontuacao (id_partida, pontos, tempo_total) VALUES (?, ?, ?)",
                   (id_partida, pontos, submission.tempo_total))
    
    conn.commit()
    conn.close()
    return {"message": "Pontuação registrada", "total_score": pontos}

@app.get("/results")
def get_results():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT J.nome, P.data, Po.pontos, Po.tempo_total
        FROM Jogador J
        JOIN Partida P ON J.id_jogador = P.id_jogador
        JOIN Pontuacao Po ON P.id_partida = Po.id_partida
        ORDER BY Po.pontos DESC, Po.tempo_total ASC
    """)
    results = [{"player_name": row[0], "data": row[1], "pontos": row[2], "tempo_total": row[3]} for row in cursor.fetchall()]
    conn.close()
    return results

# ===============================================
# NOVO ENDPOINT DE ADMINISTRAÇÃO: DELETAR JOGADOR
# ===============================================
@app.delete("/player/{player_name}")
def delete_player(player_name: str):
    """Deleta um jogador e todos os seus registros de partidas, pontuações e respostas."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. Encontrar o id_jogador
    cursor.execute("SELECT id_jogador FROM Jogador WHERE nome = ?", (player_name,))
    result = cursor.fetchone()
    
    if not result:
        conn.close()
        raise HTTPException(status_code=404, detail=f"Jogador '{player_name}' não encontrado.")
    
    id_jogador = result[0]
    
    # 2. Encontrar todos os IDs de partida do jogador
    cursor.execute("SELECT id_partida FROM Partida WHERE id_jogador = ?", (id_jogador,))
    partida_ids = [row[0] for row in cursor.fetchall()]
    
    if partida_ids:
        # Cria uma string com placeholders (?, ?, ?) para a cláusula IN
        placeholders = ','.join('?' for _ in partida_ids)
        
        # 3. Deletar Pontuações (depende de Partida)
        cursor.execute(f"DELETE FROM Pontuacao WHERE id_partida IN ({placeholders})", partida_ids)
        
        # 4. Deletar Respostas (depende de Partida)
        cursor.execute(f"DELETE FROM Resposta WHERE id_partida IN ({placeholders})", partida_ids)
        
        # 5. Deletar Partidas
        cursor.execute(f"DELETE FROM Partida WHERE id_partida IN ({placeholders})", partida_ids)
    
    # 6. Deletar o Jogador
    cursor.execute("DELETE FROM Jogador WHERE id_jogador = ?", (id_jogador,))
    
    conn.commit()
    conn.close()
    
    return {"message": f"Jogador '{player_name}' e todos os seus dados foram removidos com sucesso."}