from datetime import date


maior = menor = 0
anoAtu = date.today().year

for i in range(7):
    anoNasc = int(input(f"Digite o ano de nascimento da {i + 1}ª pessoa:"))
    idade = anoAtu - anoNasc
    if idade >=  18:
        maior += 1
    else:
        menor += 1
        
print(f'São {maior} pessoas que atingiram a maioridade e \nsão {menor} pessoas que ainda não atingiram a maioridade.')