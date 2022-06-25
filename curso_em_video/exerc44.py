print("-=" * 20)
print("Lojas Guanabara")
print("-=" * 20)

valor = float(input("Digite o valor da compra: "))

print('''Formas de pagamento:
    [1] À Vista dinheiro/cheque (10%  desconto)
    [2] À Vista no cartão (5% desconto)
    [3] 2X no cartão
    [4] 3X ou mais no cartão (20% juros)''')
resp = int(input("Opção: "))

if resp == 1:
    total = valor - (valor * .1)
elif resp == 2:
    total = valor - (valor * .05)
elif resp == 3:
    total = valor
    print(f'Serão 2 parcelas de R${valor/2:.2f}')
elif resp ==  4:
    qtdParc = 0
    while (qtdParc < 1 or qtdParc > 12):
        qtdParc = int(input("Quantas parcelas? (máx: 12) "))
    
    total = valor + (valor * .2)
    valParc = total / qtdParc
    
    print(f'Serão {qtdParc} parcelas de R${valParc:.2f}')
    
else:
    print("Opção inválida e pagamento. Tente novamente.")
    total = 0
    
print(f"Valor da compra: R${valor:.2f}\nValor final: R${total:.2f}")