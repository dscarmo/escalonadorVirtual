class Evento:

    def __init__(self, id, c, t):
        self.id = id
        self.custo = c
        self.periodo = t
        self.folga = 0
        self.prioridade = 0
        self.executado = 0

    def oi(self):
        print("Oi, eu sou um evento! Eu custo {0} tenho periodo {1} e tenho prioridade {2}" .format( self.custo,
                                                                                                     self.periodo,
                                                                                                     self.prioridade))

    def execute(self, time):
        self.executado += time