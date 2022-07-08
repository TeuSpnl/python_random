
from datetime import date


worker = {}

worker['nome'] = input("Nome: ")
anoNasc = int(input("Ano de nascimento: "))
anoAtu = date.today().year
worker['idade'] = anoAtu - anoNasc
worker['carteira'] = int(input("Nº Carteira de Trabalho (0 não tem): "))
if worker['carteira'] != 0:
    worker['anoContrat.'] = int(input("Ano de Contratação: "))
    worker['salario'] = float(input("Salário: R$"))
    worker['aposentadoria'] = (worker['idade'] - (anoAtu - worker['anoContrat'])) + 35

print(f'\n{"-="*30}')

for k, v in worker.items():
    print(f"{k.title()}: {v}")