def leiaInt(msg):
    n = str(input(msg))
    
    while not n.isnumeric():
        print("\033[31mERRO! Digite um número inteiro\033[m")
        msg = input("Digite um número: ")
        n = str(msg)
    
    return n
    
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')