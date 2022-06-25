from random import randint
from time import sleep

resp = 0
while (resp < 1 or resp > 3):
    print('''JOKENPO
        [1]Pedra
        [2]Papel
        [3]Tesoura''')
    resp = int(input())

respBot = randint(0, 2)

itens = ("Pedra", "Papel", 'Tesoura')

print('JO')
sleep(.2)
print('KEN')
sleep(.2)
print('PO!')

print("-=" * 15)
print(f"Você jogou {itens[resp - 1]}")
print(f"O PC jogou {itens[respBot]}")
print("-=" * 15)

# Player Pedra
if resp == 1: 
    if respBot == 0: # B Pedra
        print("\033[33mEmpate!\033[m")
    elif respBot == 1: # B Papel
        print("Você \033[31mperdeu\033[m!")
    elif respBot == 2: # B Tesoura
        print("Parabéns! Você \033[32mganhou\033[m!")

# Player Papel
elif resp == 2: 
    if respBot == 0: # B Pedra
        print("Parabéns! Você \033[32mganhou\033[m!")
    elif respBot == 1:  # B Papel
        print("\033[33mEmpate!\033[m")
    elif respBot == 2: # B Tesoura
        print("Você \033[31mperdeu\033[m!")

# Player Tesoura
elif resp == 3:
    if respBot == 0: # B Pedra
        print("Você \033[31mperdeu\033[m!")
    elif respBot == 1: # B Papel
        print("Parabéns! Você \033[32mganhou\033[m!")
    elif respBot == 2: # B Tesoura
        print("\033[33mEmpate!\033[m")
