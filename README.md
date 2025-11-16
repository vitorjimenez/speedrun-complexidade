# 🚀 Speed Run Complexidade Quiz

**Quiz gamificado para ensinar Notação Big O com gráficos dinâmicos, revisão visual e ranking.**

---

## 🎯 Identificação do Projeto

| Detalhe | Valor |
|:---|:---|
| **Nome do Jogo/Plugin** | **Speed Run Complexidade Quiz** |
| **Área da Disciplina** | **Computabilidade e Complexidade de Algoritmos** |

### 👥 Grupo de Desenvolvimento

| Nome | RGM |
|:---|:---|
| **Nicolas Silva** | 123456789 |
| **Vinicius Cerqueira** | 987654321 |
| **Vitor Jimenez** | 567890123 |

---

## 🎯 Objetivo Pedagógico

O jogo trabalha os **conceitos de notação Big O (tempo e espaço)**. O objetivo é que o aluno:

* Aprenda a **analisar trechos de código real** (Python).
* Identifique padrões de crescimento de complexidade.
* Escolha a notação Big O correta sob **pressão de tempo**.
* Pratique **análise rápida**, **pensamento crítico** e **compreensão visual** do impacto de algoritmos através dos gráficos.

---

## 🎮 Descrição do Jogo

O quiz é uma "corrida" contra o tempo, com foco em gamificação:

* **Regras:** 5 perguntas sobre complexidade de código Python, com **15 segundos por pergunta**.
* **Duração Média:** 60–75 segundos.

### 📢 Sistema de Feedback

| Tipo | Descrição |
|:---|:---|
| **Imediato** | Timer regressivo e alerta visual nos 5 segundos finais. |
| **Final** | Exibição da pontuação total (acertos + bônus de tempo) e posição no ranking. |
| **Revisão** | Após o quiz, o jogador revisa o código, a resposta correta e os **gráficos dinâmicos de tempo e espaço** para cada algoritmo. |

---

## 📚 Conteúdo Relacionado à Disciplina

| Tópico do Plano de Ensino | Como o Jogo Ajuda |
|:--------------------------|:-------------------|
| **Notação Assintótica (Big O)** | O aluno lê o código e escolhe a complexidade correta: `O(n)`, `O(n²)`, etc. |
| **Análise de Loops** | Perguntas abordam estruturas de controle como `for`, `while` e _loops_ aninhados. |
| **Busca Binária** | Demonstra visualmente a eficiência de `O(log n)` com código funcional. |
| **Merge Sort** | Apresenta o custo de `O(n log n)` com exemplos de recursão. |
| **Complexidade de Espaço** | Gráfico dedicado mostra a diferença entre complexidade constante (`O(1)`) e linear (`O(n)`). |

---

## 🧮 Critérios de Pontuação

| Item | Pontuação | Observação |
|:---|:---|:---|
| **Acerto** | **+20 pontos** | Máximo de 100 pontos na base. |
| **Bônus de Tempo** | **+1 ponto** por segundo restante | Máximo de 75 pontos de bônus. |
| **Nota Final** | `total_score` | Soma da Base + Bônus (ex: 115). |
| **Aprovação** | Mínimo de **60 pontos** | Limite pedagógico para sucesso. |

### ❌ Penalidades

* **Tempo Esgotado:** 0 pontos na pergunta.
* **Erro:** 0 pontos na pergunta (sem penalidade extra).

---

## 🧪 Testes Realizados

| Caso | Descrição | Resultado |
|:-----|:----------|:----------|
| 1 | 5 acertos em 60 segundos | `115` (100 base + 15 bônus) |
| 2 | 3 acertos + 2 erros em 70 segundos | `65` (60 base + 5 bônus) |
| 3 | Tempo esgotado em 1 pergunta | `80` (4 acertos) |
| 4 | Token inválido na API | `401 Unauthorized` |
| 5 | Revisão com gráficos | Gráficos desenhados corretamente, comprovando a notação. |

---

## 🎥 Roteiro de Demonstração (Vídeo)

