// Configurações Globais
const API_BASE_URL = "http://localhost:8000";
const MAX_TIME_PER_QUESTION = 15; // Segundos
// Token Fixo para Autenticação (deve ser o mesmo do main.py)
const API_TOKEN = "super-secret-complexidade-token"; 

// ===============================================
// FUNÇÃO PARA INCLUIR O HEADER DE AUTENTICAÇÃO
// ===============================================
function getAuthHeaders() {
    return {
        'Content-Type': 'application/json',
        'X-API-Token': API_TOKEN
    };
}

// Elementos do DOM
const startScreen = document.getElementById('start-screen');
const quizScreen = document.getElementById('quiz-screen');
const scoreScreen = document.getElementById('score-screen');
const reviewScreen = document.getElementById('review-screen');
const playerNameInput = document.getElementById('player-name');
const startQuizBtn = document.getElementById('start-quiz-btn');
const errorMessage = document.getElementById('error-message');
const questionCounter = document.getElementById('question-counter');
const timerDisplay = document.getElementById('timer');
const codeSnippet = document.getElementById('code-snippet');
const optionsContainer = document.getElementById('options-container');
const finalScoreDisplay = document.getElementById('final-score');
const reviewAnswersBtn = document.getElementById('review-answers-btn');
const reviewResultsContainer = document.getElementById('review-results-container');

// Variáveis de Estado do Jogo
let allQuestions = [];
let fullQuestionDetails = {};
let currentQuestionIndex = 0;
let answersLog = [];
let totalGameTime = 0;
let countdown;
let questionStartTime; 

// Funções de Utilidade (simplificadas)
function showScreen(screen) {
    startScreen.classList.add('hidden');
    quizScreen.classList.add('hidden');
    scoreScreen.classList.add('hidden');
    reviewScreen.classList.add('hidden');
    screen.classList.remove('hidden');
}

function updateTimerDisplay(time) {
    timerDisplay.textContent = time.toFixed(2) + 's';
}

function startTimer() {
    questionStartTime = performance.now();
    let timeLeft = MAX_TIME_PER_QUESTION;
    
    updateTimerDisplay(timeLeft);
    
    // Referência ao container do gráfico para o efeito dinâmico
    const quizChartContainer = document.getElementById('quizTimeChart').parentElement;

    countdown = setInterval(() => {
        const elapsedTime = (performance.now() - questionStartTime) / 1000;
        timeLeft = Math.max(0, MAX_TIME_PER_QUESTION - elapsedTime);
        
        // Lógica do EFEITO DINÂMICO no gráfico
        if (quizChartContainer) {
            // Limpa classes de animação e cores
            quizChartContainer.classList.remove('border-teal-500', 'border-yellow-500', 'border-red-500', 'animate-pulse');
            quizChartContainer.classList.add('border-2');

            if (timeLeft <= 5) {
                // Tempo Crítico: Pulsa rápido e glow forte (VERMELHO)
                quizChartContainer.classList.add('border-red-500', 'animate-pulse');
                quizChartContainer.style.boxShadow = '0 0 10px rgba(239, 68, 68, 0.8)'; 
            } else if (timeLeft <= 10) {
                // Aviso: Pulsa devagar e glow médio (AMARELO)
                quizChartContainer.classList.add('border-yellow-500');
                quizChartContainer.style.boxShadow = '0 0 5px rgba(251, 191, 36, 0.6)'; 
            } else {
                // Início: Brilho estável (TEAL)
                quizChartContainer.classList.add('border-teal-500');
                quizChartContainer.style.boxShadow = '0 0 3px rgba(20, 184, 166, 0.5)';
            }
        }


        if (timeLeft <= 0) {
            clearInterval(countdown);
            handleAnswerSubmission(null); // Submissão automática em caso de tempo esgotado
            if (quizChartContainer) {
                quizChartContainer.style.boxShadow = 'none';
                quizChartContainer.classList.remove('border-red-500', 'animate-pulse', 'border-2');
            }
        } else {
            updateTimerDisplay(timeLeft);
        }
    }, 50); // Atualiza o cronômetro a cada 50ms
}

