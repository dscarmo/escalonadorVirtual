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
        print("Evento: {3}, custo: {0}, periodo: {1}, prioridade em RM: {2}" .format(self.custo,
                                                                                     self.periodo,
                                                                                     self.prioridadeRm,
                                                                                     self.id))

    def execute(self):
        self.executado += 1
        print("Evento de prioridade {0}  executando " .format(self.prioridadeRm))
        print("Tempo executado: {0} ".format(self.executado))
        if self.executado == self.custo:
            self.executado = 0
            print("Terminou de executar.")
            return 1
        elif self.executado > self.custo:
            print("Erro: evento alocado por mais tempo que o necessario")
            return 2
        else:
            return 0
