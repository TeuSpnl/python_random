n = soma = 0

for i in range(6):
    num = int(input("Insira um número: "))
    if num % 2 == 0:
        soma += num
        n += 1
        
print(f'Você digitou {n} números pares. A soma é: {soma}')
