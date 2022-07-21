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

def op1():
    titulo("Lista de Pessoas Cadastradas")
    
    arquivo = open("ex115/Pessoas_cadastradas.txt", "a")
    
    for linha in arquivo.readline():
        print(linha)
    
    arquivo.close()
    
def op2():
    titulo("Cadastrar uma Nova Pessoa")

def op3():
    titulo("Finalizando...")