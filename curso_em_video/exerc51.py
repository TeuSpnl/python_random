print("-=" * 20)
print("Termos de uma PA")
print("-=" * 20)

n = int(input("\nPrimeiro termo: "))
r = int(input("Razão: "))
dec = n + (10 - 1) * r

for i in range(n, dec + 1, r):
    print(i, end=', ')
