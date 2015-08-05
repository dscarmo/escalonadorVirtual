# coding=UTF-8
from Evento import Evento
from someMath import lcm

class RM:

    def __init__(self):
        self.lTarefas = []
        self.jobBuffer = []
        self.time = 0
        self.quantosEventos = 0
        self.timeLimit = 0

    def getTarefas(self):
        return self.lTarefas

    def resetTimeBase(self):
        self.time = 0
        self.timeLimit = 0

    def clearList(self, lista):
         while len(lista) > 0:
            lista.pop()

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
            self.setPriority(self.lTarefas)
        except:
                print("Por favor, somente numeros.")
                self.clearList(self.lTarefas)
                self.inicializar()

    def debugInit(self):
        self.lTarefas.append(Evento(1, 2, 3))
        self.lTarefas.append(Evento(2, 3, 4))
        self.quantosEventos = 2
        print("Inicialização debug realizada.")
        self.setPriority(self.lTarefas)

    def printList(self, lista):
        for e in lista:
            e.oi()

    def setPriority(self, lista):
        print("Situação:")
        if len(lista) > 0:
            lista.sort(key=lambda evento: evento.periodo)
            p = len(lista)
            for e in lista:
                e.setPrioridadeRm(p)
                p -= 1
            self.printList(lista)
        else:
            print("Impossível setar prioridades de uma lista vazia.")
        print("")

    def orderByPriority(self, lista):
        print("Situação:")
        if len(lista) > 0:
            lista.sort(key=lambda evento: evento.periodo)
            self.printList(lista)
        else:
            print("Impossível setar prioridades de uma lista vazia.")
        print("")

    def fillBuffer(self):
        for e in self.lTarefas:
            if self.time == 0:
                self.jobBuffer.append(e)

            else:
                if self.time%e.periodo == 0:
                    for ev in self.jobBuffer:
                        if e.id == ev.id:
                            return 1
                    self.jobBuffer.append(e)

        return 0

    def errReset(self):
        self.resetTimeBase()
        self.clearList(self.jobBuffer)
        return 1

    def getExecutionTime(self, lista):
        numbers = []
        for e in self.lTarefas:
            numbers.append(e.periodo)
        self.timeLimit = lcm(numbers)
        print("Tempo de execução: {0}".format(self.timeLimit))


    def execute(self):
        self.getExecutionTime(self.lTarefas)

        #check who should be added to buffer
        while(self.time < self.timeLimit):
            if self.fillBuffer():
                print("Conjunto perdeu o deadline.")
                return self.errReset()

            print("Buffer checado, executando tarefa de maior prioridade.")
            self.orderByPriority(self.jobBuffer)

            if len(self.jobBuffer) == 0:
                print("Buffer vazio, processador em idle.")
                self.time += 1
                continue
            else:
                evento = self.jobBuffer[0]

            if evento.execute():
                self.jobBuffer.remove(evento)


            self.time += 1
            print("tempo: {0}".format(self.time))
        #end

        self.clearList(self.jobBuffer)
        return 0