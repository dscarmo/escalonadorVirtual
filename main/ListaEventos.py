from Evento import Evento


class ListaEventos:

    def __init__(self):
        self.lista = []
        self.rmList = []

    def inicializar(self):
        print("Inicializando...")
        quantosEventos = input("Quantos eventos vai adicionar?")
        i = 1
        while i <= quantosEventos:
            print("Evento {0}:" .format(i))
            c = input("Custo?")
            t = input("Periodo?")
            self.lista.append(Evento(i, c, t))
            i += 1

    def debugInit(self):
        self.lista.append(Evento(1,2,7))
        self.lista.append(Evento(2,3,2))
        self.lista.append(Evento(3,2,18))

    def printList(self, whatlist):
        if whatlist == "origin":
            print("Lista de Eventos original")
            for e in self.lista:
                e.oi()
        elif whatlist == "rm":
            print("Lista com prioridades RM")
            for e in self.rmList:
                e.oi()

    def setPrioritiesRM(self):
        self.rmList = sorted(self.lista, key=lambda evento: evento.periodo)
        p = len(self.rmList)
        for e in self.rmList:
            e.prioridade = p
            p -= 1