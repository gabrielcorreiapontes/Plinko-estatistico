import pygame
import random
import math

LARGURA_TELA = 1200
ALTURA_TELA = 750
FPS = 60

COR_FUNDO = (30, 30, 30)
COR_PINOS = (220, 220, 220)
COR_BOLA = (255, 60, 60)
COR_TEXTO = (255, 255, 255)
COR_BARRAS = (0, 200, 100)
COR_CURVA = (255, 215, 0)
COR_UI_FUNDO = (50, 50, 50)
COR_DESTAQUE = (0, 255, 255)

LINHAS = 10
RAIO_PINO = 4
RAIO_BOLA = 7
ESPACO_X = 40
ESPACO_Y = 35 
OFFSET_X = 350
OFFSET_Y = 220


MULTIPLICADORES = [10, 5, 3, 1.15, 0.5, 0.2, 0.5, 1.15, 3, 5, 10]

class Bola:
    def __init__(self):
        self.x = OFFSET_X
        self.y = OFFSET_Y
        self.alvo_x = self.x
        self.alvo_y = self.y
        self.caindo = True
        self.velocidade = 9
        
        self.caminho = []
        pos_x = 0
        for _ in range(LINHAS):
            direcao = random.choice([-1, 1])
            pos_x += 0.5 * direcao
            self.caminho.append(direcao)
        
        self.cesta_final = int(5 + pos_x)
        self.passo_atual = 0

    def atualizar(self):
        if not self.caindo: return

        dx = self.alvo_x - self.x
        dy = self.alvo_y - self.y
        dist = math.hypot(dx, dy)

        if dist < self.velocidade:
            self.x = self.alvo_x
            self.y = self.alvo_y
            if self.passo_atual < len(self.caminho):
                direcao = self.caminho[self.passo_atual]
                self.alvo_x += (ESPACO_X / 2) * direcao
                self.alvo_y += ESPACO_Y
                self.passo_atual += 1
            else:
                self.caindo = False
        else:
            angle = math.atan2(dy, dx)
            self.x += math.cos(angle) * self.velocidade
            self.y += math.sin(angle) * self.velocidade

    def desenhar(self, tela):
        pygame.draw.circle(tela, COR_BOLA, (int(self.x), int(self.y)), RAIO_BOLA)

