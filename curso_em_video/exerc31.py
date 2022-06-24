dist = int(input("Qual a distância, em km, da viagem? "))

if dist <= 200:
    valor = dist * .5
else:
    valor = dist * .45
    
print(f"O valor da passagem é R${valor:.2f}")