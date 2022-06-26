resp = 0

n1 = int(input("Insira um número inteiro: "))
n2 = int(input("Insira outro número inteiro: "))

while resp !=5:
    print("-=" * 20)
    print("""Escolha a opção do que você quer fazer:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair""")
    print("-=" * 20)
    
    resp = int(input())
    
    if resp == 1:
        print(f"{n1} + {n2} = {n1 + n2}")
        
    elif resp == 2:
        print(f"{n1} * {n2} = {n1 * n2}")
        
    elif resp == 3:
        if n1 > n2:
            print(f"O maior número é {n1}")
        elif n1 < n2:
            print(f"O maior número é {n2}")
        else:
            print("Eles são números iguais")
            
    elif resp == 4:
        n1 = int(input("Insira um número inteiro: "))
        n2 = int(input("Insira outro número inteiro: "))

    elif resp == 5:
        print("Goo bai!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")