n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1

if (n == 1):
    print(f"{t1}")
    
elif (n == 2):
    print(f'{t1} - {t2}')
    
elif (n > 2):
    print(f'{t1} - {t2}', end=' - ')
    
    i = 2
    
    while i < n:
        soma = t1 + t2
        
        print(soma, end='')
        print(" - " if i < (n - 1) else "", end='')
        
        t1 = t2
        t2 = soma
        
        i += 1
        
print("\nPrograma Finalizado.")