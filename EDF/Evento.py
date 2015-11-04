class Evento:
    def __init__(self, id, c, t):
        self.id = id
        self.custo = c
        self.periodo = t
        self.folga = 0
        self.executado = 0

    def oi(self):
        print("Evento: {2}, custo: {0}, periodo: {1}" .format(self.custo, self.periodo, self.id))

    def calc(self):
        return float(self.custo)/float(self.periodo)
