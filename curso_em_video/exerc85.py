ns = [[], []]

for i in range(7):
    n = int(input(f"Digite o {i + 1}º valor: "))
    
    if n % 2 == 0:
        ns[1].append(n)
    else:
        ns[0].append(n)
        
ns[0].sort()
ns[1].sort()
print(f"Os pares foram {ns[1]} e os ímpares foram {ns[0]}")