function stopTimer() {
    clearInterval(countdown);
    const endTime = performance.now();
    const elapsedTime = (endTime - questionStartTime) / 1000;
    
    // Referência ao container do gráfico para PARAR o efeito dinâmico
    const quizChartContainer = document.getElementById('quizTimeChart').parentElement;
    if (quizChartContainer) {
        quizChartContainer.style.boxShadow = 'none';
        quizChartContainer.classList.remove('border-teal-500', 'border-yellow-500', 'border-red-500', 'animate-pulse', 'border-2');
    }

    // Calcula o tempo gasto, limitado ao máximo
    const timeSpent = Math.min(elapsedTime, MAX_TIME_PER_QUESTION);
    totalGameTime += timeSpent;
    
    // Reseta a cor do timer
    timerDisplay.classList.remove('text-yellow-500');
    timerDisplay.classList.add('text-red-400');
    
    return timeSpent;
}

// Lógica Principal do Quiz
async function fetchQuestions() {
    try {
        // Busca TODAS as perguntas para fins de dica/revisão
        const fullResponse = await fetch(`${API_BASE_URL}/questions_full`, {
            headers: getAuthHeaders()
        }); 
        
        if (fullResponse.status === 401) {
             throw new Error('Erro de Autenticação: Token API inválido.');
        }
        if (!fullResponse.ok) {
            throw new Error('API indisponível ou erro ao buscar perguntas completas.');
        }
        
        const fullData = await fullResponse.json();
        
        // Cria um mapa de IDs para facilitar a busca de detalhes
        fullQuestionDetails = fullData.questions.reduce((map, q) => {
            map[q.id_pergunta] = q;
            return map;
        }, {});

        // Embaralha e limita as perguntas a 5 para o quiz
        allQuestions = fullData.questions
            .sort(() => Math.random() - 0.5)
            .slice(0, 5)
            .map(q => ({
                id_pergunta: q.id_pergunta,
                code: q.code,
                options: q.options
            }));
        
        if (allQuestions.length === 0) {
            throw new Error('Nenhuma pergunta disponível no banco de dados.');
        }
    } catch (error) {
        console.error("Erro ao buscar perguntas:", error);
        errorMessage.textContent = error.message;
        errorMessage.classList.remove('hidden');
        allQuestions = [];
    }
}

// FUNÇÃO ATUALIZADA: Desenha o código e os GRÁFICOS DE DICA na tela do quiz
function renderQuestion() {
    if (currentQuestionIndex >= allQuestions.length) {
        submitScore();
        return;
    }

    const question = allQuestions[currentQuestionIndex];
    const fullDetail = fullQuestionDetails[question.id_pergunta]; // Detalhe completo para as dicas
    
    // Atualiza contador
    questionCounter.textContent = `Pergunta ${currentQuestionIndex + 1} de ${allQuestions.length}`;
    
    // Atualiza o código e re-highlight
    codeSnippet.textContent = question.code;
    hljs.highlightElement(codeSnippet);

    // 🚨 DESENHA O GRÁFICO DE DICA NA TELA DO QUIZ 🚨
    drawComplexityGraph('quizTimeChart', fullDetail.correct_answer, `Crescimento: ${fullDetail.correct_answer}`);
    
    // Atualiza opções
    optionsContainer.innerHTML = '';
    const shuffledOptions = question.options.sort(() => Math.random() - 0.5);

    shuffledOptions.forEach(option => {
        const button = document.createElement('button');
        button.className = 'w-full text-left p-4 bg-gray-700 hover:bg-teal-600 rounded-lg font-medium transition duration-200 shadow-md transform hover:scale-[1.02]';
        button.textContent = option;
        button.setAttribute('data-answer', option);
        button.onclick = () => handleAnswerSubmission(option);
        optionsContainer.appendChild(button);
    });
    
    startTimer();
    showScreen(quizScreen);
}

