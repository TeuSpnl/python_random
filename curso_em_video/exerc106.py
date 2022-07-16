from time import sleep

c = (
    '\033[m',  # 0 - Sem cor
    '\033[30;41m',  # 1 - Fundo vermelho, letra preta
    '\033[30;42m',  # 2 - Fundo verde, letra preta
    '\033[30;43m',  # 3 - Fundo amarelo, letra preta
    '\033[30;46m',  # 4 - Fundo azul, letra preta
    '\033[30;45m',  # 5 - Fundo roxo, letra preta
    '\033[30;46m',  # 6 - Fundo ciano, letra preta
    '\033[30;107m',  # 7 - Fundo Branco, letra preta
)


def help2(funcao):
    msg_color(f"Acessando o manual de comando do '{funcao}'", 4)

    sleep(.5)

    print(c[7])
    help(funcao)
    print(c[0])

    sleep(.5)


def msg_color(msg, color=0):
    print(c[color])
    print("~" * (len(msg) + 4))
    print(f"  {msg}")
    print("~" * (len(msg) + 4))
    print(c[0])


while True:
    msg_color("Sistema de ajuda PyHELP", 2)

    resp = input("Função ou Biblioteca (fim finaliza) > ")

    if resp.lower() == 'fim':
        break

    help2(resp)

msg_color('Programa finalizado', 1)
