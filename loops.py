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

#exemplo for
    for i in range(digito_user + 1):
        print(i)

#exemplo while
   # contador = 0
   # while(contador <= digito_user):
   #     print(contador)
   #     contador = contador + 1

contagem_usuario()

def tabuada_de_dois():
    #Exemplo FOR
    for i in range(1, 11):
        soma = 2 + i
        print("2", "+" ,i, "=", soma)


    #Exemplo while
    contador = 1
    while(contador < 11):
        soma = 2 + contador
        print("2", "+" ,contador, "=", soma)
        contador = contador + 1    

tabuada_de_dois()