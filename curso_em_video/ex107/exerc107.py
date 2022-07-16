import modulo107

n = float(input("Digite o preço: R$"))
print(f"A metade de R${n:.2f} é R${modulo107.metade(n):.2f}")
print(f"O dobro de R${n:.2f} é R${modulo107.dobro(n):.2f}")
print(f"Aumentando 10%, temos R${modulo107.dez_porc(n):.2f}")
