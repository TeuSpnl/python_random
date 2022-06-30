while True:
    resp = -1

    while True:
        n = int(input("\nDigite um número entre 0 e 20: "))
        
        if 0 <= n <= 20:
            break 
        
    extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
            'dezoito', 'dezenove', 'vinte')

    print(f"Você digitou o número {extenso[n]}")
    
    sn = ' '    
    while sn not in 'SN':
        sn = input("Deseja continuar? [S/N] ").strip().upper()[0]
        
    if sn == 'N':
        break
    
print("Programa finalizado.")