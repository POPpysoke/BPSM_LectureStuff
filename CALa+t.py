#!/usr/bin/python3
shortDNA  = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
residueA = "A"
residueT = "T"
shortDNA.count(residueA)
shortDNA.count(residueT)
Tcou = shortDNA.count(residueT)
Acou = shortDNA.count(residueA)
Acou + Tcou
TandAcout = Acou + Tcou
len (shortDNA)
TOTcou = len (shortDNA)
print("the number of T's and A's combined is: ", TandAcout)
TandAcout / TOTcou
TandA = TandAcout / TOTcou
TandA
perTandA =TandA * 100
print("the A and T dna % is: ", perTandA)
perGandC = 100 - perTandA
print("the G and C dna $ is: ", perGandC) 

