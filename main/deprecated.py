__author__ = 'diedre'
def executeRM(self):

        for i in range(0, self.quantosEventos):

            if self.nextAction == RM.init:
                self.prioridadeAtual = self.getHigherPriority()
                self.nextAction = RM.stupidExecution

            for e in self.lista:
                if e.prioridadeRm == self.prioridadeAtual:
                    self.eventoAtual = e

            self.eventoAtual.oi()

            self.nextTime = self.eventoAtual.custo - self.eventoAtual.executado + self.time
            print("nextTime = {0}".format(self.nextTime))

            timeofexecution = self.nextTime - self.time
            print("timeOfExecution = {0}".format(timeofexecution))

            self.eventoAtual.execute(timeofexecution)

            self.prioridadeAtual -= 1

            self.time += timeofexecution
            print("timeBase = {0}".format(self.time))