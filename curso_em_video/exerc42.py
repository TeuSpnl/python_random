seg1 = float(input("Qual o primeiro segmento? "))
seg2 = float(input("Qual o segundo segmento? "))
seg3 = float(input("Qual o terceiro segmento? "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("Esses segmentos podem formar um triângulo", end= ' ')
    if seg1 == seg2 == seg3:
        print("Equilátero.")
    elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
        print("Isósceles.")
    else:
        print("Escaleno.")
else:
    print("Esses segmentos não podem formar um triângulo.")
