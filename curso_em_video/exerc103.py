def infos(nome = '<desconhecido>', gols = 0):
    """
    Recebe o nome do jogador e o número de gols e printa as informações recebidas na tela.
    Se nenhuma informação for recebida, a função printa o '<desconhecido>' como nome e '0'
    como qauntidade de gols.
    
    :param nome = '<desconhecido>': O nome do jogador
    :param gols = 0: A quantidade de gols feitos
    """
    
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

nome = input("Nome do Jogador: ")

gols = input("Número de gols: ")
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    infos(gols = gols)
else:
    infos(nome, gols)
    