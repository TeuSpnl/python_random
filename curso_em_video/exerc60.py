from math import factorial


n = int(input("Digite um número para ver o fatorial: "))

print(f'{n}! = ', end='')

f = 1

for i in range(n, 0, -1):
    print(f"{i}", end= '')
    print(' x ' if i > 1 else ' = ', end='')
    
print(factorial(n))