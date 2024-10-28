#!/usr/bin/python3

restrictP = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
GrSITE = "GAATTC"
rsloc = restrictP.find(GrSITE,0)
DNAlen = len(restrictP)
rSITE = "AATTC"
CUTloc = restrictP.find(rSITE,0)
FRAGlen = DNAlen - CUTloc
print("The restiction site appears at", rsloc, "in the sequence", DNAlen, "long")
print("the first fragment is", CUTloc, " nucleiotides long and the second fragment ", FRAGlen)
