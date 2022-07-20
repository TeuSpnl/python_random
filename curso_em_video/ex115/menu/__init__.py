import funcoes

def main_menu(lista):
    funcoes.titulo("Menu Principal")
    
    for i, item in enumerate(lista):
        print(f"{i + 1}- \033[36m{item}\033[m")
    
    ans = funcoes.leiaInt("Sua opção: ")
        
    while ans <= 0 or ans > len(lista):
        print("\033[31mErro!")
        print("Digite uma opção válida!\033[m")
        
        ans = funcoes.leiaInt("Sua opção: ")
                
    return ans
        