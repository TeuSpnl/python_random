def resumo (valor, aum, dim):
    aumento = moeda(aum_porc(valor, aum))
    diminuicao = moeda(dim_porc(valor, dim))
    dobro = moeda(dob(valor))
    metade = moeda(met(valor))
    
    print('-' * 20)
    print(f"{'RESUMO DO VALOR':^20}")
    print('-' * 20)
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Dobro do preço: \t{dobro}")
    print(f"Metade do preço: \t{metade}")
    print(f"{aum}% de aumento: \t{aumento}")
    print(f"{dim}% de redução: \t\t{diminuicao}")
    
def dob(v = 0):
    return v * 2

def met(v = 0):
    return v / 2
    
def aum_porc(v = 0, aum = 0):
    return v + (v * (aum/100))

def dim_porc(v = 0, dim = 0):
    return v - (v * (dim/100))

def moeda(valor = 0, moeda = "R$"):
    return f'{moeda}{valor:.2f}'.replace('.',',')