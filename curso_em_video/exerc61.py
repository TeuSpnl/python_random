print("-=" * 20)
print("Termos de uma PA")
print("-=" * 20)

n = int(input("\nPrimeiro termo: "))
r = int(input("Razão: "))

i = 1

while i < 11:
    print(n, end='')
    print(", " if i < 10 else ".", end='')
    
    n += r
    i += 1