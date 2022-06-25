from datetime import date


anoNasc = int(input("Qual o seu ano de nascimento? "))

idade = date.today().year - anoNasc

if idade > 1:
    print(f'Idade: {idade} anos;')
else:
    print(f'Idade: {idade} ano;')

print("Categoria: \033[;32m", end= (''))

if idade <= 7:
    print("Mirim\033[m")
elif idade <= 12:
    print("Infantil\033[m")
elif idade <= 18:
    print("Júnior\033[m")
elif idade <= 25:
    print("Sênior\033[m")
else:
    print("Master\033[m")
