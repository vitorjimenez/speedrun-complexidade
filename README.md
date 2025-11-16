# 🚀 Speed Run Complexidade Quiz

**Quiz gamificado para ensinar Notação Big O com gráficos dinâmicos, revisão visual e ranking.**

---

## 🎯 Objetivo Pedagógico

Ensinar **complexidade de algoritmos (Big O)** de forma **interativa, rápida e visual**.  
O jogador responde 5 perguntas em até 15 segundos cada, ganha pontos por acerto + bônus por tempo, e **vê gráficos do crescimento do algoritmo** na tela de revisão.

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
```markdown
# 🚀 Speed Run Complexidade Quiz

**Quiz gamificado para ensinar Notação Big O com gráficos dinâmicos, revisão visual e ranking.**

---

## 🎯 Objetivo Pedagógico

Ensinar **complexidade de algoritmos (Big O)** de forma **interativa, rápida e visual**.  
O jogador responde 5 perguntas em até 15 segundos cada, ganha pontos por acerto + bônus por tempo, e **vê gráficos do crescimento do algoritmo** na tela de revisão.

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

```
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
├── relatorio_pedagogico.md  # Relatório pedagógico
├── fase_final_demo.mp4      # Vídeo de demonstração (2-5 min)
├── requirements.txt
├── README.md                # ← este arquivo
└── venv/
```

## ⚙️ Como Executar (Passo a Passo)

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/speedrun-complexidade.git
cd speedrun-complexidade
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
```
- **Windows (Git Bash):**
  ```bash
  source venv/Scripts/activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Rode a API
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Abra o jogo no navegador
```
http://localhost:8000/index.html
```

### 6. Acesse o Swagger (teste da API)
```
http://localhost:8000/docs
```

---

## 🔐 Rotas da API (com Token)

> **Token fixo:** `super-secret-complexidade-token`

| Rota | Método | Função | Exemplo |
|------|--------|-------|--------|
| `/health` | GET | Verifica API | `curl -H "X-API-Token: ..." http://localhost:8000/health` |
| `/launch` | POST | Inicia partida | Gera `session_id` |
| `/score` | POST | Envia respostas | Calcula pontos + bônus |
| `/results` | GET | Ranking | Lista jogadores |
| `/questions` | GET | Perguntas (sem resposta) | Usado no frontend |
| `/questions_full` | GET | Perguntas completas | Para revisão |

---

## 🌍 Variáveis de Ambiente

| Variável | Valor Padrão | Uso |
|---------|--------------|-----|
| `API_TOKEN` | `super-secret-complexidade-token` | Autenticação em todas as rotas |

> **Dica:** Para mudar o token:
> ```python
> # app/main.py
> API_TOKEN = os.environ.get("API_TOKEN", "novo-token-aqui")
> ```

---

## 🎥 Vídeo de Demonstração (Storytelling)

**Link:** [https://youtu.be/XXXXXXX](https://youtu.be/XXXXXXX) *(substitua pelo seu link)*

**Duração:** 3 minutos  
**Apresentador:** Apenas voz (sem aparecer)  
**Conteúdo:**
1. **Por que criamos?** → Ensinar Big O de forma divertida.
2. **Como funciona?** → Quiz + gráficos + ranking.
3. **Demo ao vivo** → Jogar, revisar com gráficos, ver ranking.
4. **O que aprendemos?** → FastAPI, SQLite, Chart.js, pedagogia ativa.
5. **Teorias abordadas** → Big O de tempo e espaço, loops, recursão.

---

## 📝 Relatório Pedagógico

### 1. Objetivo do Projeto
Ensinar **notação Big O** de forma **gamificada, visual e ativa**, transformando um conceito teórico em uma experiência prática e competitiva.

### 2. Problema Resolvido
> **"Como fazer alunos internalizarem Big O sem decorar fórmulas?"**

**Solução:**  
Um **quiz cronometrado** com **código real**, **gráficos dinâmicos** e **revisão visual**.

### 3. Mecânicas Pedagógicas

| Mecanismo | Efeito no Aprendizado |
|---------|------------------------|
| **15 segundos por pergunta** | Treina **análise rápida** |
| **20 pontos por acerto** | Reforça **precisão** |
| **Bônus por tempo** | Ensina **eficiência** |
| **Gráficos Big O (tempo/espaço)** | **Visualiza o crescimento** |
| **Revisão com código + gráficos** | **Aprendizado ativo** |
| **Ranking persistido** | **Competição saudável** |

### 4. Teorias Abordadas

| Conceito | Implementação |
|--------|---------------|
| `O(1)` | Função constante |
| `O(n)` | Loop simples |
| `O(n²)` | Loops aninhados |
| `O(log n)` | Busca binária |
| `O(n log n)` | Merge Sort |
| **Complexidade de espaço** | `O(1)` vs `O(n)` |

### 5. Resultados Esperados
- Aluno **lê código** → **identifica padrão** → **escolhe Big O**
- **Vê o gráfico** → **entende o impacto real**
- **Repete para subir no ranking** → **internaliza o conceito**

### 6. Conclusão
> **"O Speed Run não ensina Big O. Ele faz o aluno VIVER Big O."**

Projeto **executável, documentado e escalável**.  
Pronto para ser usado em sala de aula ou como material de apoio.

**Grupo: Nicolas, Vinicius, Vitor**  
**Disciplina: Complexidade de Algoritmos**

---

## 🐞 Solução de Problemas

| Problema | Solução |
|--------|--------|
| `uvicorn not found` | `pip install uvicorn` |
| Porta 8000 ocupada | Use `--port 8001` |
| Erro de CORS | Frontend já tem `getAuthHeaders()` |
| Banco não criado | Rode a API uma vez → `speedrun.db` é gerado |

---

## 👥 Equipe

| Nome | GitHub | Função |
|------|--------|--------|
| Nicolas Silva | [@nicolas](https://github.com/nicolassantana42) | Full Stack + Gráficos |
| Vinicius Cerqueira | [@vinicius](https://github.com/ViniCerqueira) | Backend + Banco |
| Vitor Jimenez | [@vitor](https://github.com/vitorjimenez) | Frontend + UX |

---

## 📄 Licença

**MIT** – Use, estude, melhore!

---

**Projeto 100% executável, documentado e pedagógico.**
```
```
