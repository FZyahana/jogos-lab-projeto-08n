import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina o tamanho da tela
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))

#Importar a imagem do corredor
sprite_main = pygame.image.load("sprite_main_test.png")
scale_sprite = (160/sprite_main.get_height())
sprite_main = pygame.transform.scale(sprite_main,(scale_sprite*sprite_main.get_width(),scale_sprite*sprite_main.get_height()))
print(sprite_main.get_height())

# Definir variáveis para o jogo
pos = 0

# Defina o título da janela
pygame.display.set_caption("Projeto 08N JogosLab")

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                if pos != 0:
                    pos -= 1
            elif evento.key == pygame.K_DOWN:
                if pos != 2:
                    pos += 1
    


    # Limpar a tela
    tela.fill((0, 0, 0))  # Preencher a tela com a cor preta

    # Desenhar objetos, personagens, etc. aqui
    pygame.draw.rect(tela, (255,0,0), (0,0, 1280, 240))

    # Desenhar personagem principal
    tela.blit(sprite_main,(0,240+pos*160))


    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
