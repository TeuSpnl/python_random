from random import randint
from time import sleep

lista = []


def sorte():
    lista.clear()
    print("Sorteando 5 valores da lista: ", end='')
    for i in range(5):
        num = randint(0, 10)
        lista.append(num)

        print(num, end=' ', flush=True)
        sleep(.3)

    print("Pronto!")


def somaPar(lista):
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item

    print(f"A soma dos valores pares de {lista} é: {soma}.")


sorte()
somaPar(lista)
