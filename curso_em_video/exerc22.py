nome = input("Insira um nome completo: ").strip()

print(f"Maiúsculas: {nome.upper()}\nMinúsculas: {nome.lower()}")

print(f"Total de letras: {len(nome) - nome.count(' ')}")

print(f"O primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras.")