function handleAnswerSubmission(selectedAnswer) {
    const question = allQuestions[currentQuestionIndex];
    const correctAnswer = fullQuestionDetails[question.id_pergunta].correct_answer;
    
    // Pausa o cronômetro e acumula o tempo
    stopTimer();
    
    // Determina a resposta dada (TIME_OUT se nulo) e a correção
    const answerGiven = selectedAnswer || 'TIME_OUT';
    const isCorrect = (answerGiven !== 'TIME_OUT' && answerGiven === correctAnswer);
    
    // Registra a resposta COMPLETA para a log de revisão
    answersLog.push({
        id_pergunta: question.id_pergunta,
        resposta_dada: answerGiven,
        is_correct: isCorrect
    });
    
    // Avança para a próxima pergunta
    currentQuestionIndex++;
    renderQuestion();
}

async function submitScore() {
    showScreen(scoreScreen);
    
    const playerName = playerNameInput.value.trim() || 'Anônimo';
    
    const answersToSubmit = answersLog
        .filter(a => a.resposta_dada !== 'TIME_OUT')
        .map(a => ({ id_pergunta: a.id_pergunta, resposta_dada: a.resposta_dada }));
    
    const finalScoreSubmission = {
        player_name: playerName,
        answers: answersToSubmit,
        tempo_total: totalGameTime
    };

    try {
        // Usa o token de autenticação
        const response = await fetch(`${API_BASE_URL}/score`, {
            method: 'POST',
            headers: getAuthHeaders(),
            body: JSON.stringify(finalScoreSubmission)
        });

        if (response.status === 401) {
             throw new Error('Erro de Autenticação: Token API inválido ao submeter pontuação.');
        }

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'Erro desconhecido ao registrar pontuação.');
        }

        finalScoreDisplay.textContent = data.total_score;
        
    } catch (error) {
        console.error("Erro na submissão da pontuação:", error);
        finalScoreDisplay.textContent = 'ERRO!';
        alert(`Não foi possível registrar a pontuação. ${error.message}`);
    }
}

// ===============================================
// FUNÇÕES PARA DESENHAR GRÁFICOS (BASE CHART.JS)
// ===============================================

// Mapeamento de funções Big O para geração de dados
const complexityFunctions = {
    'O(1)': (n) => 10, // Constante
    'O(log n)': (n) => 10 * Math.log2(n || 1), // Logarítmico
    'O(n)': (n) => 10 * n, // Linear
    'O(n log n)': (n) => 10 * n * Math.log2(n || 1), // Linearitmico
    'O(n^2)': (n) => 10 * n * n, // Quadrático
    'O(2^n)': (n) => 10 * Math.pow(2, n), // Exponencial (Limitado a N<10)
};

function generateChartData(complexityStr, maxN = 10) {
    const data = [];
    const func = complexityFunctions[complexityStr];
    if (!func) return data;

    for (let n = 1; n <= maxN; n++) {
        data.push(func(n) / 10); // Normalizado para N
    }
    return data;
}

function drawComplexityGraph(canvasId, complexityStr, title) {
    // Se já houver um gráfico no canvas, destruí-lo primeiro (essencial para redesenho)
    const existingChart = Chart.getChart(canvasId);
    if (existingChart) {
        existingChart.destroy();
    }
    
    const dataPoints = generateChartData(complexityStr);
    const labels = Array.from({ length: dataPoints.length }, (_, i) => `N=${i + 1}`);

    const ctx = document.getElementById(canvasId).getContext('2d');
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: complexityStr,
                data: dataPoints,
                borderColor: '#10b981', // Verde Teal
                backgroundColor: 'rgba(16, 185, 129, 0.1)',
                borderWidth: 2,
                tension: 0.1,
                pointRadius: 3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true,
                    labels: {
                        color: '#9ca3af' // cinza claro
                    }
                },
                title: {
                    display: true,
                    text: title,
                    color: '#e5e7eb' // branco
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Tamanho da Entrada (N)',
                        color: '#9ca3af'
                    },
                    grid: { color: '#374151' }, // cinza escuro
                    ticks: { color: '#e5e7eb' }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Custo Relativo',
                        color: '#9ca3af'
                    },
                    grid: { color: '#374151' },
                    ticks: { color: '#e5e7eb' }
                }
            }
        }
    });
}
// ===============================================

