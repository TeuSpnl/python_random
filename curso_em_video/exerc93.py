gols = []
dados = {}

dados['nome'] = input("Nome do jogador: ")
part = int(input(f"Quantas partidas {dados['nome']} jogou? "))

for i in range(1, part + 1):
    gols.append(int(input(f"    Quantos gols na partida {i}? ")))

dados['gols'] = gols[:]
dados['total'] = sum(gols)

print(f'\n{"-="*30}')
print(dados)
print(f'{"-="*30}')

print()
for k, v in dados.items():
    print(f'{k.title()}: {v}')

print(f'\n{"-="*30}')
print(f"O jogador {dados['nome']} jogou {len(gols)} partidas:")
for i, n in enumerate(gols):
    print(f"    => Na partida {i + 1}, fez {n} gols.")
print(f"Foram um total de {dados['total']} gols.")
