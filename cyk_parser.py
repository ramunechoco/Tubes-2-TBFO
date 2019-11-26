import os.path
import argparse
import grammar_converter


left, right = 0, 1





def loadTXT(txtfile):
    file = open(txtfile).read()
    sentence = file.split()
    return sentence


def CYK():
    for i in range(ns):
        for j in range(ng):
            if grammar[j][right] == sentence[i]:
                P[0][i][j] = True
    for i in range(1, ns):
        for j in range(ns-i+1):
            for k in range(i-1):
                for l in range():
                    for m in range
                if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
                if P[k][j][]


'''
let the input be a string I consisting of n characters: a1 ... an.
let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
for each s = 1 to n
  for each unit production Rv → as
    set P[1,s,v] = true
for each l = 2 to n -- Length of span
  for each s = 1 to n-l+1 -- Start of span
    for each p = 1 to l-1 -- Partition of span
      for each production Ra  → Rb Rc
        if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
if P[n,1,1] is true then
  I is member of language
else
  I is not member of language
'''

sentence = loadTXT("input.txt")
grammar = grammar_converter.main("grammar_python.txt")
variable = grammar_converter.GetNonTerminals("grammar_python.txt")
nt = grammar_converter.NumNonTerminals("grammar_python.txt")
ng = len(grammar)
P = [[[False for k in range(nt)] for j in range(len(sentence))] for i in range(len(sentence))]
ns = len(sentence) # nsentence 

'''
def concatWords(sentence):
    global Neff
    newsentence = ["#" for i in range(Neff-1)]
    for i in range(len(newsentence)):
        newsentence[i] = sentence[i] + " " + sentence[i+1]
    return newsentence

def StrToTabEl(string):
    n = len(string)
    for i in range(1, n):
        string[:i] 


def CYK(sentence):
    correct = True
    i = 0
    while correct and i < len(sentence):
    #untuk baris pertama, isi table dengan e
        j = 0
        while correct and j < len(sentence):
        #baca sentence
            count = 0
            for k in range(len(grammar)):
                if sentence[j] == grammar[k][right]: # gini ga sih? maksudnya elemen ke k, yang kanan
                   table[0][i].append(grammar[k][left])
                   count += 1
            if count == 0:
                correct = False #kalau ada sentence yang tidak bisa dicari derivatornya
            j += 1
        i += 1

    while correct:
        #langkah selanjutnya adalah untuk barisan barisan berikutnya dalam table
        i = 1
        while i < len(sentence) and correct:
            #belom kelar :((((
            sentence = concatWords(sentence)
            # contoh: dari ["a", "b", "c", "d", "e", "f"] menjadi ["ab", "bc", "cd", "de", "ef"]
            sentence[i] = 



sentence = ["lorem", "ipsum", "dolor", "sit", "amet"] #Belom fix, coba gini dulu
Neff = len(sentence)
#dianggep grammar sudah didefinisikan
nTab = len(sentence)*(len(sentence)+1)/2 #bentuk tangga, ukuran pasti n(n+1)/2 dengan n panjang sentence
table = [[[] for j in range(nTab)] for i in range(nTab)] # buat matriks
'''