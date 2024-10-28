#!/usr/bin/python3
NcompDNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
attemptComp=NcompDNA.replace("A", "t")
secattemptComp=attemptComp.replace("T", "a")
thrattemptComp=secattemptComp.replace("G", "c")
CompDNA=thrattemptComp.replace("C", "g")
print("complementary dna: ", CompDNA)
print("original dna was: ", NcompDNA)



