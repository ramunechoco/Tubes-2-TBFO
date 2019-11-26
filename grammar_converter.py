import assist

left, right = 0, 1

Terminals, Variables, Grammar = [],[],[]

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
    return [('S0', [Variables[0]])] + grammar

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
                        newGrammar.append([newVar, [symbol]])
                        rule[right][index] = newVar
                        i += 1
                    elif symbol == value:
                        newVar = variablestore[valuestore.index(symbol)]
                        rule[right][index] = newVar
            newGrammar.append([rule[left],rule[right]])
    return newGrammar

def BIN(grammar):
    newGrammar = []
    j = 1
    for rule in grammar:
        rlength = len(rule[right])
        if rlength <= 2:
            newGrammar.append(rule)
        else:
            newVar = 'BIN'
            Variables.append(newVar+str(j))
            newGrammar.append( (rule[left], [rule[right][0]]+[newVar+str(j)]) )
            j = j + 1
            i = 1
            for i in range(1, rlength-2):
                var, var2 = newVar+str(i), newVar+str(i+1)
                Variables.append(var2)
                result.append( (var, [rule[right][i], var2]) )
            newGrammar.append((newVar+str(rlength-2), rule[right][rlength-2:rlength]))
    return newGrammar

def DEL(grammar):
    newSet = []
    outlaws, grammar = assist.seekAndDestroy(target='epsilon', grammar=grammar)
    for outlaw in outlaws:
        for rule in grammar + [e for e in newSet if e not in grammar]:
            if outlaw in rule[right]:
                newSet = newSet + [e for e in  assist.rewrite(outlaw, grammar) if e not in newSet]
    return newSet + ([grammar[i] for i in range(len(grammar)) 
                            if grammar[i] not in newSet])


def unit_repeat(grammar):
    newGrammar = []
    unit_production = []
    for rule in grammar:
        if isUnitary(rule, Variables):
            unit_production.append((rule[left], rule[right][0]))
        else:
            newGrammar.append(rule)
        for uni in unit_production:
            for rule in grammar:
                if uni[right]==rule[left] and uni[left]!=rule[left]:
                    newGrammar.append((uni[left],rule[right]))
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

if __name__ == '__main__':
    modelPath = 'grammar_placeholder.txt'
    
    Terminals, Variables, Grammar = assist.loadModel(modelPath)

    Grammar = START(Grammar)
    Grammar = TERM(Grammar)
    Grammar = BIN(Grammar)
    Grammar = DEL(Grammar)
    print( Terminals )
    print( Variables )
    print( Grammar )
    print( len(Grammar) )