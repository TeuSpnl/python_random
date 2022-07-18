def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

        except ValueError:
            print("\033[31mErro!\033[m")
            print("Você tem que digitar um número inteiro!\n")

        except Exception as e:
            print("\033[31mErro!\033[m")
            print(f"Classe do erro: {e.__class__}")
        
        else:
            break

    return n

while True:
    try:
        n = leiaInt('Digite um número: ')
    except:
        n = leiaInt('Digite um número: ')
    else:
        break
        
print(f"\033[32mSucesso!\033[m")
print(f'Você acabou de digitar o número {n}.')
