while True:
    n = int(input("\n\nVocê quer a tabuada de qual número? "))
    print("-" * 40)
    print(f'TABUADA DE {n}\n')
    
    if n < 0:
        break
    
    for i in range(1, 11):
        print(f'{n} X {i} = {n * i}')
    print("-" * 40)
    
print("Programa finalizado")