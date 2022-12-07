import os

lista_meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
               'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

vezes = int(input("Quantidade de anos: "))
ano = int(input("Ano inicial: "))

for k in range(vezes):
    # Cria a pasta do ano, caso não exista
    try:
        os.mkdir(f'./{ano}')
    except FileExistsError:
        print("Pasta do ano já existe. Seguindo...")
    except Exception as e:
        print(e.__class__)

    for i, mes in enumerate(lista_meses):
        # Cria as pastas dos meses que ainda não têm pasta
        try:
            os.mkdir(f'./{ano}/{i + 1}. {mes}')
        except FileExistsError:
            print("Pasta do mês já existe. Seguindo...")
        except Exception as e:
            print(e.__class__)

        # Cria as pastas dos dias
        if i < 8:
            if ((i + 1) % 2 == 0):  # Caso o mês tenha < 31 dias
                if (i == 1):  # Caso o mês seja fevereiro
                    # Caso o ano seja bissexto
                    if ((ano % 4 == 0 or ano % 400 == 0) and ano % 100 != 0):
                        for j in range(29):
                            try:
                                os.mkdir(f'./{ano}/{i + 1}. {mes}/{ano}-{(i + 1):02d}-{(j + 1):02d}')
                            except FileExistsError:
                                print("Pasta do dia já existe. Seguindo...")
                            except Exception as e:
                                print(e.__class__)

                    else:  # Caso o ano não seja bissexto
                        for j in range(28):
                            try:
                                os.mkdir(f'./{ano}/{i + 1}. {mes}/{ano}-{(i + 1):02d}-{(j + 1):02d}')
                            except FileExistsError:
                                print("Pasta do dia já existe. Seguindo...")
                            except Exception as e:
                                print(e.__class__)

                else:  # Caso não seja fevereiro
                    for j in range(30):
                        try:
                            os.mkdir(f'./{ano}/{i + 1}. {mes}/{ano}-{(i + 1):02d}-{(j + 1):02d}')
                        except FileExistsError:
                            print("Pasta do dia já existe. Seguindo...")
                        except Exception as e:
                            print(e.__class__)

            else:  # Caso o mês tenha 31 dias
                for j in range(31):
                    try:
                        os.mkdir(f'./{ano}/{i + 1}. {mes}/{ano}-{(i + 1):02d}-{(j + 1):02d}')
                    except FileExistsError:
                        print("Pasta do dia já existe. Seguindo...")
                    except Exception as e:
                        print(e.__class__)
        else:
            if ((i + 1) % 2 == 0):  # Caso o mês tenha < 30 dias
                for j in range(31):
                    try:
                        os.mkdir(f'./{ano}/{i + 1}. {mes}/{ano}-{(i + 1):02d}-{(j + 1):02d}')
                    except FileExistsError:
                        print("Pasta do dia já existe. Seguindo...")
                    except Exception as e:
                        print(e.__class__)

            else:  # Caso o mês tenha 31 dias
                for j in range(30):
                    try:
                        os.mkdir(f'./{ano}/{i + 1}. {mes}/{ano}-{(i + 1):02d}-{(j + 1):02d}')
                    except FileExistsError:
                        print("Pasta do dia já existe. Seguindo...")
                    except Exception as e:
                        print(e.__class__)

    ano += 1
