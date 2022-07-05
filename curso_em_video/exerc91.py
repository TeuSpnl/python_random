from operator import itemgetter
from random import randint

players = []
player = {}

n = int(input("São quantos jogadores? "))

print("\nValores sorteados:")
for i in range(n):
    player['nome'] = f'{i + 1}'
    player['resultado'] = randint(1, 6)
    
    players.append(player.copy())
    
for i, p in enumerate(players):
    print(f'O jogador {p["nome"]} tirou o valor {p["resultado"]} nos dados')

ranking = []
ranking = sorted(players, key= itemgetter('resultado'), reverse= True)

print(f'\n{"-="*30}\nResultado final:\n')

for i, p in enumerate(ranking):
    print(f"Em {i+ 1}º lugar ficou {p['nome']} com {p['resultado']} no dado.")
    
