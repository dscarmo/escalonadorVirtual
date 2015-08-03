# coding=UTF-8
import math

result = 0

def tempoResposta(ci, hplist, i, ant_tr, next_tr):
    global result
    print("iteration: {0}".format(i))

    if ant_tr == next_tr:
        result = next_tr
        return next_tr
    else:
        if i == 1:
            ant_tr = ci
        else:
            ant_tr = next_tr

        next_tr = ci
        for e in hplist:
            divisao = float(ant_tr)/e.periodo
            ceil = math.ceil(divisao)*e.custo
            next_tr = next_tr + ceil
        i += 1
        tempoResposta(ci, hplist, i, ant_tr, next_tr)


def executeATR(listaEventos):
    #Executar tempo de resposta pra cada tarefa separada, se passar do deadline, retorna -1, se nao, retorna o TR
    hplist = []
    maxTr = 0
    global result

    for e in listaEventos:
        for ev in listaEventos:
            if ev.prioridadeRm > e.prioridadeRm:
                hplist.append(ev)

        print("Calculando tempo de resposta da tarefa: ")
        e.oi()
        tempoResposta(e.custo, hplist, 1.0, 1.0, 0.0)
        print(result)

        if result > e.periodo:
            print("Tempo de resposta passou o periodo, não e possivel executar o conjunto de tarefas fornecido.")
            return -1

        while len(hplist) > 0:
            hplist.pop()

        if result > maxTr:
            maxTr = result

    print("Conjunto de tarefas e escalonavel em RM, maior tempo de resposta: {0} " .format(maxTr))


