class Evento:
    def __init__(self, id, c, t):
        self.id = id
        self.custo = c
        self.periodo = t
        self.nextExec = 0
        self.executado = 0

    def oi(self):
        print("Evento: {2}, custo: {0}, periodo: {1}" .format(self.custo, self.periodo, self.id))

    def calc(self):
        return float(self.custo)/float(self.periodo)

    def getPeriodo(self):
        return float(self.periodo)

    def getNextExec(self):
        return float(self.nextExec)

    def getDeadline(self):
        return float(self.periodo) + float(self.nextExec)

    def stepEDF(self,step):
        self.executado += step
        print("ID: {0}, Tempo Executado: {1}, Custo {3} ,Deadline: {2}" .format(self.id, self.executado, self.getDeadline(),self.custo))
        if self.executado == float(self.custo):
            self.executado=0
            self.nextExec += float(self.periodo)
            print("Tarefa ",self.id," terminou de executar")
