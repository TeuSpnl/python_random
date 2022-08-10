import menu, funcoes

while True:
    ans = menu.main_menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])

    if ans == 1:
        funcoes.op1()
    elif ans == 2:
        nome = input("Insira o nome da pessoa: ").title()
        idade = int(input(f"Insira a idade de {nome}: "))
        
        funcoes.op2(nome, idade)
    elif ans == 3:
        funcoes.op3()
        break