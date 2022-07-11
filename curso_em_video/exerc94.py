pessoa = {}
pessoas = []
totalIdade = 0

while True:
    pessoa['nome'] = input("Nome: ").lower().title()
    
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input("Sexo: [M/F] ").upper().strip()[0]
        
    pessoa['idade'] = int(input("Idade: "))
    totalIdade += pessoa['idade']
    
    pessoas.append(pessoa.copy())
    
    sn = ' '
    while sn not in 'SN':
        sn = input("Deseja continuar? [S/N] ").strip().upper()[0]

    if sn == 'N':
        break
    
print(f'\n{"-="*30}')
media = totalIdade / len(pessoas)

print(f'Ao todo, temos {len(pessoas)} pessoas cadastradas')
print(f"A média de idade é: {media:.2f}")
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f"{p['nome']}", end=' e ')
print('só.')
print("Lista de pessoas que estão acima da média:")
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f"{k}: {v}", end='; ')
    print()

