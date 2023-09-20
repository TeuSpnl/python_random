import pyautogui as ptgui
from time import sleep

# Abre o sistema e entra na tela de pedidos fechados
ptgui.hotkey('win', '1')
sleep(.25)
ptgui.hotkey('ctrl', 'r')
sleep(.25)

# Define a data de hoje
ptgui.click(114, 102)
sleep(.25)
ptgui.click(94, 256)
sleep(.25)

resp = "SIM"

# Início do loop
while resp.upper() == "SIM":
    # Define as variáveis
    jump = nf = ans = ""

    # Pede que o usuário informe quantos pedidos ele quer conferir
    while ans.isnumeric() == False and jump.isnumeric() == False:
        ans = ptgui.prompt("Quantos pedidos você quer conferir?", "Nº Pedido")
        jump = ptgui.prompt(
            "Vai pular quantos pedidos? – Cuidado com as devoluções totais", "Nº Pedido")
        nf = ptgui.confirm(text='Tem NF no meio?',
                           title='NF no meio', buttons=['Sim', 'Não'])
        
    # Clica no séculos para evitar problemas
    ptgui.click(50, 2)

    # Caso tenha NF no meio
    if nf.upper() == "SIM":
        cont = 0

        # Pula os pedidos que não serão conferidos
        for i in range(int(ans)):
            for i in range(int(jump) + cont):
                ptgui.press("down")

            sleep(.1)

            # Abre pedido
            ptgui.press("enter")
            sleep(.6)
            # Botão alterar
            ptgui.click(246, 790)
            sleep(.2)
            # Botão gravar
            ptgui.click(385, 790)
            sleep(1.3)
            # Fechar coprovante
            ptgui.press("esc")
            sleep(.25)
            # Volta para a tela de pedidos fechados
            ptgui.click(50, 50)
            sleep(.25)
            # Resseleciona a data de hoje
            ptgui.click(50, 104)

            ptgui.press("enter")

            cont += 1

    # Caso não tenha NF no meio
    else:
        for i in range(int(jump)):
            ptgui.press("down")

        for i in range(int(ans)):
            # Abre pedido
            ptgui.press("enter")
            sleep(.6)
            # Botão alterar
            ptgui.click(246, 790)
            sleep(.2)
            # Botão gravar
            ptgui.click(385, 790)
            sleep(1.3)
            # Fechar coprovante
            ptgui.press("esc")
            sleep(.25)
            # Volta para a tela de pedidos fechados
            ptgui.click(50, 50)
            sleep(.25)

            # Segue a lista de pedidos
            for i in range(4):
                ptgui.press("tab")

            ptgui.press("down")

    # Verifica se o usuário quer continuar
    resp = ptgui.confirm(text='Ver mais pedidos?',
                         title='Continuar?', buttons=['Sim', 'Não'])


# sleep(3)
# print(ptgui.position())
# sleep(3)
# print(ptgui.position())
