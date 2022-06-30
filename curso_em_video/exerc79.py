list = []

while True:
    n = int(input("Insira um valor: "))
    
    if n in list:
        print(f"Já tem {n} na lista. Não vou adicionar.")
    else:
        list.append(n)
        print(f'{n} inserido na lista')

    resp = ' '

    while resp not in "SN":
        resp = input("Você quer continuar? [S/N] ").upper().strip()[0]

    if resp == 'N':
        break
    
print(f"Os valores inseridos foram: {sorted(list)}")
