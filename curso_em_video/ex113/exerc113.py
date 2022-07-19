from mod113 import *

while True:
    try:
        n = leiaInt('Digite um número inteiro: ')
    except:
        n = leiaInt('Digite um número inteiro: ')
    else:
        try:
            f = leiaFloat('Digite um número real: ')
        except:
            f = leiaFloat('Digite um número real: ')
        else:
            break
        
        break
        
print(f"\033[32mSucesso!\033[m")
print(f'O número inteiro que você digitou foi {n} e o número real foi {f:.2f}.')
