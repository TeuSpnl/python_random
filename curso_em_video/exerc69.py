h = mulMenos20 = mais18 = 0

while True:
    print('-' * 40)
    print('CADASTRO DE PESSOAS')
    print('-' * 40)
    
    idade = int(input("Idade: "))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = input("Sexo: [M/F] ").upper().strip()
    
    if idade >= 18:
        mais18 += 1
    if sexo == 'F' and idade < 20:
        mulMenos20 += 1
    elif sexo == 'M':
        h += 1
    
    resp = ' '
    while resp not in 'SN':
        resp = input("Você quer continuar ou não? [S/N] ").upper().strip()
        
    if resp == 'N':
        break
        
print(f'''Foram cadastrados:
    {h} homens;
    {mulMenos20} mulheres com menos de 20 anos e
    {mais18} pessoas com + 18 anos''')