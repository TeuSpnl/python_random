import random


class Gym:
    def __init__(self):
        # Cria a academia com 13 halteres, de 10 a 34 e coloca os halteres nos lugares certos do suporte
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.suporte = {}
        self.reiniciar_dia()

    def reiniciar_dia(self):
        # Coloca o halter i na posição i
        self.suporte = {i: i for i in self.halteres}

    def list_halteres(self):
        return [i for i in self.suporte.values() if i != 0]

    def pegar_halter(self, peso):
        # Pega a posição do haltére de peso {peso}
        pos_peso = list(self.suporte.values()).index(peso)
        # Pega a chave da posição do peso (Dicionário é chave:pos)
        key_suporte = list(self.suporte.keys())[pos_peso]
        self.suporte[key_suporte] = 0
        return peso

    def devolver_haltere(self, pos, peso):
        self.suporte[pos] = peso  # Coloca o peso na posição pos

    def calcula_caos(self):
        # Pega a quantidade de halteres que não estão no devido lugar
        num_caos = [i for i, j in self.suporte.items() if i != j]
        # Retorna a porcentagem de halteres que estão fora do lugar
        return len(num_caos) / len(self.suporte)


class User:
    def __init__(self, tipo, gym):
        pass


gym = Gym()
gym.suporte.items()
