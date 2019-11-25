left, right = 0, 1

Terminals, Variables, result = [],[],[]

RULE_DICT = {}

def read_cfg(cfg_file):
    # reading cfg file.
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
    newRule = []
    valuestore = []
    variablestore = []
    for rule in grammar:
        if isSimple(rule):
            newRule.append(rule)
        else:
            for symbol in Terminals:                
                for index, value in enumerate(rule[right]):
                    if symbol == value and not symbol in valuestore:
                        valuestore.append(symbol)
                        newVar = 'S' + str(i)
                        variablestore.append(newVar)
                        Variables.append(newVar)
                        newRule.append([[newVar], [symbol]])
                        rule[right][index] = newVar
                        i += 1
                    elif symbol == value:
                        newVar = variablestore[valuestore.index(symbol)]
                        rule[right][index] = newVar
            newRule.append([rule[left],rule[right]])
    return newRule

grammar = read_cfg('grammar_placeholder.txt')
grammar = START(grammar)
grammar = TERM(grammar)
print("Terminals:")
print(Terminals)
print("Variables:")
print(Variables)
print("Grammar:")
print(grammar)