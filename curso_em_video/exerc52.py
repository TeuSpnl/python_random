cont = 0
n = int(input("Digite um número: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(f"\033[32m{i}\033[m", end=' ')
        cont += 1
    else:
        print(f"\033[31m{i}\033[m", end= ' ')
        
if(cont == 2):
    print("\nEste número é primo.")
else:
    print(f"\nEsse número não é primo e é divisível por {cont} números")