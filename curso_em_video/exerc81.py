list = []

while True:
    list.append(int(input("Insira um valor: ")))
    
    resp = ' '
    
    while resp not in "SN":
        resp = input("Você quer continuar? [S/N] ").upper().strip()[0]
        
    if resp == 'N':
        break
    
print(f'\n{"-="*30}')
print(f"Você digitou {len(list)} elementos")

list.sort(reverse=True)
print(f"A lista em ordem decrescente é {list}")

if 5 in list:
    print("O valor 5 faz parte desta lista!")
else:
    print("Não há nenhum 5 nessa lista.")
    