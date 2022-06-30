from multiprocessing.pool import IMapIterator


list = []
par = []
impar = []

while True:
    n = int(input("Insira um valor: "))
    list.append(n)
    
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    resp = ' '

    while resp not in "SN":
        resp = input("Você quer continuar? [S/N] ").upper().strip()[0]

    if resp == 'N':
        break
    
print(f'\n{"-="*30}')
print(f"Você digitou os valores: {list}.\nOs pares são: {par}\nOs ímpares são: {impar}")
