from dis import dis
from pydoc import describe
from tkinter.tix import IMAGE
from turtle import distance
import pygame  # Biblioteca de criação de jogos
import random  # Gera números aleatórios
import os  # Integra esse código com os arquivos

SCREEN_WIDTH = 500
SCREEN_HEIGTH = 800

# O os junta o caminho com o nome do arquivo // O pygame vai carregar a imagem e aumentar a escala (tamanho) dela em 2x
IMAGE_PIPE = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'pipe.png')))

IMAGE_BASE = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'base.png')))

IMAGE_BG = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'bg.png')))

IMAGES_BIRD = [
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()  # Inicializa a fonte

FONT_POINTS = pygame.font.SysFont(
    'Old English Text MT', 50)  # Define a fonte da pontuação

# A gente só vai criar objetos para os itens que se movem no jogo


class Bird:
    IMGS = IMAGES_BIRD

    # Animações de rotação (A animação de descida e subida pra não ficar zoado)
    MAX_ROTATION = 25
    VEL_ROTATION = 20
    ANIM_TIME = 5

    def __init__(self, x, y):  # Definições iniciais do pássaro
        self.x = x
        self.y = y

        self.angle = 0
        self.jump_h = 0  # Altura do pulo
        self.heigth = self.y
        self.time = 0
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.jump_h = -8.5
        self.time = 0  # É o início do deslocamento dele
        self.heigth = self.y

    def move(self):  # Essa função acontece o tempo todo
        # Calcula o deslocamento
        self.time += 1
        displacement = 1.5 * (self.time**2) + self.jump_h * self.time
        # S = So + Vot + at^2/2

        # Restringir o deslocamento (para o pássaro não ficar acelerando infinitamente para baixo ou pra cima)
        if displacement > 16:
            displacement = 16

        elif displacement < 0:  # O pássaro tende a descer mais do que pula, esse impulso melhora a jogabilidade
            displacement -= 2

        self.y += displacement

        # Definir o ângulo do pássaro
        # Quando o pássaro está pulando, ou "subindo", vai ficar com a rotação máxima
        if displacement < 0 or self.y < (self.heigth + 50):
            if self.angle < self.MAX_ROTATION:
                self.angle = self.MAX_ROTATION

        else:
            if self.angle > -90:  # Enquanto o pássaro não está com o bico pra baixo, o ângulo dele vai descendo
                self.angle -= self.VEL_ROTATION

    def draw(self, screen):
        # Bater asa
        self.img_count += 1

        if self.img_count < self.ANIM_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIM_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIM_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIM_TIME*3:
            self.img = self.IMGS[1]
        elif self.img_count >= self.ANIM_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # Não bater asa quando o pássaro está caindo
        if self.angle <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIM_TIME*2

        # Printar

        # Rotaciona uma imagem (self.img) por um ângulo (self.angle)
        rotate_img = pygame.transform.rotate(self.img, self.angle)

        # Pega o centro
        img_center_pos = self.img.get_rect(topleft=(self.x, self.y)).center
        # get_rect sesenha o objeto dentro de um retângulo, é sempre usado para desenhar um objeto rotacionado na tela
        retangle = rotate_img.get_rect(center=img_center_pos)

        # Denha na tela a imagem e a posição que você quer desenhar ela.
        screen.blit(rotate_img, retangle.topleft)

    def get_mask(self):  # Pega a máscara (local dentro do retângulo que realmente tem a imagem) do pássaro
        return pygame.mask.from_surface(self.img)


class Pipe:
    DISTANCE = 200  # Espaço para o pássaro passar
    VELOCITY = 5

    def __init__(self, x):  # A altura do cano na tela, é gerada aleatoriamente dentro do próprio cano
        self.x = x
        self.heigth = 0
        self.pos_top = 0  # Eixo y
        self.pos_bottom = 0  # Eixo y
        # Flipa a imagem no eixo x e no eixo y
        self.PIPE_TOP = pygame.transform.flip(IMAGE_PIPE, False, True)
        self.PIPE_BOTTOM = IMAGE_PIPE
        self.passed = False

        self.set_heigth()

    def set_heigth(self):
        # Gera um número aletório dentro de um intervalo
        self.heigth = random.randrange(50, 450)
        self.pos_top = self.heigth - self.PIPE_TOP.get_height()
        self.pos_bottom = self.heigth + self.DISTANCE

    def move(self):
        self.x -= self.VELOCITY

    def draw(self, screen):
        screen.blit(self.PIPE_TOP, (self.x, self.pos_top))
        screen.blit(self.PIPE_BOTTOM, (self.x, self.pos_bottom))

    def bump(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        # Verificando colisão
        dist_top = (self.x - bird.x, self.pos_top - round(bird.y))
        dist_bottom = (self.x - bird.x, self.pos_bottom - round(bird.y))

        # Verifica se teve colisão
        colision_top = bird_mask.overlap(top_mask, dist_top)
        colision_bottom = bird_mask.overlap(bottom_mask, dist_bottom)

        if colision_top or colision_bottom:
            return True
        return False


class Base:
    VELOCITY = 5
    WIDTH = IMAGE_BASE.get_width()
    IMG = IMAGE_BASE

    def __init__(self, y):  # Só precisa do y, pois a função define o x dos chãos
        self.y = y
        self.x0 = 0
        self.x1 = self.WIDTH

    def move(self):
        self.x0 -= self.VELOCITY
        self.x1 -= self.VELOCITY

        if self.x0 + self.WIDTH < 0:
            self.x0 = self.x1 + self.WIDTH
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x0 + self.WIDTH

    def draw(self, screen):
        screen.blit(self.IMG, (self.x0, self.y))
        screen.blit(self.IMG, (self.x1, self.y))


# Desenha a tela do jogo
def drawScreen(screen, birds, pipes, base, points):
    screen.blit(IMAGE_BG, (0, 0))  # Desenha o fundo da tela
    for bird in birds:
        bird.draw(screen)

    for pipe in pipes:
        pipe.draw(screen)

    # O 1 ali é só pro texto não ficar pixelado e o fim é cor
    text = FONT_POINTS.render(f"Pontuação: {points}", 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 20 - text.get_width(), 20))  # (x, y)
    base.draw(screen)

    pygame.display.update()


def main():
    birds = [Bird(230, 350)]
    base = Base(730)
    pipes = [Pipe(700)]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    points = 0
    clock = pygame.time.Clock()  # De tanto em tanto tempo, o jogo vai rodar as coisas

    while True:
        clock.tick(30)  # 60 é o framerate. Controla o tempo do nosso jogo

        for event in pygame.event.get():  # Verifica se o jogo foi fechado
            if event.type == pygame.QUIT:
                False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # Verifica se o player apertou espaço
                if event.key == pygame.K_SPACE:
                    for bird in birds:
                        bird.jump()

        for bird in birds:
            bird.move()  # Move os pássaros
        base.move()  # Move o chão

        # Verifica se houve colisão e se deve criar, ou não, um novo cano
        add_pipe = False
        remove_pipes = []
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.bump(bird):
                    birds.pop(i)
                if not pipe.passed and bird.x > pipe.x:
                    pipe.passed = True
                    add_pipe = True
            pipe.move()
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                # Adiciona à lista pra não dar B.O. enquanto eu percorro a lista de canos
                remove_pipes.append(pipe)

        # Cria um novo cano
        if add_pipe:
            points += 1
            pipes.append(Pipe(600))

        # Remove os canos que é pra remover
        for pipe in remove_pipes:
            pipes.remove(pipe)

        # Define colisão com o chão e com o céu
        for i, bird in enumerate(birds):
            if (bird.y + bird.img.get_height()) > base.y or bird.y < 0:
                birds.pop(i)

        drawScreen(screen, birds, pipes, base, points)


if __name__ == '__main__':
    main()
