valor = float(input("Insira o valor da casa: "))
sal = float(input("Digite o seu salário: "))
anos = int(input("Por quantos anos de financiamento? "))

prest = valor / (anos * 12)

print(f"\nPara pagar um casa que custa R${valor:.2f} em {anos} anos, a prestação é R${prest:.2f} ao mês.")

if (prest <= sal * .3):
    print(f"\nComo a prestação é maior que {sal * .3} (30% do salário), o empréstimo foi \033[;32mpermitido\033[m.")
else:
    print(f"Como a prestação é menor que {sal * .3} (30% do salário), o empréstimo foi \033[;31mnegado\033[m.\n")
