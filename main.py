import pygame
import sys

# Inicialize o Pygame
pygame.init()


# Defina o tamanho da tela
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

# Definir classe da sprite do main
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, image_files, x, y, frame_duration):
        super().__init__()

        self.images = []
        for file in image_files:
            png = pygame.image.load(file)
            escala = (160/png.get_height())
            png = pygame.transform.scale(png,(escala*png.get_width(),escala*png.get_height()))
            self.images.append(png)

        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.frame_duration = frame_duration
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]


# Importar a imagem do corredor
sprite_image_files = ["Run (1).png","Run (2).png", "Run (3).png", "Run (4).png", "Run (5).png", "Run (6).png", "Run (7).png", "Run (8).png"]
for i in range(len(sprite_image_files)):
    sprite_image_files[i] = "assets\\sprite\\" + sprite_image_files[i]
sprite_main = AnimatedSprite(sprite_image_files,0,0,40)

# Importar o fundo fase 1
# Considerando que todas as imagens de um parallel vão ter mesmo tamanho, vou deixar o código eficiente
background1_1 = pygame.image.load("assets/parallax-forest-back-trees.png")
scale_background = (240/background1_1.get_height())
background1_1 = pygame.transform.scale(background1_1,(scale_background*background1_1.get_width(),scale_background*background1_1.get_height()))

#2
background1_2 = pygame.image.load("assets/parallax-forest-lights.png")
background1_2 = pygame.transform.scale(background1_2,(scale_background*background1_2.get_width(),scale_background*background1_2.get_height()))

#3
background1_3 = pygame.image.load("assets/parallax-forest-middle-trees.png")
background1_3 = pygame.transform.scale(background1_3,(scale_background*background1_3.get_width(),scale_background*background1_3.get_height()))

#4
background1_4 = pygame.image.load("assets/parallax-forest-front-trees.png")
background1_4 = pygame.transform.scale(background1_4,(scale_background*background1_4.get_width(),scale_background*background1_4.get_height()))

road_png = pygame.image.load("assets/road.png")

fire_png = pygame.image.load("assets/fire.png")
scale_fire = (160/fire_png.get_height())
fire_png = pygame.transform.scale(fire_png,(scale_fire*fire_png.get_width(),scale_fire*fire_png.get_height()))

# Velocidade dos backgrounds
velocidade1 = 1
velocidade2 = 2
velocidade3 = 3
velocidade4 = 4

# Definir variáveis para o jogo
dificuldade = 0
pos = 0
qtd_obstacles = [30,50,80]
spd_obstacles = [5,10,15]

# Array de posições dos backgrounds
background1_x = [0,408,816,1224,1632]
background2_x = [0,408,816,1224,1632]
background3_x = [0,408,816,1224,1632]
background4_x = [0,408,816,1224,1632]

obstacles_x = [(((i*80)+300*i))+1280 for i in range(qtd_obstacles[dificuldade])]
obstacles_y = [10] * qtd_obstacles[dificuldade]
array_road = [((i*1264)) for i in range(round(max(obstacles_x)/1264)+1)]
print(array_road)

# Função pra blitar os cenários
def blitParallelBackground_indiv(arraypos,img,speed,qtd):
    for i in range(qtd):
        tela.blit(img,(arraypos[i],0))
        arraypos[i]-=speed
        if arraypos[i] <= -408:
            arraypos[i] = max(arraypos)+408-5

def blitParallelBackground_full(matrixpos,arrayimg,arrayspeed):

    blitParallelBackground_indiv(matrixpos[0],arrayimg[0],arrayspeed[0],5)
    blitParallelBackground_indiv(matrixpos[1],arrayimg[1],arrayspeed[1],5)
    blitParallelBackground_indiv(matrixpos[2],arrayimg[2],arrayspeed[2],5)
    blitParallelBackground_indiv(matrixpos[3],arrayimg[3],arrayspeed[3],5)

# Defina o título da janela
pygame.display.set_caption("Projeto 08N JogosLab")

# Loop principal do jogo
executando = True
while executando:
    clock.tick(30)
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

    # Blitando o fundo da rua
    for i in range(len(array_road)):
        if array_road[i] <= largura and array_road[i] >= -1264:
            tela.blit(road_png,(array_road[i],240))
        array_road[i]-=spd_obstacles[dificuldade]

    # Blitando os obstaculos
    for i in range(qtd_obstacles[dificuldade]):
        if obstacles_x[i] <= largura and obstacles_x[i] >= -80:
            if obstacles_y[i] == 10:
                obstacles_y[i] = pos    
            tela.blit(fire_png,(obstacles_x[i],240+(obstacles_y[i])*160))
        obstacles_x[i]-=spd_obstacles[dificuldade]




    # Definindo posições, img e velocidades por fase
    matrixpos = [background1_x,background2_x,background3_x,background4_x]
    arrayimg = [background1_1,background1_2,background1_3,background1_4]
    arrayspeed = [velocidade1,velocidade2,velocidade3,velocidade4]
    blitParallelBackground_full(matrixpos,arrayimg,arrayspeed)


    # Desenhar personagem principal
    tela.blit(sprite_main.image,(0,240+pos*160))
    sprite_main.update()

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()