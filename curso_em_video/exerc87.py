matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0

for i in range(3):
    for j in range(3):
        n = int(input("Insira um número: "))
        matriz[i][j] = n
        
        if n % 2 == 0:
            somaPar += n
        
print(f"\n{'-='*30}")

for i, k in enumerate(matriz):
    for j, l in enumerate(matriz):
        print(f'[{matriz[i][j]:^5}]', end= '')
    print()

print(f"{'-='*30}\n")

print(f"A soma dos valores pares é {somaPar}")

for i, k in enumerate(matriz):
    somaCol = 0
    for j, l in enumerate(matriz):
        somaCol += matriz[j][i]
        
    print(f"A soma dos valores da {i + 1}ª coluna é {somaCol}")
    
for i, k in enumerate(matriz):
    maiorCol = matriz[0][i]
    for j, l in enumerate(matriz):
        if matriz[j][i] > maiorCol:
            maiorCol = matriz[j][i]
            
    print(f"O maior valor da {i + 1}ª coluna é {maiorCol}")