class JogoPlinko:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Plinko Estatístico - A Casa Sempre Ganha")
        self.clock = pygame.time.Clock()
        self.fonte_pequena = pygame.font.SysFont("Arial", 14, bold=True)
        self.fonte = pygame.font.SysFont("Arial", 18, bold=True)
        self.fonte_grande = pygame.font.SysFont("Arial", 28, bold=True)
        self.fonte_gigante = pygame.font.SysFont("Arial", 40, bold=True)

        self.estado = "INTRO"
        self.nome_jogador = ""
        self.input_investimento = ""
        
        self.bolas = []
        self.cestas_contagem = [0] * (LINHAS + 1)
        self.total_bolas = 0
        
        self.saldo = 0.0
        self.aposta_atual = 10.0
        self.lucro_sessao = 0.0

    def desenhar_pinos(self):
        for linha in range(LINHAS + 1):
            qtd_pinos = linha + 1
            y = OFFSET_Y + (linha * ESPACO_Y)
            x_inicial = OFFSET_X - ((qtd_pinos - 1) * ESPACO_X / 2)

            for pino in range(qtd_pinos):
                x = x_inicial + (pino * ESPACO_X)
                pygame.draw.circle(self.tela, COR_PINOS, (int(x), int(y)), RAIO_PINO)
                
            if linha == LINHAS:
                for i in range(len(MULTIPLICADORES)):
                    x_cesta = x_inicial + (i * ESPACO_X) - (ESPACO_X/2)
                    cor_mult = (150, 150, 150)
                    if MULTIPLICADORES[i] > 1: cor_mult = (255, 200, 50)
                    texto = self.fonte_pequena.render(f"{MULTIPLICADORES[i]}x", True, cor_mult)
                    self.tela.blit(texto, (x_cesta - 10, y + 15))

    def calcular_curva_teorica(self, indice_cesta):
        n = LINHAS
        k = indice_cesta
        combinacao = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
        return combinacao * (0.5 ** n)

    def desenhar_grafico(self):
        area_x, area_y, area_w, area_h = 700, 150, 450, 400
        pygame.draw.rect(self.tela, (40, 40, 40), (area_x, area_y, area_w, area_h))
        pygame.draw.rect(self.tela, (255, 255, 255), (area_x, area_y, area_w, area_h), 2)

        titulo = self.fonte_grande.render("Distribuição Real", True, COR_TEXTO)
        self.tela.blit(titulo, (area_x + 120, area_y - 40))

        if self.total_bolas == 0: return

        largura_barra = area_w / len(self.cestas_contagem)
        max_contagem = max(self.cestas_contagem) if max(self.cestas_contagem) > 0 else 1
        escala_y = (area_h - 30) / max_contagem 

        pontos_teoricos = []
        for i, qtd in enumerate(self.cestas_contagem):
            altura = qtd * escala_y
            x = area_x + (i * largura_barra)
            y = (area_y + area_h) - altura
            
            cor = (200, 50, 50) if MULTIPLICADORES[i] < 1 else (50, 200, 50)
            pygame.draw.rect(self.tela, cor, (x + 2, y, largura_barra - 4, altura))
            
            if qtd > 0:
                texto_qtd = self.fonte_pequena.render(str(qtd), True, (255, 255, 255))
                self.tela.blit(texto_qtd, (x + (largura_barra/2) - 5, y - 15))
            
            qtd_esperada = self.calcular_curva_teorica(i) * self.total_bolas
            y_teorico = (area_y + area_h) - (qtd_esperada * escala_y)
            pontos_teoricos.append((x + largura_barra/2, y_teorico))

        if len(pontos_teoricos) > 1:
            pygame.draw.lines(self.tela, COR_CURVA, False, pontos_teoricos, 4)

        legenda = self.fonte_pequena.render("Linha Amarela = Curva Normal Teórica", True, COR_CURVA)
        self.tela.blit(legenda, (area_x + 10, area_y + area_h + 10))

    def tela_intro(self):
        self.tela.fill((20, 20, 40))
        titulo = self.fonte_gigante.render("CASSINO ESTATÍSTICO", True, COR_CURVA)
        subtitulo = self.fonte.render("Onde a Estatística tira seu dinheiro com classe", True, COR_TEXTO)
        
        t_nome = self.fonte_grande.render(f"Nome: {self.nome_jogador}_", True, COR_DESTAQUE)
        t_valor = self.fonte_grande.render(f"Investimento Inicial: R$ {self.input_investimento}", True, COR_DESTAQUE)
        aviso = self.fonte.render("Digite e aperte ENTER para confirmar.", True, (150, 150, 150))

        self.tela.blit(titulo, (LARGURA_TELA//2 - titulo.get_width()//2, 100))
        self.tela.blit(subtitulo, (LARGURA_TELA//2 - subtitulo.get_width()//2, 160))
        self.tela.blit(t_nome, (300, 300))
        self.tela.blit(t_valor, (300, 400))
        self.tela.blit(aviso, (LARGURA_TELA//2 - aviso.get_width()//2, 600))

    def tela_falencia(self):
        s = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        s.set_alpha(200)
        s.fill((0, 0, 0))
        self.tela.blit(s, (0,0))
        
        msg1 = self.fonte_gigante.render("VOCÊ FALIU!", True, (255, 0, 0))
        msg2 = self.fonte_grande.render("O algoritmo diz que sua sorte está prestes a mudar.", True, COR_TEXTO)
        msg3 = self.fonte_grande.render("Pressione [R] para pegar R$ 100 com o agiota", True, COR_CURVA)
        
        self.tela.blit(msg1, (LARGURA_TELA//2 - msg1.get_width()//2, 250))
        self.tela.blit(msg2, (LARGURA_TELA//2 - msg2.get_width()//2, 320))
        self.tela.blit(msg3, (LARGURA_TELA//2 - msg3.get_width()//2, 380))

    def desenhar_hud(self):
        pygame.draw.rect(self.tela, (40, 40, 40), (10, 10, 400, 160), border_radius=10)
        pygame.draw.rect(self.tela, (100, 100, 100), (10, 10, 400, 160), 2, border_radius=10)

        texto_nome = self.fonte_grande.render(f"Jogador: {self.nome_jogador}", True, COR_TEXTO)
        texto_saldo = self.fonte_grande.render(f"Saldo: R$ {self.saldo:.2f}", True, COR_CURVA)
        
        cor_aposta = COR_DESTAQUE
        if self.saldo < self.aposta_atual: cor_aposta = (255, 50, 50)
        texto_aposta = self.fonte_grande.render(f"Aposta: R$ {self.aposta_atual:.2f} (Use ↑ ↓)", True, cor_aposta)

        cor_lucro = (50, 255, 50) if self.lucro_sessao >= 0 else (255, 80, 80)
        texto_lucro = self.fonte.render(f"Lucro/Prejú: R$ {self.lucro_sessao:.2f}", True, cor_lucro)
        
        self.tela.blit(texto_nome, (30, 20))
        self.tela.blit(texto_saldo, (30, 60))
        self.tela.blit(texto_aposta, (30, 100))
        self.tela.blit(texto_lucro, (30, 140))
        
        instrucoes = self.fonte.render("[ESPAÇO] Soltar Bola", True, (200, 200, 200))
        self.tela.blit(instrucoes, (30, ALTURA_TELA - 40))

    def rodar(self):
        rodando = True
        input_fase = 0 

        while rodando:
            self.clock.tick(FPS)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                
                if self.estado == "INTRO":
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            if input_fase == 0 and len(self.nome_jogador) > 0:
                                input_fase = 1
                            elif input_fase == 1 and len(self.input_investimento) > 0:
                                try:
                                    self.saldo = float(self.input_investimento)
                                    self.estado = "JOGANDO"
                                except:
                                    self.input_investimento = ""
                        elif evento.key == pygame.K_BACKSPACE:
                            if input_fase == 0: self.nome_jogador = self.nome_jogador[:-1]
                            else: self.input_investimento = self.input_investimento[:-1]
                        else:
                            if input_fase == 0: self.nome_jogador += evento.unicode
                            else: 
                                if evento.unicode.isnumeric(): self.input_investimento += evento.unicode
                
                elif self.estado == "JOGANDO":
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_SPACE:
                            if self.saldo >= self.aposta_atual:
                                self.saldo -= self.aposta_atual
                                self.lucro_sessao -= self.aposta_atual
                                self.bolas.append(Bola())
                        
                        if evento.key in [pygame.K_UP, pygame.K_w]:
                            self.aposta_atual += 5
                        if evento.key in [pygame.K_DOWN, pygame.K_s]:
                            if self.aposta_atual > 5: self.aposta_atual -= 5

                elif self.estado == "FALIDO":
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            self.saldo += 100
                            self.estado = "JOGANDO"

            if self.estado == "INTRO":
                self.tela_intro()
            
            elif self.estado == "JOGANDO":
                self.tela.fill(COR_FUNDO)
                
                if self.saldo < 5 and len(self.bolas) == 0:
                    self.estado = "FALIDO"

                for i in range(len(self.bolas) - 1, -1, -1):
                    bola = self.bolas[i]
                    bola.atualizar()
                    bola.desenhar(self.tela)
                    if not bola.caindo:
                        idx = bola.cesta_final
                        self.cestas_contagem[idx] += 1
                        self.total_bolas += 1
                        ganho = self.aposta_atual * MULTIPLICADORES[idx]
                        self.saldo += ganho
                        self.lucro_sessao += ganho
                        self.bolas.pop(i)

                self.desenhar_pinos()
                self.desenhar_grafico()
                self.desenhar_hud()

            elif self.estado == "FALIDO":
                self.tela.fill(COR_FUNDO)
                self.desenhar_pinos()
                self.desenhar_grafico()
                self.desenhar_hud()
                self.tela_falencia()

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    jogo = JogoPlinko()
    jogo.rodar()