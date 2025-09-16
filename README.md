# 🚀 Speed Run Complexidade Quiz
Resumo: Plataforma web educativa e gamificada para ensinar complexidade de algoritmos (Big O, grafos, estruturas de dados) por meio de um quiz interativo. Jogadores respondem até 10 perguntas em 15 segundos cada, com pontuações salvas em um banco de dados e ranking.

## 🎯 Objetivo
O Speed Run de Complexidade é um quiz interativo que ensina conceitos de complexidade de algoritmos de forma divertida. Os jogadores avançam por fases, respondendo perguntas sobre notação Big O, com o objetivo de aprender enquanto competem. A Fase 1 estabelece a base técnica com um endpoint /health para verificar a API.

## 👨‍💻 Tecnologias Utilizadas

Python 3.8+ - Linguagem principal
FastAPI - Framework para a API
Uvicorn - Servidor ASGI
Git/GitHub - Controle de versão
VS Code - Editor de código
Virtualenv - Isolamento de dependências


## 🗂️ Estrutura do Projeto
📦 speedrun-complexidade
├── 📁 app
│   ├── __init__.py      # Pacote Python
│   ├── main.py          # API com endpoint /health
├── requirements.txt      # Dependências
├── README.md            # Documentação


## ⚙️ Como Executar
✅ Rodando Localmente

Clone o repositório:
git clone https://github.com/SEU_USUARIO/speedrun-complexidade.git
cd speedrun-complexidade


Verifique o Python (3.8+ necessário):
python --version


## Crie e ative o ambiente virtual:
python -m venv venv
source venv/Scripts/activate  # Git Bash (Windows) ou


### Instale dependências:
pip install -r requirements.txt


## Rode a API:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


## Teste o endpoint /health:

No navegador: http://localhost:8000/health
Ou com curl:curl http://localhost:8000/health


Resposta esperada:{"status": "ok"}






## 💡 Acesse http://localhost:8000/docs para ver a documentação da API.


## 👥 Equipe



Nome
GitHub
Função



Nicolas Silva
 [@nicolas](https://github.com/nicolassantana42)
Desenvolvedor


Vinicius Cerqueira
[@vinicius](https://github.com/ViniCerqueira/ViniCerqueira)
Desenvolvedor


Vitor Jimenez
[@vitorjimenez](https://github.com/vitorjimenez)
Desenvolvedor



## 📝 Notas

Fase 1: Configuração inicial com endpoint /health. As próximas fases adicionarão rotas /launch, /score, banco SQLite e autenticação.
Diferencial: Quiz gamificado com storytelling para ensinar complexidade de algoritmos de forma acessível! 🎮


## 🐞 Solucionando Problemas



Problema
Solução



"uvicorn: command not found"
Ative o venv e reinstale: pip install -r requirements.txt


Porta 8000 ocupada
Use outra porta: uvicorn app.main:app --host 0.0.0.0 --port 8001


Erro no Git
Configure: git config --global user.name "Seu Nome" e user.email



📄 Licença
MIT License — use, estude e adapte este projeto livremente.
