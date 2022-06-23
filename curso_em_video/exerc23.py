from random import randint

num = randint(0, 9999)

# n = str(num)


uni = int(num / 1 % 10) # 9999 % 10 = 9
dez = int(num / 10 % 10) # 999 % 10 = 9 (lembrando que é int)
cem = int(num / 100 % 10) # 99 % 10 = 9
mil = int(num / 1000 % 10) # 9 % 10 = 9

uniEuPensei = num % 10 # 9
dezEuPensei = (num % 100 - uni) / 10 # (99 - 9) / 10 = 90 / 10 = 9
cemEuPensei = (num % 1000 - uni - dez * 10) / 100 # (999 - 9 - 90) / 10 = 900 / 10 = 9
milEuPensei = (num - cem * 100 - dez * 10 - uni) / 1000 # (9999 - 900 - 90 - 9) / 1000 = 9000 / 1000 = 9

print(
    f"Número: {num:.0f}\nMilhar: {mil:.0f}\nCentena: {cem:.0f}\nDezena: {dez:.0f}\nUnidade: {uni:.0f}")
