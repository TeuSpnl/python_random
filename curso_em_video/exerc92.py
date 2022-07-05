worker = {}

worker['nome'] = input("Nome: ")
anoNasc = int(input("Ano de nascimento: "))
worker['idade'] = 
worker['carteira'] = int(input("Nº Carteira de Trabalho (0 não tem): "))
if worker['carteira'] != 0:
    worker['anoContrat'] = input("Ano de Contratação: ")
    worker['salario'] = float(input("Salário: R$"))
    worker['aposentadoria'] = 

for k, v in worker.items():
    print(f"{k}: {v}")
