grupo = []
dados = []

while True:
    dados.append(input("Nome: ").strip().lower().capitalize())
    dados.append(float(input("Peso: ").strip()))
    
    if len(grupo) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    
    grupo.append(dados[:])
    
    dados.clear()
    
    resp = ' '

    while resp not in "SN":
        resp = input("Você quer continuar? [S/N] ").upper().strip()[0]

    if resp == 'N':
        break
    
    
print(f'\n{"-="*30}')
print(f"Os dados inseridos foram: {grupo}.")
print(f"Foram cadastrados {len(grupo)} pessoas")

maiores = []
menores = []

for i, pessoa in enumerate(grupo):
    if pessoa[1] == maior:
        maiores.append(pessoa[0])
        
    if pessoa[1] == menor:
        menores.append(pessoa[0])


print(f"O maior peso foi {maior}Kg de {maiores}.\nO menor peso foi {menor}Kg de {menores}.")
