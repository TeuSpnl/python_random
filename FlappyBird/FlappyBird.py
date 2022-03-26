from dis import dis
import pygame #Biblioteca de criação de jogos
import random #Gera números aleatórios
import os #Integra esse código com os arquivos

SCREEN_WIDTH = 500
SCREEN_HEIGTH = 800

#O os junta o caminho com o nome do arquivo // O pygame vai carregar a imagem e aumentar a escala (tamanho) dela em 2x
IMAGE_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png'))) 
IMAGE_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGE_BG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGES_BIRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
    ]

pygame.font.init() #Inicializa a fonte

FONT_POINTS = pygame.font.SysFont('Old English Text MT',50) #Define a fonte da pontuação

#A gente só vai criar objetos para os itens que se movem no jogo
class Bird:
    IMGS = IMAGES_BIRD
    
    #Animações de rotação (A animação de descida e subida pra não ficar zoado)
    MAX_ROTATION = 25
    VEL_ROTATION = 20
    ANIM_TIME = 5

    def __init__(self, x, y):
        self.y = y
        self.x = x
        
        self.angle = 0
        self.velocity = 0
        self.heigth = self.y
        self.time = 0
        self.img_count = 0
        self.img = IMGS[0]
        
    def pular(self):
        self.velocity = -10.5
        self.time = 0 #É o início do deslocamento dele
        self.heigth = self.y
        
    def move(self): #essa função acontece o tempo todo
        #Calcular o deslocamento
        self.time += 1
        displacement = 1.5 * (self.time^2) + self.velocity * self.time
        
        #Restringir o deslocamento (para o pássaro não ficar acelerando infinitamente para baixo ou pra cima)
        if displacement > 16:
            displacement = 16
            
        elif displacement < 0: #O pássaro tende a descer mais do que pula, esse impulso melhora a jogabilidade
            displacement -= 2
            
        self.y = displacement
        
        #Definir o ângulo do pássaro
        if displacement < 0 or self.y < (self.heigth + 50):
            self.angle = 45
        
#S = So + Vot + at^2/2
        
        
    
class Pipe:
    pass

class Base:
    pass
