from random import randint


print('-'*20)
print(f'{"MEGA SENA":^20}')
print('-'*20)

n = int(input("Quantos jogos você quer que eu sorteie? "))

print(f"\n{'-='*3}", end= ' ')
print(f'SORTEANDO {n} JOGOS', end= ' ')
print('-='*3)

lista = []

for i in range(n):
    lista.clear()
    
    for c in range(8):
        num = randint(1, 60)
        
        while num in lista:
            num = randint(1, 60)
            
        lista.append(num)
    
    lista.sort()
    print(f"Jogo {i + 1}: {lista}")
    
print('-='*5, end= ' ')
print(f'BOA SORTE!', end= ' ')
print('-='*5)

    
    
    