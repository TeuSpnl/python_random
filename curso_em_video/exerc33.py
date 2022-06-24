valor = [1, 2, 3]

for i in range(3):
    valor[i] = int(input(f"Digite o {i + 1}º valor: "))

menor = valor[0]
maior = valor[0]

for i in range(3):
    if valor[i] < menor:
        menor = valor[i]
        
    elif valor[i] > maior:
        maior = valor[i]
        
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')