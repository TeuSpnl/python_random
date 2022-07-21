from time import sleep
import timeit


lista = ["hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia", "hoje", "é", "um", "novo", "dia"]

# lista = ["hoje", "é", "um", "novo", "dia"]

inicio = timeit.default_timer()
for palavra in lista:
    print(palavra)
    sleep(.3)
fim = timeit.default_timer()

print(f"Tempo de execução: {fim - inicio}")