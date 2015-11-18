from Evento import Evento


class EDF:

    def __init__(self):
        self.lTarefas = []
        self.jobBuffer = []
        self.time = 0.0
        self.quantosEventos = 0
        self.timeLimit = 0.0

    def getTarefas(self):
        return self.lTarefas

    def inicializar(self):
        try:
            print("Inicializando...")
            self.quantosEventos = int(input("Quantos eventos vai adicionar?"))
            i = 1
            while i <= self.quantosEventos:
                print("Evento {0}:".format(i))
                c = input("Custo?")
                t = input("Periodo?")
                self.lTarefas.append(Evento(i, c, t))
                i += 1
        except:
                print("Por favor, somente numeros.")
                self.clearList(self.lTarefas)
                self.inicializar()
        self.printList(self.lTarefas)

    def printList(self, lista):
        for e in lista:
            e.oi()

    def clearList(self, lista):
         while len(lista) > 0:
            lista.pop()

    def clearListaMenu(self):
        self.clearList(self.lTarefas)

    def calcProc(self,lista):
        soma=0.0
        for e in lista:
            soma=soma+e.calc()
        print("Uso de Processador:",soma)
        if soma <= 1:
            print("Sistema Escalonavel")
        else:
            print("Sistema nao escalonavel")

    def lista_vazia(self,lista):
        if  not self.lTarefas:
            print("Lista Vazia. Adicione Elementos na Lista")
            return True
        else:
            return False

    def call_calcProc(self):
        if not self.lista_vazia(self.lTarefas):
            self.calcProc(self.lTarefas)


    def org_list(self,lista):
        lista.sort(key=lambda evento: evento.getDeadline())


    def mmc(self,num1, num2):
        a = num1
        b = num2
        while b !=0:
            temp=b
            b=a % b
            a=temp
        return  (num1 * num2) / a


    def calc_execTime(self,lista):
        time=1
        for e in lista:
            a=e.getPeriodo()
            time=self.mmc(a,time)
        self.timeLimit=time

    def perda_DeadLine(self,a):
        if a.getDeadline() < self.time+1:
            return True

    def exec_esc(self,a,step):
         if self.perda_DeadLine(a):
             return False
         else:
            a.stepEDF(step)
            self.time=self.time + step

    def escalona_EDF(self):
        step=1
        self.calc_execTime(self.lTarefas)
        if not self.lista_vazia(self.lTarefas):
            #Entra no loop da EDF
            while (self.time < self.timeLimit+1):
                #Organiza a Lista por prioridade
                self.org_list(self.lTarefas)
                print("Time:",self.time)
                i=0
                a=self.lTarefas[i]
                #Verifica se a tarefa mais prioritaria pode exectuar
                if float(a.getNextExec()) <= self.time:
                    d=self.exec_esc(a,step)

                else:
                    #Procura por uma tarefa pronta para ser executada
                    while float(a.getNextExec()) > float(self.time) :
                        i=i+1
                        if i >= self.quantosEventos:
                            break
                        a=self.lTarefas[i]
                    #Caso não encontre incrementa o tempo
                    if i >= self.quantosEventos:
                        print("Sem Tarefa para executar")
                        self.time=self.time + step
                    #Case encontre executa o elemento pronto para executar
                    else :
                        d=self.exec_esc(a,step)
                #Caso alguma tarefa falhe no deadline retorna False
                if d == False:
                    return False
