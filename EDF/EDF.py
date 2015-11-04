from Evento import Evento

class EDF:

    def __init__(self):
        self.lTarefas = []
        self.jobBuffer = []
        self.time = 0
        self.quantosEventos = 0
        self.timeLimit = 0

    def getTarefas(self):
        return self.lTarefas

    def inicializar(self):
        try:
            print("Inicializando...")
            self.quantosEventos = int(input("Quantos eventos vai adicionar?"))
            i = 1
            while i <= self.quantosEventos:
                print("Evento {0}:".format(i))
                c = input("Custo?")
                t = input("Periodo?")
                self.lTarefas.append(Evento(i, c, t))
                i += 1
        except:
                print("Por favor, somente numeros.")
                self.clearList(self.lTarefas)
                self.inicializar()
        self.printList(self.lTarefas)
        self.calcProc(self.lTarefas)
    def printList(self, lista):
        for e in lista:
            e.oi()

    def clearList(self, lista):
         while len(lista) > 0:
            lista.pop()

    def calcProc(self,lista):
        soma=0.0
        for e in lista:
            soma=soma+e.calc()
        print("Uso de Processador:",soma)
        if soma <= 1:
            print("Sistema Escalonavel")
        else:
            print("Sistema nao escalonavel")
            exit()