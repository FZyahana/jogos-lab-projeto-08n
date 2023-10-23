import pygame
import sys

# Inicialize o Pygame
pygame.init()


# Defina o tamanho da tela
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))

# Importar a imagem do corredor
sprite_main = pygame.image.load("sprite_main_test.png")
scale_sprite = (160/sprite_main.get_height())
sprite_main = pygame.transform.scale(sprite_main,(scale_sprite*sprite_main.get_width(),scale_sprite*sprite_main.get_height()))
print(sprite_main.get_height())

# Importar o fundo fase 1
# Considerando que todas as imagens de um parallel vão ter mesmo tamanho, vou deixar o código eficiente
background1_1 = pygame.image.load("assets/parallax-forest-back-trees.png")
scale_background = (240/background1_1.get_height())
background1_1 = pygame.transform.scale(background1_1,(scale_background*background1_1.get_width(),scale_background*background1_1.get_height()))

#2
background1_2 = pygame.image.load("assets/parallax-forest-lights.png")
# scale_background = (240/background1_1.get_height())
background1_2 = pygame.transform.scale(background1_2,(scale_background*background1_1.get_width(),scale_background*background1_1.get_height()))

#3
background1_3 = pygame.image.load("assets/parallax-forest-middle-trees.png")
# scale_background = (240/background1_1.get_height())
background1_3 = pygame.transform.scale(background1_3,(scale_background*background1_1.get_width(),scale_background*background1_1.get_height()))

#4
background1_4 = pygame.image.load("assets/parallax-forest-front-trees.png")
# scale_background = (240/background1_1.get_height())
background1_4 = pygame.transform.scale(background1_4,(scale_background*background1_1.get_width(),scale_background*background1_1.get_height()))


# Definir variáveis para o jogo
pos = 0
background1_x = [0,408,816,1224,1632]
background2_x = [0,408,816,1224,1632]
background3_x = [0,408,816,1224,1632]
background4_x = [0,408,816,1224,1632]

# def backgroundPosReset():
#     background1_x = [0,408,816,1224,1632]
#     background2_x = [0,408,816,1224,1632]
#     background3_x = [0,408,816,1224,1632]
#     background4_x = [0,408,816,1224,1632]

# Função pra blitar os cenários
def blitParallelBackground_indiv(arraypos,img,speed):
    for i in range(5):
        tela.blit(img,(arraypos[i],0))
        arraypos[i]-=speed
        if arraypos[i] <= -408:
            arraypos[i] = max(arraypos)+408-5

def blitParallelBackground_full(matrixpos,arrayimg,arrayspeed):

    blitParallelBackground_indiv(matrixpos[0],arrayimg[0],arrayspeed[0])
    blitParallelBackground_indiv(matrixpos[1],arrayimg[1],arrayspeed[1])
    blitParallelBackground_indiv(matrixpos[2],arrayimg[2],arrayspeed[2])
    blitParallelBackground_indiv(matrixpos[3],arrayimg[3],arrayspeed[3])

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

    velocidade1 = 1
    velocidade2 = 2
    velocidade3 = 3
    velocidade4 = 4

    #definindo posições, img e velocidades por fase
    matrixpos = [background1_x,background2_x,background3_x,background4_x]
    arrayimg = [background1_1,background1_2,background1_3,background1_4]
    arrayspeed = [velocidade1,velocidade2,velocidade3,velocidade4]
    blitParallelBackground_full(matrixpos,arrayimg,arrayspeed)

    # Desenhar personagem principal
    tela.blit(sprite_main,(0,240+pos*160))

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
