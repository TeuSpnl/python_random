turma = []

while True:
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    
    media = (n1 + n2) / 2

    turma.append([nome, [n1, n2], media])
    
    resp = ' '

    while resp not in "SN":
        resp = input("Você quer continuar? [S/N] ").upper().strip()[0]

    if resp == 'N':
        break
    
print('-=' * 60)
print(f'{"No.":^5} {"NOME":25} {"MÉDIA":^5}')
print('-' * 40)
for i, k in enumerate(turma):
    print(f'{i:^5} {k[0]:25} {k[-1]:^5.1f}')
    
while True:
    print(f'\n{"-="*60}')
    n = int(input("Mostrar as notas de qual aluno? (999 interrompe) "))
    
    if n == 999:
        break
    
    try:
        print(f"Notas de {turma[n][0]} são {turma[n][1]}")
    except:
        print("Não há aluno com esse id.")

    
print("Programa finalizado")