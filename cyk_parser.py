import os.path
import argparse
import grammar_converter


left, right = 0, 1


sentence = ["lorem", "ipsum", "dolor", "sit", "amet"] #Belom fix, coba gini dulu
#dianggep grammar sudah didefinisikan
nTab = len(sentence)*(len(sentence)+1)/2 #bentuk tangga
table = [[] for i in range nTab]

def Parser(sentence):

    for i in range(nTab):
        for j in range(len(sentence)):
            if sentence[j] == grammar[right]:
                table[i] = 



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