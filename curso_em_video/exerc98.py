from time import sleep


def contador(inicio, fim, passo):
    
    print('=-'*20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    sleep(.8)
    
    if fim < inicio:
        passo *= -1
    
    if fim <= 0:
        fim -= 1
    else:
        fim += 1
    
    for i in range(inicio, fim, passo):
        print(i, end=' ')
        sleep(0.2)
        
    print("FIM!")
    sleep(0.8)

contador(1, 10, 1)
contador(10, 0, 2)

print('=-'*20)

print("Agora é sua vez!")
inicio = int(input(f'{"Início: ":9}'))
fim = int(input(f'{"Fim: ":9}'))
passo = int(input(f'{"Passo: ":9}'))

contador(inicio, fim, passo)
