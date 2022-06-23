frase = input("Digite uma frase: ").strip()

print(f"A frase tem {frase.upper().count('A')}\nO primeiro A aparecem em {frase.upper().find('A')}\nO último A aparece em {frase.upper().rfind('A')}")