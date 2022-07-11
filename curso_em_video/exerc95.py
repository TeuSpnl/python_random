jogador = {}
jogadores = []
gols = []

while True:
    gols.clear()
    jogador['nome'] = input("Nome do jogador: ").lower().title()
    part = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for i in range(part):
        gols.append(int(input(f"Quantas gols na partida {i + 1}? ")))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    sn = ' '
    while sn not in 'SN':
        sn = input("Deseja continuar? [S/N] ").strip().upper()[0]

    if sn == 'N':
        break

print(f'\n{"-="*30}')
print(f'{"Cod":>4}', end=' ')
for i in jogador.keys():
    print(f'{i.lower().title():20}', end='')
print(f'\n{"-"*60}')

for i, jog in enumerate(jogadores):
    print(f"{i:>4}", end=' ')
    for v in jog.values():
        print(f"{str(v):20}", end='')
    print()
    
resp = int(input("\nMostrar os dados de qual jogador? (999 para parar) "))

while resp != 999:
    try:
        print(f"Levantamento do jogador {jogadores[resp]['nome']}:")
        for j, n in enumerate(jogadores[resp]['gols']):
            print(f"    No jogo {j + 1} fez {n} gols.")
    except:
        print(f"Não há jogador com id {resp}.")
    
    resp = int(input("\nMostrar os dados de qual jogador? (999 para parar) "))

print("Programa finalizado.")