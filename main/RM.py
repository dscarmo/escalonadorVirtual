# coding=UTF-8
from Evento import Evento


class RM:
    stupidExecution = 1
    init = 0

    def __init__(self):
        self.lTarefas = []
        self.lJobs = []
        self.time = 0
        self.quantosEventos = 0

    def getTarefas(self):
        return self.lTarefas

    def resetTimeBase(self):
        self.time = 0

    def clearList(self):
         while len(self.lTarefas) > 0:
            self.lTarefas.pop()

    def inicializar(self):
        try:
            print("Inicializando...")
            self.quantosEventos = input("Quantos eventos vai adicionar?")
            i = 1
            while i <= self.quantosEventos:
                print("Evento {0}:".format(i))
                c = input("Custo?")
                t = input("Periodo?")
                self.lTarefas.append(Evento(i, c, t))
                i += 1
            self.setPrioritiesRM()
        except:
                print("Por favor, somente numeros.")
                self.clearList()
                self.inicializar()


    def debugInit(self):
        self.lTarefas.append(Evento(1, 2, 9))
        self.lTarefas.append(Evento(2, 2, 5))
        self.lTarefas.append(Evento(3, 1, 3))
        self.quantosEventos = 3
        print("Inicialização debug realizada.")
        self.setPrioritiesRM()

    def printList(self):
        for e in self.lTarefas:
            e.oi()

    def getHigherPriority(self):
        hp = 0
        for e in self.lTarefas:
            if e.prioridadeRm > hp:
                hp = e.prioridadeRm
        return hp

    def setPrioritiesRM(self):
        if len(self.lTarefas) > 0:
            self.lTarefas.sort(key=lambda evento: evento.periodo)
            p = len(self.lTarefas)
            for e in self.lTarefas:
                e.setPrioridadeRm(p)
                p -= 1
            self.printList()
        else:
            print("Impossível setar prioridades de uma lista vazia.")