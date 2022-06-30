times = ('Palmeiras', 'Corinthians', 'Athletico PR', 'Internacional', 'Atlético-MG', 'Fluminense',
         'Santos', 'São Paulo', 'Flamengo', 'Botafogo', 'Avaí', 'Red Bull Bragantino', 'Atlético-GO',
         'Goiás', 'Ceará', 'Coritiba', 'América-MG', 'Cuiabá-MT', 'Juventude', 'Fortaleza')

print('-=' * 50)
print(f'Os 20 times do brasileirão na série A são: {times}')
print('-=' * 50)

print("\n")

print('-=' * 50)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-=' * 50)

print("\n")

print('-=' * 50)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 50)

print("\n")

print('-=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 50)

print("\n")

print('-=' * 50)
time = input('Digite um time a procurar: ').lower().capitalize()
try :
    print(f'Posição do {time}: {times.index(time)+ 1}ª')
except:
    print(f'Time {time} não está na série A')
print('-=' * 50)