**Link do vídeo:** [https://youtu.be/XXXXXXX](https://youtu.be/XXXXXXX) *(Lembre-se de substituir pelo seu link real)*

| Tempo | Conteúdo |
|:------|:---------|
| **[0:00 - 0:15]** | Introdução ao problema pedagógico e a motivação para o Speed Run. |
| **[0:15 - 0:40]** | Apresentação da solução: quiz cronometrado, código real e gráficos de crescimento. |
| **[0:40 - 1:40]** | **Demonstração em Tempo Real** do jogo. Ênfase no `O(n²)` e como o gráfico "explode!". |
| **[1:40 - 2:20]** | Foco na **Revisão Visual** (código, resposta, gráficos de tempo/espaço). |
| **[2:20 - 2:50]** | Destaque para o **Ranking** (motivação) e as tecnologias utilizadas. |
| **[2:50 - 3:00]** | Conclusão: a transformação da teoria de Big O em prática. |

---

## 👨‍💻 Tecnologias

| Tecnologia | Uso |
|:----------|:-----|
| **Python + FastAPI** | Backend robusto, provendo a API REST. |
| **SQLite** | Banco de dados leve para armazenar o ranking. |
| **HTML + Tailwind + Chart.js** | Frontend moderno, com gráficos dinâmicos. |
| **Uvicorn** | Servidor ASGI para execução local. |

---

## 🗂️ Estrutura do Projeto

A organização dos diretórios e arquivos é a seguinte:

speedrun-complexidade/├── app/│   └── main.py              # 🚀 API Principal (FastAPI + SQLite)├── index.html               # 🎮 Interface do Jogo (Quiz)├── results.html             # 🏆 Página de Ranking├── script.js                # 🧠 Lógica do Quiz e Geração de Gráficos├── style.css                # 🎨 Estilos da Aplicação (Opcional)├── questions.json           # 📜 Perguntas com Big O de tempo e espaço├── database_schema.json     # 🏗️ Modelo Relacional do Banco├── speedrun.db              # 💾 Banco de Dados SQLite (Gerado automaticamente)├── relatorio_pedagogico.md  # 📝 Relatório Pedagógico Completo├── fase_final_demo.mp4      # 🎬 Vídeo de Demonstração├── requirements.txt         # 📦 Dependências do Python├── README.md                # 📖 Este Arquivo└── venv/                    # 🚫 Ambiente Virtual
---

## ⚙️ Como Executar (Passo a Passo)

### 1. Clone o Repositório

```bash
git clone [https://github.com/SEU_USUARIO/speedrun-complexidade.git](https://github.com/SEU_USUARIO/speedrun-complexidade.git)
cd speedrun-complexidade
```

### 2. Crie e Ative o Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate.bat  # Windows (cmd)
```
### 3. Instale as Dependências
```bash
pip install -r requirements.txt

```
### 4. Rode a API
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Abra o Jogo no Navegador
http://localhost:8000/index.html

### Rotas Principais
Rota,Método,Função,Observação
/health,GET,Verifica status da API,Requer API_TOKEN
/launch,POST,Inicia partida,Retorna session_id
/score,POST,Envia respostas,Calcula pontuação e salva ranking
/results,GET,Ranking,Lista os jogadores
/questions,GET,Perguntas (frontend),Não inclui a resposta correta
/questions_full,GET,Perguntas completas,Rota administrativa para revisão

Variável,Valor Padrão,Uso
API_TOKEN,super-secret-complexidade-token,Chave de autenticação em todas as rotas.

### 🛑 Solução de Problemas
Problema Comum,Solução
uvicorn not found,Execute pip install uvicorn
Porta 8000 ocupada,Use --port 8001 no comando uvicorn
Erro de CORS,O frontend (script.js) já possui a lógica de headers.
speedrun.db não existe,O banco é gerado automaticamente na primeira execução da API.

### 🤝 Contato
Nome,GitHub,Função Principal
Nicolas Silva,@nicolas,Full Stack + Gráficos
Vinicius Cerqueira,@vinicius,Backend + Banco
Vitor Jimenez,@vitor,Frontend + UX/UI
