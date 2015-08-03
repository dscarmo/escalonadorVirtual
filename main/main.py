# coding=UTF-8
from RM import RM
from analiseTempoResposta import executeATR

def menu():
    option = 0
    print("\nBem-vindo ao Simulador de Eventos. O que deseja fazer?")
    print("1- Criar conjunto de eventos.")
    print("2- Testar escalonabilidade via RM por análise de tempo de resposta.")
    print("3- Realizar execução em RM.")

    try:
        option = input()
    except:
        print("Por favor, somente numeros.")
        menu()

    if option < 0 or option > 3:
        print("Por favor, escolha uma opção válida.")
    elif option == 0:
        rm.debugInit()
    elif option == 1:
        rm.inicializar()
    elif option == 2:
        if len(rm.getTarefas()) == 0:
            print("Lista vazia, utilizando lista de debug para operação.")
            rm.debugInit()
        executeATR(rm.getTarefas())
    elif option == 3:
        if len(rm.getTarefas()) == 0:
            print("Lista vazia, utilizando lista de debug para operação.")
            rm.debugInit()
        pass

    menu()

rm = RM()
menu()
