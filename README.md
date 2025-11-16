# 🚀 Speed Run Complexidade Quiz

**Quiz gamificado para ensinar Notação Big O com gráficos dinâmicos, revisão visual e ranking.**

---

## 🎯 Identificação do Plugin (Relatório Pedagógico)

**Nome do jogo/plugin:**  
**Speed Run Complexidade Quiz**

**Área da disciplina:**  
**Computabilidade e Complexidade de Algoritmos**

**Grupo:**  
- **Nicolas Silva** – RA: 123456789  
- **Vinicius Cerqueira** – RA: 987654321  
- **Vitor Jimenez** – RA: 567890123  

---

## 🎯 Objetivo Pedagógico

O jogo trabalha os **conceitos de notação Big O (tempo e espaço)**.  
O aluno aprende a **analisar trechos de código real**, identificar padrões de crescimento e escolher a complexidade correta sob pressão de tempo.  
Pratica **análise rápida**, **pensamento crítico** e **compreensão visual do impacto de algoritmos**.

---

## 🎮 Descrição do Jogo

- **Regras:** 5 perguntas com código Python. 15 segundos por pergunta. Escolha única.  
- **Duração média:** 60–75 segundos.  
- **Feedback:**  
  - **Imediato:** Timer vermelho, alerta de 5s.  
  - **Final:** Pontuação total (acertos + bônus).  
  - **Revisão:** Código, resposta correta, **gráficos de tempo e espaço**.

---

## 📚 Conteúdo Relacionado à Disciplina

| Tópico do Plano de Ensino | Como o Jogo Ajuda |
|---------------------------|-------------------|
| **Notação Assintótica (Big O)** | Aluno lê código → escolhe `O(n)`, `O(n²)`, etc. |
| **Análise de Loops** | Perguntas com `for`, `while`, loops aninhados |
| **Busca Binária** | Demonstra `O(log n)` com código funcional |
| **Merge Sort** | Mostra `O(n log n)` com recursão |
| **Complexidade de Espaço** | Gráfico separado: `O(1)` vs `O(n)` |

---

## 🧮 Critérios de Pontuação

- **20 pontos por acerto** → máx. 100  
- **Bônus de tempo:** 1 ponto por segundo restante (máx. 75s)  
- **Nota final:** `total_score` (ex: 115)  
- **Mínimo para aprovação:** 60 pontos  
- **Penalidades:**  
  - Tempo esgotado → 0 pontos na pergunta  
  - Erro → 0 pontos (sem penalidade extra)

---

## 🧪 Testes Realizados

| Caso | Descrição | Resultado |
|------|---------|---------|
| 1 | 5 acertos em 60s | `115` (100 + 15) |
| 2 | 3 acertos + 2 erros em 70s | `65` (60 + 5) |
| 3 | Tempo esgotado em 1 pergunta | `80` (4 acertos) |
| 4 | Token inválido | `401 Unauthorized` |
| 5 | Revisão com gráficos | Gráficos desenhados corretamente |

---

## 🎥 Roteiro de Demonstração (Vídeo)

**Link do vídeo:** [https://youtu.be/XXXXXXX](https://youtu.be/XXXXXXX) *(substitua pelo seu link)*

**Duração:** 3 minutos  
**Apresentador:** Apenas voz (sem aparecer)

### Roteiro:

> **[0:00 - 0:15]**  
> _"Por que criamos o Speed Run? Porque alunos decoram Big O, mas não entendem o impacto real."_

> **[0:15 - 0:40]**  
> _"Nosso jogo resolve isso com um quiz cronometrado, código real e gráficos que mostram o crescimento."_

> **[0:40 - 1:40]**  
> _[Mostre o jogo]_  
> _"O jogador tem 15 segundos por pergunta. Ganha 20 pontos por acerto + bônus por tempo. Veja o gráfico: O(n²) explode!"_

> **[1:40 - 2:20]**  
> _[Mostre revisão]_  
> _"Na revisão, o aluno vê o código, a resposta e os gráficos de tempo e espaço. Aprendizado visual."_

> **[2:20 - 2:50]**  
> _[Mostre ranking]_  
> _"O ranking motiva repetição. Usamos FastAPI, SQLite e Chart.js. Aprendemos full stack e design pedagógico."_

> **[2:50 - 3:00]**  
> _"O Speed Run transforma teoria em prática. Obrigado!"_

---

## 👨‍💻 Tecnologias

| Tecnologia | Uso |
|----------|-----|
| **Python + FastAPI** | Backend com API REST |
| **SQLite** | Banco de dados leve |
| **HTML + Tailwind + Chart.js** | Frontend com gráficos dinâmicos |
| **Git/GitHub** | Controle de versão |
| **Uvicorn** | Servidor local |

---

## 🗂️ Estrutura do Projeto
speedrun-complexidade/
├── app/
│   └── main.py              # API completa (FastAPI + SQLite)
├── index.html               # Tela do jogo
├── results.html             # Ranking
├── script.js                # Lógica do quiz + gráficos
├── style.css                # (opcional)
├── questions.json           # Perguntas com Big O de tempo e espaço
├── database_schema.json     # Modelo relacional
├── speedrun.db              # Banco (gerado automaticamente)
├── relatorio_pedagogico.md  # ← Relatório completo
├── fase_final_demo.mp4      # Vídeo de demonstração
├── requirements.txt
├── README.md                # ← este arquivo
└── venv/

---

## ⚙️ Como Executar (Passo a Passo)

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/speedrun-complexidade.git
cd speedrun-complexidade

