cont = mil = soma = 0

while True:
    cont += 1
    
    nome  = input("Nome do produto: ").lower().capitalize()
    valor = float(input("Preço: R$"))
    
    soma += valor
    
    if valor > 1000:
        mil += 1
    
    if cont == 1:
        menor = valor
        nomeMenor = nome
        
    elif valor < menor:
        menor = valor
        nomeMenor = nome
        
    resp = ' '
    while resp not in 'SN':
        resp =  input('Adicionar mais produtos? [S/N]').upper().strip()[0]
        
    if resp == 'N':
        break
    
print(f'''Programa finalizado
Total gasto: R${soma:.2f}
{mil} produto(s) custa(m) mais de R$1000.00
O produto mais barato foi {nomeMenor} e custa R${menor:.2f}''')

    