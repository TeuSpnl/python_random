from statistics import mean


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) /2

print(f"Média: {media}")

if (media >= 7):
    print("O alundo foi \033[1;32maprovado\033[m!")
elif (media >= 4 and media < 7):
    print("O aluno está de \033[1;33mrecuperação\033[m.")
else:
    print("O aluno foi \033[1;31mreprovado\033[m!")

