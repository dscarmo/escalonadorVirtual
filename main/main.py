from RM import RM
from analiseTempoResposta import executeATR

rm = RM()
rm.debugInit()
rm.setPrioritiesRM()
rm.printList()
executeATR(rm.getLista())


#RM Things
#
#lista.printList()
#lista.executeRM()
