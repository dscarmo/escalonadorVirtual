from Evento import Evento


class RM:

    stupidExecution = 1
    init = 0

    def __init__(self):
        self.lista = []
        self.timeBase = 0
        self.nextAction = 0
        self.nextEvent = 0
        self.nextTime = 0
        self.prioridadeAtual = 0
        self.eventoAtual = Evento(0, 0, 0)
        self.quantosEventos = 0


    def resetTimeBase(self):
        self.timeBase = 0

    def inicializar(self):
        print("Inicializando...")
        self.quantosEventos = input("Quantos eventos vai adicionar?")
        i = 1
        while i <= self.quantosEventos:
            print("Evento {0}:".format(i))
            c = input("Custo?")
            t = input("Periodo?")
            self.lista.append(Evento(i, c, t))
            i += 1

    def debugInit(self):
        self.lista.append(Evento(1, 2, 7))
        self.lista.append(Evento(2, 3, 6))
        self.lista.append(Evento(3, 2, 18))
        self.quantosEventos = 3

    def printList(self):
        for e in self.lista:
            e.oi()

    def getHigherPriority(self):
        hp = 0
        for e in self.lista:
            if e.prioridadeRm > hp:
                hp = e.prioridadeRm
        return hp

    def setPrioritiesRM(self):
        self.lista.sort(key=lambda evento: evento.periodo)
        p = len(self.lista)
        for e in self.lista:
            e.setPrioridadeRm(p)
            p -= 1

    def executeRM(self):

        #Lets just execute everything one after another?
       for i in range(0, self.quantosEventos):

            if (self.nextAction == RM.init):
                self.prioridadeAtual = self.getHigherPriority()
                self.nextAction = RM.stupidExecution


            for e in self.lista:
                if (e.prioridadeRm == self.prioridadeAtual):
                    self.eventoAtual = e

            self.eventoAtual.oi()

            self.nextTime = self.eventoAtual.custo - self.eventoAtual.executado + self.timeBase
            print("nextTime = {0}" .format(self.nextTime))
            timeOfExecution = self.nextTime - self.timeBase
            print("timeOfExecution = {0}" .format(timeOfExecution))

            self.eventoAtual.execute(timeOfExecution)

            self.prioridadeAtual -= 1

            self.timeBase += timeOfExecution
            print("timeBase = {0}" .format(self.timeBase))