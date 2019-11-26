import os.path
import argparse
import grammar_converter


left, right = 0, 1


def loadTXT(txtfile):
    file = open(modelPath).read()
    sentence = (file.split())

def concatWords(sentence):
    global Neff
    newsentence = ["#" for i in range(Neff-1)]
    for i in range(len(newsentence)):
        newsentence[i] = sentence[i] + " " + sentence[i+1]
    return newsentence

def CYK(sentence):
    correct = True
    i = 0
    while correct and i < len(sentence):
    #untuk baris pertama, isi table dengan e
        j = 0
        while correct and j < len(sentence):
            count = 0
            for k in range(len(grammar)):
                if sentence[j] == grammar[k][right]: # gini ga sih? maksudnya elemen ke k, yang kanan
                   table[i].append(grammar[k][left])
                   count += 1
            if count == 0:
                correct = False #kalau ada sentence yang tidak bisa dicari derivatornya
            j += 1
        i += 1

    while correct:
        #langkah selanjutnya adalah untuk barisan barisan berikutnya dalam table



sentence = ["lorem", "ipsum", "dolor", "sit", "amet"] #Belom fix, coba gini dulu
Neff = len(sentence)
#dianggep grammar sudah didefinisikan
nTab = len(sentence)*(len(sentence)+1)/2 #bentuk tangga, ukuran pasti n(n+1)/2 dengan n panjang sentence
table = [[] for i in range nTab]