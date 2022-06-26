from random import randint

cont = 0
n = randint(0, 10)

print("Olá! Eu pensei em um número entre 0 e 10. Tente adivinhar qual é!")
resp = int(input())

if resp == n:
    print(f"Uau! De primeira! Parabéns!\nEu realmente pensei em {n}.")
else:
    acertou = False
    while not acertou:
        cont += 1
        
        if resp == n:
            acertou = True
        else:
            print("Poxa! Não foi dessa vez que você conseguiu. Mas não desista ", end='')
            if resp > n:
                print("e coloque menos dessa vez.")
                resp = int(input())
            else: 
                print("e coloque um pouco mais... ( ͡° ͜ʖ ͡°)")
                resp = int(input())
    
    print(f"Boa! Agora sim acertou. Foram {cont} tentativas pra adivinhar que eu pensei {n}.")
