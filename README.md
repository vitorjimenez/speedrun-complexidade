🚀 Speed Run Complexidade Quiz
🎯 Objetivo
Uma plataforma web gamificada para ensinar complexidade de algoritmos (Big O, grafos, estruturas de dados) com um quiz interativo. Jogadores respondem até 10 perguntas em 15 segundos cada, com pontuações salvas em um banco de dados e ranking.
🛠️ Stack Utilizada

Linguagem: 🐍 Python 3.8+
Framework: ⚡ FastAPI (backend)
Ferramentas: 📂 Git, GitHub, VS Code
Ambiente: 🧪 Virtualenv (venv)
Testes: 🔍 Requisições HTTP (navegador, curl)

📂 Estrutura do Projeto
speedrun-complexidade/
├── app/
│   ├── __init__.py  # Pacote Python
│   ├── main.py      # API com /health
├── requirements.txt # Dependências
├── README.md       # Instruções

🚀 Como Rodar Localmente
Pré-requisitos

Python 3.8+ (python.org)
Git (git-scm.com)
VS Code (opcional, code.visualstudio.com)

Passos

Clone o repositório:
git clone https://github.com/SEU_USUARIO/speedrun-complexidade.git
cd speedrun-complexidade


Crie e ative o ambiente virtual:
python -m venv venv
source venv/Scripts/activate  # Git Bash (Windows)


Instale dependências:
pip install -r requirements.txt


Rode o FastAPI:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


Teste o endpoint /health:

No navegador: http://localhost:8000/health
Ou com curl:curl http://localhost:8000/health


Resposta esperada:{"status": "ok"}

👥 Integrantes

Nicolas Sanana

Vinicius Freire Cerqueira

Vitor

📝 Notas

Fase 1: Setup inicial com endpoint /health. Futuras fases trarão rotas /launch, /score, banco SQLite e autenticação.
Diferencial: Quiz gamificado com storytelling para ensinar complexidade de forma divertida! 🎮
