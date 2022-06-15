sal = float(input("Qual o atual salário do funcionário [separe decimais com ponto]? "))
porc_reaj = float(input("Qual a procentagem de reajuste? "))

reaj = sal + (sal * porc_reaj / 100)

print(f"O salário reajustado dele fica R${reaj:.2f}")