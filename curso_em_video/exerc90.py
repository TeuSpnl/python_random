turma = {}

turma['nome'] = input("Nome: ").lower().capitalize()
turma['media'] = float(input(f"Média de {turma['nome']}: "))

if turma['media'] >= 7:
    turma['situacao'] = 'Aprovado.'
elif 7 >  turma['media'] >= 5:
    turma['situacao'] = 'Em recuperação.'
else:
    turma['situacao'] = 'Reprovado.'
    
print(f'\n{"-="*30}')

for k, v in turma.items():
    print(f"{k}: {v}")
    