tupla = ('aprender', 'programar', 'Linguagem', 'python', 'curso', 'estudar', 
         'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in tupla:
    print(
        f'\nNa palavra \033[32m{palavra.lower()}\033[m temos as vogais: ', end='')
    for letra in palavra:
        if letra in ('aeiou'):
            print(letra, end= ' ')