num = int(input("Digite um número inteiro: "))
resp = 50
while resp != 0:
    print('''\nEscolha uma das bases para conversão:\n
        [1] converter para \033[1;31mbinário\033[m\n
        [2] converter para \033[1;31moctal\033[m\n
        [3] converter para \033[1;31mhexadecimal\033[m\n
        [0] sair''')
    resp = int(input())
    
    while resp != 1 and resp != 2 and resp != 3 and resp != 0:
        print('''\nEscolha uma das bases para conversão:\n
            [1] converter para \033[1;31mbinário\033[m\n
            [2] converter para \033[1;31moctal\033[m\n
            [3] converter para \033[1;31mhexadecimal\033[m\n
            [0] sair''')
        resp = int(input())

    if resp == 1:
        print(f"{num} convertido para \033[;31mbinário\033[m é: \033[1;32m{bin(num)[2:]}\033[m.")
    elif resp == 2:
        print(f"{num} convertido para \033[;31moctal\033[m é: \033[1;32m{oct(num)[2:]}\033[m.")
    elif resp == 3:
        print(f"{num} convertido para \033[;31mhexadecimal\033[m é: \033[1;32m{hex(num)[2:]}\033[m.")

print("\n")
print("-=" * 20)
print("Obrigado por usar nosso programa!")