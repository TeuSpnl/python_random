def leiaInt(msg):
    while True:
        try:
            n = int(input(msg).strip())

        except ValueError:
            print("\033[31mErro!")
            print("Você tem que digitar um número inteiro!\033[m\n")

        except Exception as e:
            print("\033[31mErro!")
            print(f"Classe do erro: {e.__class__}\033[m\n")

        else:
            break

    return n


def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg).strip().replace(',','.'))

        except ValueError:
            print("\033[31mErro!")
            print("Você tem que digitar um número real!\033[m\n")

        except Exception as e:
            print("\033[31mErro!")
            print(f"Classe do erro: {e.__class__}\033[m\n")

        else:
            break

    return f
