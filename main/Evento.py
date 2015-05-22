class Evento:

    def __init__(self, c, t):
        self.c = c
        self.t = t

    def oi(self):
        print("Oi, eu sou um evento! Eu custo %d " % self.c)