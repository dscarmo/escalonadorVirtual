# coding=UTF-8
from RM import RM
from analiseTempoResposta import executeATR


def checkInit():
    if len(rm.getTarefas()) == 0:
            print("Lista vazia, utilizando lista de debug para operação.")
            rm.debugInit()


def menu():
    option = 0
    print("\nBem-vindo ao Simulador de Eventos. O que deseja fazer?")
    print("1- Criar conjunto de eventos.")
    print("2- Testar escalonabilidade via RM por análise de tempo de resposta.")
    print("3- Realizar execução em RM.")

    try:
        option = int(input())
    except:
        print("Por favor, somente numeros.")
        menu()

    if option < 0 or option > 3:
        print("Por favor, escolha uma opção válida.")
    elif option == 1:
        rm.inicializar()
    elif option == 2:
        checkInit()
        executeATR(rm.getTarefas())
    elif option == 3:
        checkInit()
        if (rm.execute()):
            print("Conjunto perdeu o deadline usando RM")
        else:
            print("Conjunto executado com sucesso utilizado RM")
        pass

    menu()

rm = RM()
menu()
