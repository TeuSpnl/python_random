from itertools import count


n = (int(input("Digite um número: ")),
     int(input("Digite um número: ")),
     int(input("Digite um número: ")),
     int(input("Digite um número: ")),)

print(f"Você digitou os números {n}")
print(f"Dos números digitados, {n.count(9)} eram 9")

try:
    print(f"O primeiro número 3 apareceu na {n.index(3) + 1}ª posição.")
except:
    print("Você não digitou nenhum número 3.")
    
print("Você digitou os seguintes números pares: ", end='')
for i in n:
    if i % 2 == 0:
        print(i, end= ' ')