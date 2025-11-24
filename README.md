# Plinko-estatistico
Este projeto implementa um jogo digital inspirado em um "Cassino Fake" com foco no estudo do comportamento de variáveis aleatórias do tipo binomial.
O usuário lança bolinhas que descem por uma pirâmide de pinos, escolhendo aleatoriamente (50/50) ir para a esquerda ou direita em cada linha, simulando um processo binomial clássico.

Enquanto o jogo acontece, um histograma empírico é atualizado em tempo real e comparado com a curva teórica binomial, permitindo visualizar a convergência entre teoria e prática.

Este projeto atende ao requisito de apresentar simultaneamente:

✔ Simulação aleatória em tempo real
✔ Distribuição de probabilidade empírica vs. teórica
✔ Jogabilidade + visualização estatística

Funcionalidades do Jogo:

Lado Esquerdo – O Jogo

Pirâmide de pinos simulada via grade.

Bolinhas caindo linha por linha, escolhendo aleatoriamente esquerda/direita.

Cestas na base com multiplicadores de aposta:

Centrais → baixo retorno (altamente prováveis)

Extremidades → alto retorno (raras)

HUD exibindo:

Saldo atual

Lucro/Prejuízo da última jogada

Valor da aposta fixa

Teclas:

ESPAÇO → Lançar uma bola

R → Resetar o jogo

Lado Direito – Estatística em Tempo Real

Histograma atualizado conforme as bolinhas caem.

Curva teórica fixa da distribuição binomial desenhada no fundo.

Comparação direta:

Resultados empíricos (simulação)

Probabilidades teóricas (modelo binomial)

Modelo Matemático

Cada bola percorre uma série de decisões binárias independentes.
Isso equivale a um ensaio binomial com:

n = número de linhas da pirâmide

p = 0.5 em cada decisão

Isso cria a clássica curva em formato de sino (aproximação da normal para n grande).

As cestas representam os valores 
𝑘
k possíveis do número de passos à direita.

equisitos

Python 3.10+

pygame

Bibliotecas padrão:

random

math

sys

etc.

Instalação do pygame: pip install pygame

Como Executar

Clone o repositório: git clone https://github.com/SEU_USUARIO/seu-repo.git
cd seu-repo

Execute o jogo: python jogo.py

Arquitetura do Código:

O projeto foi implementado em um único arquivo, conforme os requisitos.

Principais seções do código:

Configurações gerais (cores, tamanhos, fonte, constantes)

Classe Ball – lógica da bolinha caindo

Sistema de pinos e cestas

HUD e textos

Histograma + Curva Teórica

Loop principal do jogo

Sistema de apostas

Todo o código é comentado em português e organizado.

Controles:
Tecla	Função
ESPAÇO	Solta uma nova bola
R	Reseta o jogo
ESC	Fecha o jogo

Distribuição Empírica vs. Teórica

Histograma → Frequências empíricas dos resultados.

Curva → 𝑃(𝑋=𝑘)=(𝑛/𝑘)0.5^𝑛

Permite observar:

Convergência estatística

Flutuações amostrais

Análise de risco e retorno (via multiplicadores)

Objetivo Acadêmico

Este jogo demonstra:

✔ Comportamento de eventos aleatórios
✔ Formação de uma distribuição binomial
✔ Diferença entre probabilidade teórica e experimental
✔ Simulação estocástica em tempo real
✔ Conceitos de risco/retorno em jogos de azar

Pontuação do trabalho é maximizada por:

Criatividade

Jogabilidade

Visualização estatística explícita

Qualidade da implementação e apresentação

📜 Licença

Este projeto pode ser utilizado para fins acadêmicos e educacionais.
