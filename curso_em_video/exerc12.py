valor = float(input("Qual o valor atual do produto [use ponto para separar os decimais]? "))
desc = float(input("Qual a porcentagem do desconto? "))

v_final = valor - (valor * (desc / 100))

print(f"O valor final do produto fica {v_final:.2f} com um desconto de {desc}%")