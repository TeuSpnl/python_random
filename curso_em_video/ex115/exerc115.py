import menu, funcoes

while True:
    ans = menu.main_menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])

    if ans == 1:
        funcoes.op1()
    elif ans == 2:
        funcoes.op2()
    elif ans == 3:
        funcoes.op3()
        break