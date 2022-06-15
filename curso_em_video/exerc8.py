m = int(input("Insira um valor em metros: "))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print("Este valor é igual a:\n"
      f"{km}Km\n"
      f"{hm}Hm\n"
      f"{dam}Dam\n"
      f"{m}m\n"
      f"{dm}dm\n"
      f"{cm}cm\n"
      f"{mm}mm\n")