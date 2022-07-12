def escreva(msg):
    tam = len(msg) + 4
    
    print(f"~" * tam)
    print(f"  {msg}")
    print(f"~" * tam)

msg1 = input("Digite uma mensagem: ")
msg2 = input("Digite mais uma mensagem: ")
msg3 = input("Digite outra mensagem: ")
escreva(msg1)
escreva(msg2)
escreva(msg3)
