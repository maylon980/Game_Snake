#configurações inciais 
import pygame
import random

pygame.init()
pygame.display.set_caption("JOGO DO MAYLÃO")
largura, altura =  1920, 1080
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

#cores RGB
preto = (0, 0, 0)
branca = (255, 255, 255)
vermelho =(255, 0, 0)
verde = (0, 255, 0)

#parametros da cobrinha
tamanho_quadrado =30
velocidade_jogo = 30 

imagem_maca = pygame.image.load("espada.png")
imagem_maca = pygame.transform.scale(imagem_maca,(tamanho_quadrado, tamanho_quadrado))


def gerar_comida():
     comida_x = round(random.randrange(0, altura - tamanho_quadrado) /tamanho_quadrado) * tamanho_quadrado
     comida_y = round(random.randrange(0, altura - tamanho_quadrado) /tamanho_quadrado) * tamanho_quadrado
     return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    tela.blit(imagem_maca,(comida_x,comida_y))

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1 ], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
  fonte = pygame.font.SysFont("Helvetica", 35)
  texto = fonte.render(f"Pontos:{pontuacao}", True, vermelho)
  tela.blit(texto, [1,1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
      velocidade_x = 0
      velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
      velocidade_x = 0
      velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
      velocidade_x = tamanho_quadrado
      velocidade_y = 0
    elif tecla == pygame.K_LEFT:
      velocidade_x = -tamanho_quadrado
      velocidade_y = 0
    else:
         velocidade_x, velocidade_y = 0, 0  

    return velocidade_x, velocidade_y

def rodar_jogo():
  fim_jogo = False

  x = largura / 2
  y = altura / 2

  velocidade_x = 0
  velocidade_y = 0

  tamanho_cobra = 1
  pixels = []

  comida_x,comida_y = gerar_comida() 

  while not fim_jogo:
      for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
          fim_jogo = True
       elif evento.type == pygame.KEYDOWN:
           velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

      x += velocidade_x
      y += velocidade_y    

      #atualizar o tamanho da cobra
      if x < 0 or x >= largura or y <0 or y >= altura:
          fim_jogo = True
      
      #desenhar a cobra
      pixels.append([x,y])
      if len(pixels) > tamanho_cobra:
       del pixels[0]  

      # verificar se a cobrinha bateu no propio corpo
      for pixel in pixels[:-1]:
        if pixel == [x,y]:
            fim_jogo = True
      
        #desenhar os elementos do jogo
      tela.fill(preto)
      desenhar_comida(tamanho_quadrado, comida_x, comida_y)
      desenhar_cobra(tamanho_quadrado, pixels)
      desenhar_pontuacao(tamanho_cobra - 1)

      
     #verificar se a cobra comeu a comida

      if x == comida_x and y == comida_y:
          tamanho_cobra +=1 
          comida_x, comida_y = gerar_comida()

      #atualização da tela
      pygame.display.update()
      relogio.tick(velocidade_jogo)

rodar_jogo()
pygame.quit()