maiorIdadeH = soma = media = maior = cont = 0

for i in range(4):
    print("\n")
    print("-"*5, end= '')
    print(f"{i + 1}ª Pessoa", end= '')
    print("-"*5)
    
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    sexo = ""
    while sexo != 'F' and sexo != 'M':
        sexo = input("Sexo [M/F]: ").upper()
        
    soma += idade
    
    if sexo == 'M' and idade > maior:
        maior = idade
        nomeVelho = nome
        
    if sexo == "M" and idade < 20:
        cont += 1
        
media = soma / 4

print(f"A média de idade é {media}.\nO homem mais velho tem {maior} e se chama {nomeVelho}.\n")

if cont > 1:
    print(f"Existem {cont} mulheres com mais de 20 anos.")
else:
    print(f"Existe {cont} mulher com mais de 20 anos.")
    