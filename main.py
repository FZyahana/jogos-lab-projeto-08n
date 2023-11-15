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
            png = pygame.transform.scale(
                png, (escala*png.get_width(), escala*png.get_height()))
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

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image


# Função pra blitar os cenários


def blitParallelBackground_indiv(arraypos, img, speed, qtd):
    for i in range(qtd):
        tela.blit(img, (arraypos[i], 0))
        arraypos[i] -= speed
        if arraypos[i] <= -408:
            arraypos[i] = max(arraypos)+408-5


def blitParallelBackground_full(backgrounds_x, backgrounds, spd_backgrounds,qtd):
    for i in range(len(backgrounds)):
        blitParallelBackground_indiv(backgrounds_x[i], backgrounds[i],spd_backgrounds[i], qtd)

def fixScaleBg(background_img,altura):
    scale = altura/background_img.get_height()
    return pygame.transform.scale(background_img,(scale*background_img.get_width(),scale*background_img.get_height()))

def setParallelBackground(dificuldade):
    if dificuldade == 0:
        # Importar o fundo fase 1
        # Considerando que todas as imagens de um parallel vão ter mesmo tamanho, vou deixar o código eficiente
        background1 = pygame.image.load("assets/fase0/0.png")
        background1 = fixScaleBg(background1,240)
        # 2
        background2 = pygame.image.load("assets/fase0/1.png")
        background2 = fixScaleBg(background2,240)

        # 3
        background3 = pygame.image.load("assets/fase0/2.png")
        background3 = fixScaleBg(background3,240)

        # 4
        background4 = pygame.image.load("assets/fase0/3.png")
        background4 = fixScaleBg(background4,240)


        # obstaculo
        obstacle_png = pygame.image.load("assets/fase0/fire.png")
        scale_obstacle = (160/obstacle_png.get_height())
        obstacle_png = pygame.transform.scale(
            obstacle_png, (scale_obstacle*obstacle_png.get_width(), scale_obstacle*obstacle_png.get_height()))
        
        obstacle = Obstacle(obstacle_png)
        backgrounds = [background1,background2, background3, background4]

    elif dificuldade == 1:
        background1 = pygame.image.load("assets/fase1/0.png")
        background1 = fixScaleBg(background1,240)

        background2 = pygame.image.load("assets/fase1/1.png")
        background2 = fixScaleBg(background2,240)

        background3 = pygame.image.load("assets/fase1/2.png")
        background3 = fixScaleBg(background3,240)

        background4 = pygame.image.load("assets/fase1/3.png")
        background4 = fixScaleBg(background4,240)

        backgrounds = [background1,background2, background3, background4]

        obstacle_png = pygame.image.load("assets/fase1/obstacles.png")
        scale_obstacle = (160/obstacle_png.get_height())
        obstacle_png = pygame.transform.scale(
            obstacle_png, (scale_obstacle*obstacle_png.get_width(), scale_obstacle*obstacle_png.get_height()))
        obstacle = Obstacle(obstacle_png)
    
    elif dificuldade == 2:
        background1 = pygame.image.load("assets/fase2/0.png")
        background1 = fixScaleBg(background1,240)

        background2 = pygame.image.load("assets/fase2/1.png")
        background2 = fixScaleBg(background2,240)

        background3 = pygame.image.load("assets/fase2/2.png")
        background3 = fixScaleBg(background3,240)

        background4 = pygame.image.load("assets/fase2/3.png")
        background4 = fixScaleBg(background4,240)

        background5 = pygame.image.load("assets/fase2/4.png")
        background5 = fixScaleBg(background5,240)

        background6 = pygame.image.load("assets/fase2/5.png")
        background6 = fixScaleBg(background6,240)

        background7 = pygame.image.load("assets/fase2/6.png")
        background7 = fixScaleBg(background7,240)

        backgrounds = [background1,background2, background3, background4, background5, background6, background7]

        obstacle_png = pygame.image.load("assets/fase2/obstacles.png")
        scale_obstacle = (160/obstacle_png.get_height())
        obstacle_png = pygame.transform.scale(
            obstacle_png, (scale_obstacle*obstacle_png.get_width(), scale_obstacle*obstacle_png.get_height()))
        obstacle = Obstacle(obstacle_png)


    return backgrounds, obstacle

# Importar a imagem do corredor
sprite_image_files = ["Run (1).png", "Run (2).png", "Run (3).png", "Run (4).png",
                      "Run (5).png", "Run (6).png", "Run (7).png", "Run (8).png"]
for i in range(len(sprite_image_files)):
    sprite_image_files[i] = "assets\\sprite\\" + sprite_image_files[i]
sprite_main = AnimatedSprite(sprite_image_files, 0, 0, 40)


road_png = pygame.image.load("assets/road.png")
menu_png = pygame.image.load("assets/menu.png")
gameover_png = pygame.image.load("assets/gameover.png")
instrucoes_png = pygame.image.load("assets/instrucoes.png")
hit = pygame.mixer.Sound("assets/sounds/colision.mp3")

music = pygame.mixer.Sound("assets/sounds/background_music.mp3")
music.set_volume(0.1)

# Definir variáveis para o jogo
dificuldade = 0
pos = 0
qtd_obstacles = [30, 50, 80]
spd_obstacles = [15, 30, 45]

# Array de posições dos backgrounds
qtd_backgrounds_x = 5

# Defina o título da janela
pygame.display.set_caption("Projeto 08N JogosLab")

# Loop principal do jogo
menu = True
executando = True
gameover = False
sound_play_hit = False
instrucoes = False
sound_toggle = True

