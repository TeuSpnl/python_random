import random


class Gym:
    def __init__(self):
        # Cria a academia com 13 halteres, de 10 a 34 e coloca os halteres nos lugares certos do suporte
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.suporte = {} 
        self.reiniciar_dia()
        
    def reiniciar_dia(self):
        self.suporte = {i:i for i in self.halteres} # Coloca o halter i na posição i
        
        
        
gym = Gym()
