def imprimir_contagem():
   # for i in range(21):
    #    print(i)

    contador = 0
    while(contador < 21):
        print(contador)
        contador = contador +1

imprimir_contagem()

def contagem_usuario():
    digito_user = int(input("Digite um numero: "))

    for i in range(digito_user + 1):
        print(i)

contagem_usuario()