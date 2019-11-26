import os.path
import argparse
import grammar_converter

class Node:
    def __init__(self, symbol, child1, child2=None):
        self.symbol = symbol
        self.child1 = child1
        self.child2 = child2

    def __repr__(self):
        return self.symbol

class Parser:
	def __init__(self, grammar, sentence):
		self.parse_table = None
		self.prods = {}
		self.grammar = None
		self.__call__(sentence)