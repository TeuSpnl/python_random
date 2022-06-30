from re import M


lista = ('Borracha', 1.5,
         '20 Lápis', 10,
         'Caderno', 15,
         'Livro de Matemática', 49.9,
         'Livro de Literatura', 39.9,
         'Mochila', 120,
         '20 Canetas', 12.99)

print("-=" * 20)
print(f'{"LISTA DE PRODUTOS":^40}')
print("-=" * 20)

print('')

for i, item in enumerate(lista):
    if i % 2 == 0:
        print(f'{item:-<30}', end= ' R$')
    else:
        print(f'{item:.2f}')        