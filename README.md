# 🎰 Cassino Estatístico: O Tabuleiro de Galton

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.x-yellow?style=for-the-badge&logo=pygame)
![Status](https://img.shields.io/badge/Status-Finalizado-green?style=for-the-badge)

> Um jogo digital que une entretenimento e ciência para demonstrar o comportamento de eventos aleatórios e a distribuição de probabilidade em tempo real.

---

## 📋 Sobre o Projeto

Este trabalho foi desenvolvido para a disciplina de **Estatística** com o objetivo de simular um **Tabuleiro de Galton** (mecânica estilo "Plinko").

O software ilustra visualmente a **Lei dos Grandes Números** e o **Teorema do Limite Central**. O jogador aposta dinheiro fictício soltando bolas em uma pirâmide de pinos. Enquanto joga, um gráfico é gerado simultaneamente, demonstrando como o caos individual converge para uma ordem matemática (a Curva de Gauss/Normal).

### Destaques:
* **Gamificação:** Sistema de saldo, apostas variáveis e risco/retorno (Cassino Fake).
* **Simulação Real:** Física de colisão simples determinística (50/50).
* **Análise Visual:** Histograma empírico vs. Curva Teórica em tempo real.

---

## 🛠️ Instalação e Execução

Siga os passos abaixo para rodar o jogo no seu computador.

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)
cd NOME-DO-REPO
```
2. Criar e Ativar Ambiente Virtual (Opcional, mas recomendado)

Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```
5. Instalar Dependências
```bash
pip install -r requirements.txt
```

7. Rodar o Jogo
```bash
python src/main.py
```

🎮 Comandos do Jogo
```bash
ESPAÇO,Soltar Bola (Realizar aposta)
↑ ou W,"Aumentar Aposta (+ R$ 5,00)"
↓ ou S,"Diminuir Aposta (- R$ 5,00)"
R,Refinanciar (Apenas quando o saldo acabar)
```
