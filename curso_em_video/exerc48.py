n = soma =  0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        n += 1
    
print(f"Foram {n} números e a soma total é {soma}")