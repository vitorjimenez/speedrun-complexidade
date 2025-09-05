import requests
import time
import json

API_URL = "http://localhost:8000"  # URL da API rodando localmente

def get_random_question(level=None):
    params = {"level": level} if level else {}
    response = requests.get(f"{API_URL}/questions/random", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao pegar questão:", response.text)
        return None

def submit_answer(question_id, answer, time_taken):
    data = {"question_id": question_id, "answer": answer, "time_taken": time_taken}
    response = requests.post(f"{API_URL}/submit_answer", json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao submeter resposta:", response.text)
        return None

def save_score(player_name, total_score):
    data = {"player_name": player_name, "score": total_score}
    response = requests.post(f"{API_URL}/save_score", json=data)
    if response.status_code == 200:
        print("Pontuação salva!")
    else:
        print("Erro ao salvar pontuação:", response.text)

def get_ranking():
    response = requests.get(f"{API_URL}/ranking")
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao pegar ranking:", response.text)
        return []

def play_quiz():
    player_name = input("Digite seu nome: ")
    level = input("Escolha o nível (beginner, intermediate, advanced) ou Enter para aleatório: ").strip() or None
    total_score = 0
    num_questions = 5  # Número de questões por partida (ajustável)

    for _ in range(num_questions):
        question = get_random_question(level)
        if not question:
            return

        print("\nNível:", question["level"])
        print("Código:\n", question["code"])
        print("Opções:")
        for idx, opt in enumerate(question["options"]):
            print(f"{chr(65 + idx)}: {opt}")  # A, B, C, D

        start_time = time.time()
        answer = input("Sua resposta (ex: O(n)): ").strip()
        time_taken = time.time() - start_time

        result = submit_answer(question["id"], answer, time_taken)
        if result:
            if result["correct"]:
                print("Correto! Pontos:", result["score"])
                total_score += result["score"]
            else:
                print("Errado!")
            print("Explicação:", result["explanation"])

    print("\nPontuação total:", total_score)
    save_score(player_name, total_score)

    print("\nRanking Top 10:")
    ranking = get_ranking()
    for idx, entry in enumerate(ranking, 1):
        print(f"{idx}. {entry['player_name']}: {entry['score']}")

if __name__ == "__main__":
    play_quiz()