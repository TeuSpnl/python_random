import modulo108
from modulo108 import moeda

n = float(input("Digite o preço: R$"))
print(f"A metade de {moeda(n)} é {moeda(modulo108.metade(n))}")
print(f"O dobro de {moeda(n)} é {moeda(modulo108.dobro(n))}")
print(f"Aumentando 10%, temos {moeda(modulo108.dez_porc(n))}")
