class Evento:

    def __init__(self, id, c, t):
        self.id = id
        self.custo = c
        self.periodo = t
        self.folga = 0
        self.prioridadeRm = 0
        self.executado = 0

    def setPrioridadeRm(self, p):
        self.prioridadeRm = p

    def oi(self):
        print("Oi, eu sou um evento! Eu custo {0} tenho periodo {1} e tenho prioridade em RM {2}" .format( self.custo,
                                                                                                     self.periodo,
                                                                                                     self.prioridadeRm))

    def execute(self):
        self.executado += 1
        print("Evento de prioridade {0}  executando, ja executou {1} " .format(self.prioridadeRm, self.executado))
        if (self.executado == self.custo):
            return 1
        else:
            return 0