music.play(loops=-1)
while executando:
    clock.tick(60)
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
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if menu:
                if botao_jogar.collidepoint(evento.pos):
                    tempo_inicial = pygame.time.get_ticks()
                    menu = False
                    dificuldade = 0
                    backgrounds, obstacle = setParallelBackground(dificuldade)
                    backgrounds_x = [[(x*408) for x in range(qtd_backgrounds_x)] for i in range(len(backgrounds))]
                    obstacles_x = [(((i*80)+300*i)) +
                                1280 for i in range(qtd_obstacles[dificuldade])]
                    obstacles_y = [10] * qtd_obstacles[dificuldade]
                    array_road = [((i*1264)) for i in range(round(max(obstacles_x)/1264)+1)]
                    spd_backgrounds = [i+1 for i in range(len(backgrounds))]
                    sound_play_hit = False
                elif botao_instrucao.collidepoint(evento.pos):
                    menu = False
                    instrucoes = True
                elif botao_som.collidepoint(evento.pos):
                    if sound_toggle:
                        music.stop()
                    else:
                        music.play(loops=-1)
                    sound_toggle = not(sound_toggle)
            elif gameover or instrucoes:
                if (botao_menu.collidepoint(evento.pos)):
                    gameover = False
                    instrucoes = False
                    menu = True
                

    # Limpar a tela
    tela.fill((0, 0, 0))  # Preencher a tela com a cor preta
    if menu:

        botao_jogar = pygame.Rect(196.20, 479.02, 191.6, 77.87)
        botao_instrucao = pygame.Rect(759.93, 477.83, 330.14, 77.87)
        botao_som = pygame.Rect(1112.50,27,167.5,167.5)
        pygame.draw.rect(tela, (0, 0, 0, 0), botao_jogar)
        pygame.draw.rect(tela, (0, 0, 0, 0), botao_instrucao)
        pygame.draw.rect(tela, (0, 0, 0, 0), botao_som)
        tela.blit(menu_png, (0, 0))

    elif gameover:
        tempo_final = pygame.time.get_ticks()
        pontuacao = tempo_final - tempo_inicial
        # music.stop()
        
        botao_menu = pygame.Rect(412.43,581.02,459.14,77.87)
        pygame.draw.rect(tela,(0,0,0,0), botao_menu)
        tela.blit(gameover_png,(0,0))
        
        pygame.display.flip()
        if sound_play_hit == False:
            if sound_toggle:
                hit.set_volume(0.3)
                hit.play()
            sound_play_hit = True
            jogador = input("Nome: ")
            with open('pontuacoes.txt', 'a') as file:
                file.write(jogador + ": " + str(pontuacao) +'\n')
            
        
    elif instrucoes:
        botao_menu = pygame.Rect(412.43,581.02,459.14,77.87)
        pygame.draw.rect(tela,(0,0,0,0), botao_menu)
        tela.blit(instrucoes_png,(0,0))
        
    else:
        

        # Blitando o fundo da rua
        for i in range(len(array_road)):
            if array_road[i] <= largura and array_road[i] >= -1264:
                tela.blit(road_png, (array_road[i], 240))
            array_road[i] -= spd_obstacles[dificuldade]

        # Blitando os obstaculos
        for i in range(qtd_obstacles[dificuldade]):

            if obstacles_x[i] <= largura and obstacles_x[i] >= -80:
                if obstacles_y[i] == 10:

                    obstacles_y[i] = pos

                tela.blit(obstacle.image,
                          (obstacles_x[i], 240+(obstacles_y[i])*160))

            if (obstacles_x[i] <= 110 and obstacles_x[i] > -30) and obstacles_y[i] == pos:

                print("atritou")
                gameover = True
            obstacles_x[i] -= spd_obstacles[dificuldade]

            if (obstacles_x[qtd_obstacles[dificuldade]-1] < -80):
                if dificuldade < 2:

                    dificuldade += 1
                    backgrounds, obstacle = setParallelBackground(dificuldade)
                    backgrounds_x = [[(x*408) for x in range(qtd_backgrounds_x)] for i in range(len(backgrounds))]
                    obstacles_x = [
                        (((i*80)+300*i))+1280 for i in range(qtd_obstacles[dificuldade])]
                    obstacles_y = [10] * qtd_obstacles[dificuldade]
                    array_road = [((i*1264))
                                for i in range(round(max(obstacles_x)/1264)+1)]
                    
                    if dificuldade == 2:
                        spd_backgrounds = [4*i for i in range(7)]
                    else:
                        spd_backgrounds = [2*i for i in spd_backgrounds]
                else:
                    gameover = True

        
        blitParallelBackground_full(backgrounds_x, backgrounds, spd_backgrounds,qtd_backgrounds_x)

        # Desenhar personagem principal
        tela.blit(sprite_main.image, (0, 240+pos*160))
        sprite_main.update()

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()

with open('pontuacoes.txt', 'r') as file:
    linhas = [line.strip() for line in file]

# Criando uma lista de tuplas (nome, pontuacao) a partir das linhas
dados_pontuacao = [(linha.split(': ')[0], int(linha.split(': ')[1])) for linha in linhas]

# Ordenando a lista com base nas pontuações (em ordem decrescente)
dados_pontuacao_ordenados = sorted(dados_pontuacao, key=lambda x: x[1], reverse=True)

# Imprimindo no console
for nome, pontuacao in dados_pontuacao_ordenados:
    print(f'Jogador: {nome}, Pontuação: {pontuacao}')

sys.exit()
