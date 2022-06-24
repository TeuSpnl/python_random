from datetime import date

ano = int(input("Ano de nascimento: "))

anoAtu = date.today().year
idade = anoAtu - ano

print(f"Idade: {idade}.", end=(' '))

if idade > 18:
    print(f"Você é maior de 18 e deve estar alistado há {idade - 18} ano(s), desde o ano de {anoAtu - (idade - 18)}.")
elif idade == 18:
    print("Você deve se alistar nesse ano.")
else:
    print(f"Você é menor de 18, só precisa se alistar em {ano + 18}, daqui {ano + 18 - anoAtu} anos.")
    
