import funcoes

def main_menu(lista):
    princ("Menu Principal", lista)
    
    ans = funcoes.leiaInt("Sua opção: ")
        
    while ans <= 0 or ans > len(lista):
        print("\033[31mErro!")
        print("Digite uma opção válida!\033[m")
        
        princ("Menu Principal", lista)
        ans = funcoes.leiaInt("Sua opção: ")
                
    return ans

def princ(msg, lista):
    funcoes.titulo(msg)
    
    for i, item in enumerate(lista):
        print(f"{i + 1}- \033[36m{item}\033[m")
        