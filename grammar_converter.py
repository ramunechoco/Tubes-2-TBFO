left, right = 0, 1

Terminals, Variables, result = [],[],[]

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
    if rule[left] in Variables and rule[right][0] in Terminals and len(rule[right]) == 1:
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
                        newVar = 'TERM' + str(i)
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
            newVar = 'BIN'
            Variables.append(newVar)
            newGrammar.append([rule[left],rule[right][0]]+[newVar+'1'])
            i = 1
            for i in range(1, rlength-2):
                var, var2 = newVar+str(i), newVar+str(i+1)
                Variables.append(var2)
                newGrammar.append([var, [rule[right][i], var2]])
            newGrammar.append([[newVar+str(rlength-2)], rule[right][rlength-2:rlength]]) 
    return newGrammar

def unit_repeat(grammar):
    newGrammar = []
    unit_production = []
    for rule in grammar:
        if isUnitary(rule, Variables):
            unit_production.append([[rule[left]], [rule[right][0]]])
        else:
            newGrammar.append(rule)
        for uni in unit_production:
            for rule in grammar:
                if uni[right]==rule[left] and uni[left]!=rule[left]:
                    newGrammar.append([[uni[left]],[rule[right]]])
        return newGrammar

def UNIT(grammar):
    i = 0
    result = unit_repeat(grammar)
    tmp = unit_repeat(result)
    while result != tmp and i < 1000:
        result = unit_repeat(tmp)
        tmp = unit_repeat(result)
        i+=1
    return result


grammar = read_cfg('grammar_placeholder.txt')
grammar = START(grammar)
grammar = TERM(grammar)
grammar = BIN(grammar)
grammar = UNIT(grammar)
print("Terminals:")
print(Terminals)
print("Variables:")
print(Variables)
print("Grammar:")
print(grammar)