lista = []

for i in range(5):
    n = int(input("Insira um valor: "))
    
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print(f"O valor {n} foi adicionado no final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"O valor {n} foi adicionado na posição {pos}")
                break
            
            pos += 1
        
print(f'\n{"-="*30}')
print(f"A lista ordenada ficou: {lista}")
