from fuzzify import fuzzifyIPK,fuzzifyPOT,fuzzifyTAN,fuzzifyORG,fuzzifyPRE,viewFuzzified
from rules import rulesMin

# ipk = 4
# tan = 2
# pot = 1500000
# pre = 1
# org = 1

listIPK = []
listTAN = []
listPOT = []
listPRE = []
listORG = []


for i in fuzzifyIPK(ipk):
    listIPK.append(i)
for i in fuzzifyTAN(tan):
    listTAN.append(i)
for i in fuzzifyPOT(pot):
    listPOT.append(i)
for i in fuzzifyPRE(pre):
    listPRE.append(i)
for i in fuzzifyORG(org):
    listORG.append(i)

viewFuzzified(listIPK,listTAN,listPOT,listPRE,listORG)
# print "IPK : ",listIPK
# print "TAN : ",listTAN
# print "POT : ",listPOT
# print "PRE : ",listPRE
# print "ORG : ",listORG

rulesMin(listIPK,listTAN,listPOT,listPRE,listORG)
