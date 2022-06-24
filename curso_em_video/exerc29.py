vel = int(input("Qual a velocidade atual do carro? "))

if vel > 80:
    multa = (vel - 80) * 7
    print(f"Velocidade acima da velocidade permitida!\nMulta: R${multa:.2f}")
    
print("\nTenha um bom dia e dirija com segurança.")