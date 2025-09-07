import streamlit as st
import requests
import time
import json

API_URL = "http://localhost:8000"

def get_random_question(level=None):
    try:
        params = {"level": level} if level else {}
        response = requests.get(f"{API_URL}/questions/random", params=params)
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.ConnectionError:
        st.error("Erro: A API não está rodando. Inicie com 'uvicorn app.main:app --host 0.0.0.0 --port 8000'.")
        return None

def submit_answer(question_id, answer, time_taken):
    try:
        data = {"question_id": question_id, "answer": answer, "time_taken": time_taken}
        response = requests.post(f"{API_URL}/submit_answer", json=data)
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.ConnectionError:
        st.error("Erro: A API não está rodando.")
        return None

def save_score(player_name, total_score):
    try:
        data = {"player_name": player_name, "score": total_score}
        requests.post(f"{API_URL}/save_score", json=data)
        st.success("Pontuação salva!")
    except requests.exceptions.ConnectionError:
        st.error("Erro: Não foi possível salvar a pontuação. API desligada?")

def get_ranking():
    try:
        response = requests.get(f"{API_URL}/ranking")
        return response.json() if response.status_code == 200 else []
    except requests.exceptions.ConnectionError:
        st.error("Erro: Não foi possível carregar o ranking. API desligada?")
        return []

st.set_page_config(page_title="Speed Run Complexidade", page_icon="🚀", layout="wide")

with st.sidebar:
    st.title("🚀 Speed Run Complexidade")
    st.markdown("**Aprenda sobre complexidade de algoritmos de forma divertida!**")
    st.info("**O que é Big O?** É uma forma de medir quanto tempo um programa leva conforme a entrada cresce. Exemplo: 'O(n)' significa que o tempo cresce com o tamanho da entrada (n).")
    st.markdown("### Níveis:")
    st.markdown("- **Beginner**: Loops simples, como contar números.")
    st.markdown("- **Intermediate**: Algoritmos como busca binária.")
    st.markdown("- **Advanced**: Coisas avançadas, como grafos!")
    st.markdown("**Dica**: Responda rápido para mais pontos! 🎯")

st.header("🎉 Quiz Educativo de Complexidade de Algoritmos")
st.markdown("Teste seus conhecimentos e aprenda com explicações simples!")

player_name = st.text_input("Digite seu nome:", placeholder="Seu Nome")
level = st.selectbox("Escolha o nível:", options=[None, "beginner", "intermediate", "advanced"], format_func=lambda x: "Aleatório" if x is None else x.capitalize())

if player_name:
    if "quiz_state" not in st.session_state:
        st.session_state.quiz_state = {
            "questions_answered": 0,
            "total_score": 0,
            "current_question": None,
            "start_time": None
        }

    state = st.session_state.quiz_state

    if state["questions_answered"] < 5:
        if state["current_question"] is None:
            question = get_random_question(level)
            if question:
                state["current_question"] = question
                state["start_time"] = time.time()
                st.success(f"Questão {state['questions_answered'] + 1}/5 - Nível: {question['level'].capitalize()}")

                st.code(question["code"], language="python")

                selected_answer = st.radio("Qual é a complexidade?", question["options"])

                if st.button("Enviar Resposta"):
                    time_taken = time.time() - state["start_time"]
                    result = submit_answer(question["id"], selected_answer, time_taken)
                    if result:
                        if result["correct"]:
                            st.balloons()
                            st.success(f"Correto! Você ganhou {result['score']} pontos!")
                            state["total_score"] += result["score"]
                        else:
                            st.error("Errado! Vamos aprender com isso.")
                        st.info(f"**Explicação:** {result['explanation']}")
                        state["questions_answered"] += 1
                        state["current_question"] = None
        else:
            st.warning("Carregando próxima questão...")
    else:
        st.success(f"Quiz concluído! Sua pontuação: {state['total_score']} pontos")
        save_score(player_name, state["total_score"])
        st.session_state.quiz_state = {}

        st.header("🏆 Ranking dos Melhores")
        ranking = get_ranking()
        if ranking:
            for idx, entry in enumerate(ranking, 1):
                st.markdown(f"{idx}. **{entry['player_name']}**: {entry['score']} pontos")
        else:
            st.info("Seja o primeiro no ranking! 😊")
else:
    st.warning("Digite seu nome para começar!")