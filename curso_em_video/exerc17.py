from math import hypot


co = float(input("Qual o comprimento do cateto oposto? "))
ca = float(input("Qual o comprimento do cateto adjacente? "))

hip = hypot(co, ca)

print(f"O valor da hipotenusa é {hip:.2f}")