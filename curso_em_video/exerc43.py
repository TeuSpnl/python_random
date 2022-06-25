peso = float(input("Qual o peso da pessoa? (Kg) "))
alt = float(input("Qual a altura da pessoa? (m) "))

imc = peso / (alt ** 2)

print('''=-=- Tabela -=-=
      – IMC abaixo de 18,5: Abaixo do Peso
      – Entre 18,5 e 25: Peso Ideal
      – 25 até 30: Sobrepeso
      – 30 até 40: Obesidade
      – Acima de 40: Obesidade Mórbida
''')

print(f'IMC: {imc:.2f}')

if imc < 18.5:
    print("A pessoa está \033[31mabaixo do peso\033[m!")
elif imc < 25:
    print("A pessoa está com o \033[32mpeso ideal\033[m!")
elif imc < 30:
    print("A pessoa está com \033[33msobrepeso\033[m.")
elif imc < 40:
    print("A pessoa está com \033[31mobesidade\033[m.")
else:
    print("\033[31mA pessoa está com obesidade mórbida!\033[m")