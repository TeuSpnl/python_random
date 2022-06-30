print('-' * 40)
print('CAIXA ELETRÔNICO')
print('-' * 40)

n = int(input("Qual o valor que você quer sacar? "))

total = n
cedula = 50
nCedulas = 0

while True:
    
    if total >= cedula:
        total -= cedula
        nCedulas += 1
        
    else:
        if nCedulas > 0:
            print (f"{nCedulas} de R${cedula:.2f}")
            
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        
        nCedulas = 0
        
        if total == 0:
            break
            
        
        
            
    