// LÓGICA DA TELA DE REVISÃO (SIMPLIFICADA, SEM GRÁFICOS)
function renderReviewScreen() {
    showScreen(reviewScreen);
    reviewResultsContainer.innerHTML = '';
    
    answersLog.forEach((logEntry, index) => {
        const questionDetail = fullQuestionDetails[logEntry.id_pergunta];
        
        if (!questionDetail) return;

        const statusText = logEntry.is_correct ? 'CORRETA' : 'ERRADA';
        const answerGivenText = logEntry.resposta_dada === 'TIME_OUT' ? 'Tempo Esgotado' : logEntry.resposta_dada;
        
        const timeComplexity = questionDetail.correct_answer;

        const reviewBlock = document.createElement('div');
        reviewBlock.className = `p-6 rounded-xl shadow-lg bg-opacity-20 border-l-4 ${logEntry.is_correct ? 'border-green-400 bg-green-900/50' : 'border-red-400 bg-red-900/50'}`;
        reviewBlock.innerHTML = `
            <h3 class="text-xl font-bold mb-3 text-white">Pergunta ${index + 1}: <span class="${logEntry.is_correct ? 'text-green-400' : 'text-red-400'}">${statusText}</span></h3>
            
            <p class="text-lg font-semibold text-gray-300">Sua Resposta: <span class="${logEntry.is_correct ? 'text-green-400' : 'text-red-400'} font-bold">${answerGivenText}</span></p>

            <div class="bg-gray-900 p-3 rounded-lg my-4">
                <pre><code class="language-python">${questionDetail.code}</code></pre>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                <div>
                    <p class="text-lg font-semibold text-teal-400">Complexidade de Tempo (Correta):</p>
                    <p class="text-2xl font-bold text-white">${timeComplexity}</p>
                </div>
            </div>
        `;
        reviewResultsContainer.appendChild(reviewBlock);
        
        // Aplica o highlight.js no novo código
        reviewBlock.querySelectorAll('code').forEach((el) => {
            hljs.highlightElement(el);
        });
    });
}

// Inicialização da Partida
startQuizBtn.addEventListener('click', async () => {
    const playerName = playerNameInput.value.trim();
    if (!playerName) {
        errorMessage.textContent = 'Por favor, digite seu nome para iniciar.';
        errorMessage.classList.remove('hidden');
        return;
    }
    
    errorMessage.classList.add('hidden');
    
    // 1. Iniciar a partida na API (incluindo token)
    try {
        const launchResponse = await fetch(`${API_BASE_URL}/launch`, { 
            method: 'POST',
            headers: getAuthHeaders()
        });
        
        if (launchResponse.status === 401) {
             throw new Error('Erro de Autenticação: Token API inválido.');
        }
        if (!launchResponse.ok) {
             throw new Error('Falha ao iniciar a partida (Endpoint /launch).');
        }
    } catch (error) {
        errorMessage.textContent = 'Erro de conexão com a API. Certifique-se de que o servidor está rodando em http://localhost:8000 e que o token está correto.';
        errorMessage.classList.remove('hidden');
        return;
    }

    // 2. Resetar o estado do jogo e buscar as perguntas
    currentQuestionIndex = 0;
    answersLog = [];
    totalGameTime = 0;
    await fetchQuestions();

    if (allQuestions.length > 0) {
        renderQuestion();
    } else {
        errorMessage.textContent = 'Não foi possível carregar as perguntas. Verifique o console para mais detalhes.';
        errorMessage.classList.remove('hidden');
    }
});

// Listener do novo botão
reviewAnswersBtn.addEventListener('click', renderReviewScreen);

// Garante que a tela inicial é mostrada ao carregar
showScreen(startScreen);

// Aplica o highlight.js na inicialização (se houver código estático)
hljs.highlightAll();