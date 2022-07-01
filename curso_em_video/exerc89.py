lista = []
turma = []

while True:
    lista.clear()
    
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    
    media = (n1 + n2) / 2

    lista.append(nome)
    lista.append(n1)
    lista.append(n2)
    lista.append(media)
    
    turma.append(lista[:])
    
    resp = ' '

    while resp not in "SN":
        resp = input("Você quer continuar? [S/N] ").upper().strip()[0]

    if resp == 'N':
        break
    
print('-=' * 60)
print(f'{"No.":^5} {"NOME":25} {"MÉDIA":^5}')
print('-' * 40)
for i, k in enumerate(turma):
    print(f'{i:^5} {k[0]:25} {k[-1]:^5}')
    
while True:
    print(f'\n{"-="*60}')
    n = int(input("Mostrara as notas de qual aluno? (999 interrompe) "))
    
    print(f"Notas de {turma[n][0]} são {turma[n][1:3]}")

    if n == 999:
        break
    
print("Programa finalizado")