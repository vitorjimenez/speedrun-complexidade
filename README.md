Speed Run Complexidade Quiz
Objetivo
Desenvolver uma plataforma web educativa e gamificada para ensinar conceitos de complexidade de algoritmos (Big O, grafos, estruturas de dados) por meio de um quiz interativo. Os jogadores avançam por fases, respondem até 10 perguntas em 15 segundos cada, e suas pontuações são salvas em um banco de dados, com ranking.
Stack Utilizada

Linguagem: Python 3.8+
Framework: FastAPI (backend)
Ferramentas: Git, GitHub, VS Code
Ambiente: Virtualenv (venv)
Testes: Requisições HTTP (ex: curl, navegador)

Estrutura Inicial do Projeto
speedrun-complexidade/
├── app/
│   ├── __init__.py  # Pacote Python
│   ├── main.py      # API FastAPI com endpoint /health
├── requirements.txt  # Dependências
├── README.md        # Instruções

Como Rodar Localmente
Pré-requisitos

Python 3.8+ instalado (python.org).
Git instalado (git-scm.com).
VS Code (opcional, para edição).

Passos

Clone o repositório:
git clone https://github.com/SEU_USUARIO/speedrun-complexidade.git
cd speedrun-complexidade


Crie e ative o ambiente virtual:
python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)
# Ou: .\venv\Scripts\Activate.ps1 (PowerShell)


Instale dependências:
pip install -r requirements.txt


Rode o serviço FastAPI:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


Teste o endpoint /health:

Abra o navegador ou use curl:curl http://localhost:8000/health


Resposta esperada:{"status": "ok"}





Integrantes do Grupo

Nicolas (substitua pelos nomes reais do grupo, ex: Nicolas Silva)
[Adicione outros membros]

Notas

Este é o setup inicial (Fase 1). Futuras fases incluirão rotas /launch, /score, banco SQLite, e autenticação.
O projeto será gamificado, com storytelling para engajar iniciantes em complexidade de algoritmos.
