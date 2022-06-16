from random import choice

nome = []

for i in range(4):
    nome.append(input(f"Insira o nome do aluno {i+1}: "))
    
escolhido = choice(nome)

print(f"O aluno aleatoriamente escolhido foi {escolhido}.")