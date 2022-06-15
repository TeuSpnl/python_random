wid = float(input("Largura da parede: "))
hei = float(input("Altura da parede: "))

area = wid * hei

qtd_tinta = area / 2

print(f"A altura da parede é {hei:.2f}m, a largura é {wid:.2f}m e a área é {area:.2f}m².\n"
      f"A quantidade de balde(s) de tinta necessária é {qtd_tinta:.1f}")
