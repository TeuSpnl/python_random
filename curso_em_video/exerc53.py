frase = input("Digite a frase: ").strip()
palavras = frase.lower().split()
junto = ''.join(palavras)
inverso = junto[::-1]

# for letra in range(len(junto) -1, -1, -1):
#     inverso += junto[letra]

if inverso == junto:
    print(f'A frase {frase} é um palíndromo. O inverso (sem espaços) é: {inverso}.')
else:
    print(f'A frase {frase} não é um palíndromo.')