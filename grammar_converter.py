left, right = 0, 1

Terminals, Variables, result = [],[],[]

RULE_DICT = {}

def read_cfg(cfg_file):
    final_grammar = []
    with open(cfg_file) as cfg:
        terminal = cfg.readline().split()
        Terminals.extend(terminal)
        variable = cfg.readline().split()
        Variables.extend(variable)
        lines = cfg.readlines()
    leftright = [x.split("->") for x in lines]
    for i in range(len(leftright)):
        splitor = [y.split() for y in leftright[i]]
        final_grammar.append(splitor)
    return final_grammar

def isUnitary(rule, variables):
    if rule[left] in variables and rule[right][0] in variables and len(rule[right]) == 1:
        return True
    return False

def isSimple(rule):
    if len(rule[right]) == 1:
        return True
    return False

def START(grammar):
    Variables.append('S0')
    return [[['S0'], grammar[left][0]]] + grammar

def TERM(grammar):
    i = 1
    newGrammar = []
    valuestore = []
    variablestore = []
    for rule in grammar:
        if isSimple(rule):
            newGrammar.append(rule)
        else:
            for symbol in Terminals:                
                for index, value in enumerate(rule[right]):
                    if symbol == value and not symbol in valuestore:
                        valuestore.append(symbol)
                        newVar = 'S' + str(i)
                        variablestore.append(newVar)
                        Variables.append(newVar)
                        newGrammar.append([[newVar], [symbol]])
                        rule[right][index] = newVar
                        i += 1
                    elif symbol == value:
                        newVar = variablestore[valuestore.index(symbol)]
                        rule[right][index] = newVar
            newGrammar.append([rule[left],rule[right]])
    return newGrammar

def BIN(grammar):
    newGrammar = []
    for rule in grammar:
        rlength = len(rule[right])
        if rlength <= 2:
            newGrammar.append(rule)
        else:
            newVar = 'B1'
            Variables.append(newVar)
            newGrammar.append([rule[left],rule[right][0]]+[newVar+'1'])
            i = 1
            for i in range(1, rlength-2):
                var, var2 = newVar+str(i), newVar+str(i+1)
                Variables.append(var2)
                newGrammar.append([var, [rule[right][i], var2]])
            newGrammar.append([newVar+str(rlength-2), rule[right][rlength-2:rlength]]) 
    return newGrammar

grammar = read_cfg('grammar_placeholder.txt')
grammar = START(grammar)
grammar = TERM(grammar)
grammar = BIN(grammar)
print("Terminals:")
print(Terminals)
print("Variables:")
print(Variables)
print("Grammar:")
print(grammar)