n = int(input("Digite um número para somar [Digite 999 para parar]: "))

cont = soma = 0

while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número para somar [Digite 999 para parar]: "))
    
print(f'Programa finalizado.\nSoma total: {soma}\nQuant. de entradas: {cont}')