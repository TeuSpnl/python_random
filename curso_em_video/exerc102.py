def fatorial(valor, show=False):
    """
    Calcula o fatorial de um número e mostra, caso o usuário deseje, a equação.
    
    :param valor: O número a ser fatorado.
    :param show: (opcional) Mostra ou não a equação
    
    :return: O resultado do fatorial do valor.
    """
    
    
    i = valor
    result = 1
    while i > 0:
        if show:
            print(i, end= ' ')
            if i != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        i -= 1
        
        result *= valor
        valor -= 1
        
    return f"{result}"
        
print('-' * 20)
print(fatorial(5, show= True))