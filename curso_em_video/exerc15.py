dias = int(input("O carro foi alugado por quantos dias? "))
km = float(input("O carro rodou por quantos km? "))

v_dia = 60 * dias
v_km = .15 * km
v_final = v_km + v_dia

print(f"O valor a ser pago é R${v_final:.2f}")