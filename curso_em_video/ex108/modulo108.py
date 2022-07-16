def metade(n):
    return(n/2)

def dobro(n):
    return(n * 2)

def dez_porc(n):
    return(n + (n*.1))

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')