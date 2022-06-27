print("-=" * 20)
print("Termos de uma PA")
print("-=" * 20)

n = int(input("\nPrimeiro termo: "))
r = int(input("Razão: "))

mais = 10
total = i = 0

while mais != 0:
    total += mais
    while i < mais:
        print(n, end='')
        print(", " if i < (mais - 1) else ".", end='')

        n += r
        i += 1
    mais = int(input("\nQuantos termos você quer mostrar a mais? "))
    i = 0

print(f"Programa finalizado com {total} termos mostrados.")