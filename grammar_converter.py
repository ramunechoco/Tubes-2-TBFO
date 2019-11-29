import itertools 

left, right = 0, 1

def loadFile(filename):
    file = open(filename).read()
    T = (file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n",""))
    V = (file.split("Variables:\n")[1].split("Grammar:\n")[0].replace("Variables:\n","").replace("\n",""))
    G = (file.split("Grammar:\n")[1])
    T = T.replace('  ',' ').split(' ')
    V = V.replace('  ',' ').split(' ')
    return T, V, cleanGrammar(G)

def cleanGrammar(expression):
    result = []
    rawRulse = expression.replace('\n','').split(';')
    for rule in rawRulse:
        leftSide = rule.split(' -> ')[0].replace(' ','')
        rightTerms = rule.split(' -> ')[1].split(' | ')
        for term in rightTerms:
            result.append( (leftSide, term.split(' ')) )
    return result

def seekAndDestroy(target, grammar):
    trash, ereased = [],[]
    for rule in grammar:
        if target in rule[right] and len(rule[right]) == 1:
            trash.append(rule[left])
        else:
            ereased.append(rule)
            
    return trash, ereased

def rewrite(target, production):
    result = []
    positions = [i for i,x in enumerate(production[right]) if x == target]
    for i in range(len(positions)+1):
        for element in list(itertools.combinations(positions, i)):
            tadan = [production[right][i] for i in range(len(production[right])) if i not in element]
            if tadan != []:
                result.append((production[left], tadan))
    return result

def prettyForm(rules): # For debugging purpose only
    dictionary = {}
    for rule in rules:
        if rule[left] in dictionary:
            dictionary[rule[left]] += ' | '+' '.join(rule[right])
        else:
            dictionary[rule[left]] = ' '.join(rule[right])
    result = ""
    for key in dictionary:
        result += key+" -> "+dictionary[key]+"\n"
    return result

def START(grammar,variables):
    variables.append('S0')
    result = [('S0', [variables[0]])] + grammar
    return result

def TERM(grammar,variables,terminals):
    i = 1
    newGrammar = []
    valuestore = []
    variablestore = []
    for rule in grammar:
        if rule[left] in variables and rule[right][0] in terminals and len(rule[right]) == 1:
            newGrammar.append(rule)
        else:
            for symbol in terminals:             
                for index, value in enumerate(rule[right]):
                    if symbol == value and not symbol in valuestore:
                        valuestore.append(symbol)
                        newVar = 'TERM' + str(i)
                        variablestore.append(newVar)
                        variables.append(newVar)
                        newGrammar.append( (newVar, [symbol]) )
                        rule[right][index] = newVar
                        i += 1
                    elif symbol == value:
                        newVar = variablestore[valuestore.index(symbol)]
                        rule[right][index] = newVar
            newGrammar.append( (rule[left],rule[right]) )
    return newGrammar

def BIN(grammar,variables):
    newGrammar = []
    j = 1
    for rule in grammar:
        rlength = len(rule[right])
        if rlength <= 2:
            newGrammar.append(rule)
        else:
            newVar = 'BIN'+str(j)
            variables.append(newVar+'1')
            newGrammar.append( (rule[left], [rule[right][0]]+[newVar+'1']) )
            j = j + 1
            i = 1
            for i in range(1, rlength-2):
                var, var2 = newVar+str(i), newVar+str(i+1)
                variables.append(var2)
                newGrammar.append( (var, [rule[right][i], var2]) )
            newGrammar.append((newVar+str(rlength-2), rule[right][rlength-2:rlength]))
    return newGrammar

def DEL(grammar):
    newSet = []
    outlaws, grammar = seekAndDestroy(target='EPSILON', grammar=grammar)
    for outlaw in outlaws:
        for rule in grammar + [e for e in newSet if e not in grammar]:
            if outlaw in rule[right]:
                newSet = newSet + [e for e in rewrite(outlaw, rule) if e not in newSet]
    return newSet + ([grammar[i] for i in range(len(grammar)) 
                            if grammar[i] not in newSet])

def unit_repeat(grammar,variables):
    unitaries, result = [], []
    for rule in grammar:   
        if rule[left] in variables and rule[right][0] in variables and len(rule[right]) == 1:
            unitaries.append( (rule[left], rule[right][0]) )
        else:
            result.append(rule)
    for uni in unitaries:
        for rule in grammar:
            if uni[right]==rule[left] and uni[left]!=rule[left]:
                result.append( (uni[left],rule[right]) )
    return result

def UNIT(grammar,variables):
    i = 0
    result = unit_repeat(grammar,variables)
    tmp = unit_repeat(result,variables)
    while result != tmp and i < 1000:
        result = unit_repeat(tmp,variables)
        tmp = unit_repeat(result,variables)
        i+=1
    return result

def main(filetext):
    Terminals, Variables, Grammar = loadFile(filetext)
    Grammar = START(Grammar,Variables)
    Grammar = TERM(Grammar,Variables,Terminals)
    Grammar = BIN(Grammar,Variables)
    Grammar = DEL(Grammar)
    Grammar = UNIT(Grammar,Variables)
    return Grammar, Variables

grammar, variable = main('grammar_python.txt')
open('output.txt', 'w').write(prettyForm(grammar))