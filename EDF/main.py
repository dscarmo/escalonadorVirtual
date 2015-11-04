from EDF import EDF

def menu():

    print("\nBem-vindo ao Simulador de Eventos. O que deseja fazer?")
    print("1- Criar conjunto de eventos.")
    print("2- Calcular uso de processador")
    print("3- Executar escalonador de edf")

    option = int(input())
    if option < 0 or option > 3:
        print("Por favor, escolha uma opção válida.")
    elif option == 1:
        EDF.inicializar()

EDF = EDF()
menu()
