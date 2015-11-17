from _json import make_encoder

from EDF import EDF

def menu():

    print("\nBem-vindo ao Simulador de Eventos. O que deseja fazer?")
    print("1- Criar conjunto de eventos.")
    print("2- Calcular uso de processador")
    print("3- Executar escalonador de edf")
    print("4- Sair do programa")

    option = int(input())
    if option < 0 or option > 4:
        print("Por favor, escolha uma opção válida.")
    elif option == 1:
        EDF.inicializar()
        menu()
    elif option == 2:
        EDF.call_calcProc()
        menu()
    elif option == 3:

        menu()
    elif option == 4:
        exit()
EDF = EDF()
menu()
