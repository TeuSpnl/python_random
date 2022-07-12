from random import randint
from time import sleep

lista = []


def maior(lisst):
    max = 0

    print(f"\n{'-='*20}")
    print("Analisando os valores passados...")
    sleep(.5)

    for j, item in enumerate(lisst):
        print(item, end=' ', flush=True)
        sleep(.3)

        if j == 0:
            max = item
        elif item > max:
            max = item

    print(f"\nForam gerados {len(lisst)} valores.")
    print(f"O maior valor é {max}.")


for i in range(5):
    lista.clear()

    n = randint(0, 10)
    for j in range(n):
        num = randint(0, 10)

        lista.append(num)

    maior(lista)
