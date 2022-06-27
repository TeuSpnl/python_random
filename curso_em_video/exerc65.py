soma = cont = 0

resp = 'S'
while resp in 'Ss':
    n = int(input("Digite um número: "))
    
    soma += n
    cont += 1
    
    if cont == 1:
        maior = n
        menor = n
        
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    
    
    resp = ''
    while resp.upper() != 'S' and resp.upper() != 'N':
        resp = input("Você quer continuar ou não? [S/N] ")
        
        
media = soma / cont
print(f"Programa finalizado.\nQuant. de entradas: {cont}\nMédia: {media}\nMaior valor: {maior}  ||  Menor valor: {menor}")