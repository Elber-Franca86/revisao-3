def imprimir_nomes():
    nomes = ["João", "Maria", "Fulano", "Ciclano"]

    print("1 -", nomes[0])
    print("2 -", nomes[1])
    print("3 -", nomes[2])
    print("4 -", nomes[3])

imprimir_nomes()


def primeiro_ultimo():
    nomes = ["João", "Maria", "Fulano", "Beltrano"]

    print("1 -", nomes[0])
    print("4 -", nomes[3])

primeiro_ultimo()


def segundo_terceiro():
    nomes = ["Carlos", "Jorge", "Isabel", "Maria"]

    print("2 -", nomes[1])
    print("3 -", nomes[2])

segundo_terceiro()

def substituir_alimentos():
  
  alimentos = ["Macarrão", "Pepino", "Batata"]

  for i in range(3):
     alimento = input("Digite o nome do alimento: ")
     alimentos[i] = alimento

     print("Nova lista de alimentos:")

  for alimento in alimentos:

     print(alimento)

substituir_alimentos() 