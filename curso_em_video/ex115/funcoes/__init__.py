def titulo(titulo):
    print('-' * 40)
    print(f"{titulo:^40}")
    print('-' * 40)


def quest(quest):
    print('-' * 40)
    resp = input(f"{quest}").strip()
    print('-' * 40)

    return resp


def leiaInt(msg):
    while True:
        try:
            n = int(quest("\033[33mSua opção: \033[m"))

        except ValueError:
            print("\033[31mErro!")
            print("Você tem que digitar um número inteiro!\033[m")

        except KeyboardInterrupt:
            print("\033[31mErro!")
            print("Entrada interrompida pelo usuário.\033[m")
            return 0

        except Exception as e:
            print("\033[31mErro!")
            print(f"Classe do erro: {e.__class__}\033[m")

        else:
            break

    return n


def create_doc():
    try:
        arquivo = open("ex115/Pessoas_cadastradas.txt", "wt+")
    except (FileNotFoundError):
        arquivo = open("ex115/Pessoas_cadastradas.txt", "a")
        arquivo = open("ex115/Pessoas_cadastradas.txt", "wt+")
    except Exception as e:
        print(f"Erro classe {e.__class__}.")

    return arquivo


def op1():
    """    Leitura do arquivo    """
    try:
        arq = open("ex115/Pessoas_cadastradas.txt", "rt")
    except (FileNotFoundError):
        arq = create_doc()
        arq = open("ex115/Pessoas_cadastradas.txt", "rt")
    except Exception as e:
        print(f"Erro classe {e.__class__}.")

    titulo("Lista de Pessoas Cadastradas")

    try:
        for linha in arq:
            pessoa = linha.split(';')
            pessoa[1] = pessoa[1].replace('\n', '')
            print(f"{pessoa[0]:<40}{pessoa[1]:>} anos")
    except Exception as e:
        print(f"Erro classe {e.__class__}")

    arq.close()


def op2(nome, idade):
    """    Cadastro de pessoas    """
    titulo("Cadastrar uma Nova Pessoa")

    try:
        arq = open("ex115/Pessoas_cadastradas.txt", "at")
    except (FileNotFoundError):
        arq = create_doc()
        arq = open("ex115/Pessoas_cadastradas.txt", "at")
    except Exception as e:
        print(f"Erro classe {e.__class__}.")
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except Exception as e:
            print(f"Erro classe {e.__class__}.")

    arq.close()


def op3():
    titulo("Finalizando...")
