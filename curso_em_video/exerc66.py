cont = soma = 0

while True:
    n = int(input("Digite um número para somar [Digite 999 para parar]: "))
    
    if n == 999:
        break
    
    soma += n
    cont += 1
    
print(f"\nPrograma finalizado.\nNº de entradas: {cont}\nSoma total: {soma}")