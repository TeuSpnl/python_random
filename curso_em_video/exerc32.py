from datetime import date


ano = int(input("Digite um ano (Escreva 0 para falar do ano atual): "))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} não é BISSEXTO")