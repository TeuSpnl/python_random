v1 = int(input("Primeiro número: "))
v2 = int(input("Segundo número: "))

if (v1 > v2):
    print("O \033[1;31mprimeiro\033[m valor é maior.")
elif (v1 < v2):
    print("O \033[1;31msegundo\033[m valor é maior.")
else:
    print("Os valores são \033[1;31miguais\033[m.")
    