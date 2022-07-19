def main_menu():
    print('-' * 30)
    print(f"{'Menu Principal':^30}")
    print('-' * 30)
    
    print('''
1- \033[36mVer pessoas cadastradas\033[m
2- \033[36mCadastrar nova pessoa\033[m
3- \033[36mSair do Sistema\033[m
            ''')
    
    
    while True:
        try:
            print('-' * 30)
            ans = int(input("\033[33mSua opção: \033[m"))
            print('-' * 30)
            
            while ans <= 0 or ans > 3:
                print("\033[31mErro!\033[m")
                print("Digite uma opção válida!")
                ans = int(input("\033[33mSua opção: \033[m"))
                
        except (ValueError, TypeError):
            print("\033[31mErro!\033[m")
            print("Você tem que digitar um número inteiro")
            
        except Exception as e:
            print("\033[31mErro!\033[m")
            print(f"Classe do erro: {e.__class__}")
            
        else:
            break
        
    return ans
        