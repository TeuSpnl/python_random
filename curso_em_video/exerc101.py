from datetime import date


def voto(nasc):
    anoAtu = date.today().year
    idade = anoAtu - nasc

    if idade >= 18 and idade < 60:
        return print(f"{idade} anos: Voto \033[31mObrigatório\033[m.")
    elif idade < 18 or idade >= 60:
        return print(f"{idade} anos: Voto \033[33mOpcional\033[m.")
    else:
        return print(f"{idade} anos: \033[32mNão vota\033[m.")


print('-'*20)
anoNasc = int(input("Em que ano você nasceu? "))

print(voto(anoNasc))
