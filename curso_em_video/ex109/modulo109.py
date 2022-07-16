def metade(n, form = False):
    return(n/2) if form is False else (moeda(n/2))

def dobro(n, form = False):
    return(n * 2) if form is False else (moeda(n * 2))

def aum_porc(n, porc, form = False):
    total = (n + (n*(porc/100)))
    return total if form is False else moeda(total)

def dim_porc(n, porc, form = False):
    total = n - (n*(porc/100))
    return total if form is False else moeda(total)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')