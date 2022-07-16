def notas(*n, sit=False):
    """
    -> Função que analisa notas e situações de alunos
    
    :param n: valor da(s) nota(s) do aluno
    :param sit: (opcional) Indica se deve ou não aparecer a situação do aluno
    :return: dicionário com várias informações sobre o aluno
    """
    
    ficha = {}
    
    media = sum(n) / len(n)

    ficha['total'] = len(n)
    ficha['maior'] = max(n)
    ficha['menor'] = min(n)
    ficha['media'] = media

    if sit:
        if media >= 7:
            ficha['situação'] = 'Aprovado'
        elif media >= 5:
            ficha['situação'] = 'Recuperação'
        else:
            ficha['situação'] = 'Reprovado'

    return ficha


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
