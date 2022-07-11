def calculo(width, length):
    area = width * length

    print(f"A área de um terreno {width:.2f} x {length:.2f} é {area:.2f}m².")


print("Controle de Terrenos")
print("-"*20)

w = float(input("Comprimento (m): "))
l = float(input("Largura (m): "))

calculo(w, l)
