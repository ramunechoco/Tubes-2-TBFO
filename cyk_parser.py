import os.path
import argparse
import grammar_converter


left, right = 0, 1


sentence = ["lorem", "ipsum", "dolor", "sit", "amet"] #Belom fix, coba gini dulu
#dianggep grammar sudah didefinisikan
nTab = len(sentence)*(len(sentence)+1)/2 #bentuk tangga, ukuran pasti n(n+1)/2 dengan n panjang sentence
table = [[] for i in range nTab]

def Parser(sentence):
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

    if correct:
        #langkah selanjutnya adalah untuk barisan barisan berikutnya 



'''
class Node:
    def __init__(self, symbol, child1, child2=None):
        self.symbol = symbol
        self.child1 = child1
        self.child2 = child2

    def __repr__(self):
        return self.symbol
'''

'''
class Parser:
	def __init__(self, grammar, sentence):
		self.parse_table = None
		self.prods = {}
		self.grammar = None
		self.__call__(sentence)
    def start()
'''