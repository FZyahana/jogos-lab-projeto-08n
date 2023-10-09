import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina o tamanho da tela
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))

# Defina o título da janela
pygame.display.set_caption("Projeto 08N JogosLab")

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Limpar a tela
    tela.fill((0, 0, 0))  # Preencher a tela com a cor preta

    # Desenhar objetos, personagens, etc. aqui

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
