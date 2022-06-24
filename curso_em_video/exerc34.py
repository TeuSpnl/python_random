sal = float(input("Qual o salário do funcionário? "))

if sal > 1250:
    salFim = sal + (sal * .1)
else:
    salFim = sal + (sal * .15)
    
print(f'Quam ganhava {sal:.2f} vai ganhar {salFim:.2f}.')

