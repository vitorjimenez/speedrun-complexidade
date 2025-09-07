Speed Run Complexidade Quiz
Aplicação educacional gamificada para aprender complexidade de algoritmos.
Estrutura de Pastas
speedrun-complexidade/
├── app/
│   ├── __init__.py      # Opcional
│   ├── main.py         # API FastAPI
│   └── scores.json     # Gerado automaticamente
├── ui/
│   └── app.py          # Interface Streamlit
├── Dockerfile          # Ignorar (sem Docker)
├── questions.json      # Questões na raiz
├── requirements.txt    # Dependências
├── README.md           # Este arquivo
└── venv/               # Ambiente virtual

Como Rodar (Sem Docker)

Navegue para a pasta raiz:cd /d/projeto--001/speedrun-complexidade


Crie e ative venv:python -m venv venv
source venv/Scripts/activate


Instale dependências:pip install -r requirements.txt


Rode a API:uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


Em outro terminal, navegue para a raiz, ative venv, e rode a interface:cd /d/projeto--001/speedrun-complexidade
source venv/Scripts/activate
streamlit run ui/app.py


Acesse http://localhost:8501 no navegador.

Como Jogar

Abra http://localhost:8501.
Digite seu nome, escolha nível, responda 5 questões.
Veja explicações educativas e ranking.

Contribuir

Adicione questões em questions.json.
Melhore a interface em ui/app.py (ex: adicione gráficos).

Diferenciais: Interface gráfica (Streamlit), tempo afeta pontuação, feedback educativo para iniciantes.