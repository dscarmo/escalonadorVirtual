from Evento import Evento


class RM:

    release = 2
    receive = 1

    def __init__(self):
        self.lista = []
        self.timeBase = 0
        self.nextAction = 0
        self.nextEvent = 0
        self.nextTime = 0

    def resetTimeBase(self):
        self.timeBase = 0

    def inicializar(self):
        print("Inicializando...")
        quantosEventos = input("Quantos eventos vai adicionar?")
        i = 1
        while i <= quantosEventos:
            print("Evento {0}:".format(i))
            c = input("Custo?")
            t = input("Periodo?")
            self.lista.append(Evento(i, c, t))
            i += 1

    def debugInit(self):
        self.lista.append(Evento(1, 2, 7))
        self.lista.append(Evento(2, 3, 2))
        self.lista.append(Evento(3, 2, 18))

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
        #Debug execution
        prioridadeAtual = self.getHigherPriority()
        eventAtual = Evento(0, 0, 0)
        for e in self.lista:
            if (e.prioridadeRm == prioridadeAtual):
                eventAtual = e
        eventAtual.oi()
        eventAtual.execute()

        #Actual execution
        #   Execution checks: what time to stop to do things, wich event to mess, what to do in next action