def leiaDinheiro(valor = " "):
    valor = input(valor).replace(',','.').strip()
    
    while valor.isalpha() or valor == '':
        print(f"\033[31mERRO! '{valor}' não é um preço válido\033[m")
        valor = input("Digite o valor: R$")
    
    return float(valor)