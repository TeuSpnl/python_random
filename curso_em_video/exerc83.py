exp = input("Insira uma expressão: ")

contFecha = contAbre = 0

for dig in exp:
    if dig == '(':
        contAbre += 1
    elif dig == ')':
        contFecha += 1
        
result = contAbre - contFecha

if result == 0:
    print("Sua expressão está válida.")
else:
    print("Sua expressão está inválida.")