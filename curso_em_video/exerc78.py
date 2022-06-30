lista = []

for i in range(5):
    lista.append(int(input(f"Insira o valor da posição {i}: ")))
    
    
print("")
print("-=" * 30)

print(f"Você digitou os valores: ", end= '')
for item in lista:
    print(item, end= ' ')

print(f"\nO \033[31mmaior\033[m valor digitado foi {max(lista)} e se encontra na(s) posição(ões) ", end= '')
for i, item in enumerate(lista):
    if item == max(lista):
        print(i, end= ' ')
        
print(f"\nO \033[32mmenor\033[m valor digitado foi {min(lista)} e se encontra na(s) posição(ões) ", end= '')
for i, item in enumerate(lista):
    if item == min(lista):
        print(i, end= ' ')