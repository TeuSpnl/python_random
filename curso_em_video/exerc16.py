from random import uniform


num = uniform(1, 99999)
roundNum = round(num)

print(f"O programa criou um número aleatório entre 1 e 99.999. \n Este número é {num:.2f}")
print(f"Sua porção inteira é {int(num)}")
# print(f"Arredondando, ele fica {roundNum}")



