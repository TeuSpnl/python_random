from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram ', end= '')
for i in n:
    print(i, end= ' ')
    
print(f"\nO maior valor foi {max(n)} e o menor foi {min(n)}")