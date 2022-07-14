def notas(*n, sit=False):
    ficha = {}

    for i, nota in enumerate(n):
        if i == 0:
            menor = maior = nota
        elif nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota

    media = sum(n) / len(n)

    ficha['total'] = len(n)
    ficha['maior'] = maior
    ficha['menor'] = menor
    ficha['media'] = media

    if sit:
        if media >= 7:
            ficha['situação'] = 'Aprovado'
        elif 7 < media > 5:
            ficha['situação'] = 'Recuperação'
        else:
            ficha['situação'] = 'Reprovado'

    return ficha


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
