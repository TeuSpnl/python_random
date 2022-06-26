for i in range(5):
    peso = float(input(f"Qual o peso da {i + 1}ª pessoa? (Kg) "))
    
    if i == 0:
        menor = peso
        maior = peso
    
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            
print(f"O maior peso é {maior}.\nO menor peso é {menor}.")