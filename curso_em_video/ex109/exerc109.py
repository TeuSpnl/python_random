import modulo109
from modulo109 import moeda

n = float(input("Digite o preço: R$"))
print(f"A metade de {moeda(n)} é {modulo109.metade(n, True)}")
print(f"O dobro de {moeda(n)} é {modulo109.dobro(n, True)}")
print(f"Aumentando 10%, temos {modulo109.aum_porc(n, 10, True)}")
print(f"Diminuindo 13%, temos {modulo109.dim_porc(n, 13, True)}")
