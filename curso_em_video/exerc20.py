from random import shuffle

nome = []

for i in range(4):
    nome.append(str(input(f"Insira o nome da {i+1}ª pessoa: ")))

shuffle(nome)

print(nome)
print(f"A ordem de apresentação é: {nome}")
    
    