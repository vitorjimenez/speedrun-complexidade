# Speed Run de Complexidade

Aplicação educacional gamificada para aprender complexidade de algoritmos.

## Como Rodar

1. Instale dependências: `pip install -r requirements.txt`
2. Build Docker: `docker build -t algo-quiz .`
3. Rode o container: `docker run -p 8000:8000 -v $(pwd)/app:/app algo-quiz`
   - O `-v` persiste questions.json e scores.json.
4. Acesse a API: http://localhost:8000/docs (Swagger para documentação).
5. Jogue via CLI: `python interface/quiz_cli.py`

## Como Jogar
- Rode a API via Docker.
- Execute o CLI: responda questões, veja explicações e ranking.

## Contribuir
- Adicione questões em questions.json.
- Melhore a gamificação (ex: mais níveis).

Diferenciais: Tempo de resposta afeta score, feedback educativo, interface Python simples.