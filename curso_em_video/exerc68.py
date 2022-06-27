from random import randint

win = 0
print("-=" * 30)
print("PAR OU ÍMPAR")
print("-=" * 30)

while True:
    nPlayer = int(input("Digite um valor: "))
    nBot = randint(0, 10)
    soma = nPlayer + nBot

    resp = 'n'
    while resp not in 'PpIi':
        resp = input("Par ou Ímpar? [P/I] ").strip().upper()

    print(f'''
O player escolheu: {resp} e digitou o número: {nPlayer}
O Pc colocou o número: {nBot}
A soma é: {soma} ''', end= '')
    print("PAR" if soma % 2 == 0 else "ÍMPAR")

    if resp == 'I':
        if soma % 2 == 0:
            print(f"\033[31mVocê perdeu!\033[m")
            break
        else:
            print("\033[32mVocê ganhou!\033[m")
            win += 1
    else:
        if soma % 2 == 0:
            print("\033[32mVocê ganhou!\033[m")
            win += 1
        else:
            print(f"\033[31mVocê perdeu!\033[m")
            break
            
    print("\nBora jogar de novo!\n")
    
print(f"Você ganhou {win} vezes.")
