from random import randint

ans = True
i = 1

num =  randint(1, 10)

resp = int(input("Pensei em um número entre 1 a 10, tente adivinhá-lo.\nVocê tem 3 chances: "))

if resp == num:
    ans = False
    print(f"Parabéns! Você acertou! O número que eu pensei era {num}!")
    
while ans and i < 3:
    resp = int(input("Errou! Tente de novo: "))
    
    i += i
    
if resp != num and i >= 3:
    print(f"Poxa! Não foi dessa vez. O número que eu pensei era {num}")