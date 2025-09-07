🚀 Speed Run: Quiz de Complexidade de Algoritmos
Bem-vindo(a) ao Speed Run, um aplicativo educacional gamificado para você testar e aprimorar seus conhecimentos sobre a complexidade de algoritmos (notação Big O).

Este projeto combina um quiz dinâmico com feedback educativo, perfeito para quem está começando ou precisa revisar o tema.

✨ Funcionalidades Principais
Interface Gráfica com Streamlit: Uma experiência de usuário intuitiva e amigável.

Aprendizado Gamificado: O tempo de resposta afeta sua pontuação, adicionando um elemento de "speed run".

Feedback Educativo: Receba explicações detalhadas sobre as respostas, ajudando a consolidar o aprendizado.

Ranking de Jogadores: Compare sua pontuação com a de outros jogadores e suba no ranking.

Perguntas Customizáveis: O quiz utiliza um arquivo JSON, facilitando a adição de novas perguntas.

💻 Como Rodar o Projeto
Siga estes passos para colocar o quiz para rodar na sua máquina local.

Pré-requisitos
Certifique-se de ter o Python e o pip instalados.

1. Clonar o Repositório
Comece clonando o projeto para sua máquina:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Substitua o link pelo endereço correto do seu repositório.

2. Configurar o Ambiente
É altamente recomendado criar e ativar um ambiente virtual para isolar as dependências do projeto.

Bash

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate

# Ativa o ambiente virtual (macOS/Linux)
source venv/bin/activate
Em seguida, instale todas as bibliotecas necessárias:

Bash

pip install -r requirements.txt
3. Executar as Aplicações
O projeto é dividido em duas partes: a API (backend) e a interface (frontend). Você precisará rodar ambas em terminais separados.

Terminal 1: Iniciar a API com FastAPI
Bash

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
A API será responsável por gerenciar as pontuações e a lógica do quiz.

Terminal 2: Iniciar a Interface com Streamlit
Certifique-se de que o ambiente virtual está ativado.

Bash

streamlit run ui/app.py
Acesse a aplicação no seu navegador em: http://localhost:8501.

🎮 Como Jogar
Acesse http://localhost:8501 no seu navegador.

Digite seu nome e escolha um nível de dificuldade.

Responda às 5 perguntas de Big O no tempo limite.

Após a rodada, confira seu feedback educativo e veja sua posição no ranking.

📂 Estrutura do Projeto
Bash

speedrun-complexidade/
├── app/
│   ├── main.py             # Lógica da API (FastAPI)
│   └── scores.json         # Ranking de pontuações
├── ui/
│   └── app.py              # Interface do quiz (Streamlit)
├── questions.json          # Banco de dados de perguntas e respostas
└── requirements.txt        # Dependências do projeto
🤝 Como Contribuir
Sua ajuda é bem-vinda! Se você quiser melhorar o projeto, aqui estão algumas ideias:

Adicionar Novas Perguntas: Basta incluir novos objetos no arquivo questions.json.

Melhorar a Interface: Faça alterações no arquivo ui/app.py (por exemplo, adicione gráficos de desempenho ou novos elementos visuais).

Correção de Bugs: Se encontrar algum problema, abra uma issue e, se possível, um pull request.
