#!/usr/bin/python3
Gen_DNA = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = Gen_DNA[0:63]
exon2 = Gen_DNA[90:]
intron = Gen_DNA[63:90]
CombEXON = exon1 + exon2
print( "the coded sequence is", len(CombEXON), "Nucleotides long")
CombLen = len(CombEXON)
print("the coding sequence is", CombEXON)
Genlen = len(Gen_DNA)
perExon= ((CombLen / Genlen)*100)
print("of the entire genomic dna, coding sequences make up", perExon, "percent")
ReVin = intron.replace("A", "a").replace("T", "t").replace("G", "g").replace("C", "c")
print("#exon-intron-exon \n",  exon1 + ReVin + exon2, "\n", Gen_DNA)




