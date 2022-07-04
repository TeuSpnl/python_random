matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range (3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))
        
for i, c in enumerate(matriz):
    for j, k in enumerate(matriz):
        print(f'[{matriz[i][j]:^5}]', end= '')
    print()
    