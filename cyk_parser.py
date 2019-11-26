import grammar_converter

left, right = 0, 1

def loadTXT(txtfile):
    file = open(txtfile).read()
    sentence = file.split()
    return sentence


def CYK():
    P = [[[False for k in range(nt)] for j in range(ns)] for i in range(ns)]
    for i in range(ns):
        for j in range(ng):
            if grammar[j][right] == sentence[i]:
                P[0][i][j] = True
    for i in range(1, ns):
        for j in range(ns-i+1):
            for k in range(i-1):
                for l in range(ng):
                    if len(grammar[l][right]) == 2:
                        a = grammar[l][right][0]
                        found = False
                        m = 0
                        while not found and m < nt:
                            if variable[m] == a:
                                found = True
                            if not found:
                                m += 1
                        b = grammar[l][right][1]
                        found = False
                        n = 0
                        while not found and n < nt:
                            if variable[n] == b:
                                found = True
                            if not found:
                                n += 1
                        c = grammar[l][left]
                        found = False
                        o = 0
                        while not found and o < nt:
                            if variable[o] == c:
                                found = True
                            if not found:
                                o += 1

                        if P[k][j][m] and P[i-k][j+k][n]:
                            P[i][j][o] = True
    return P[0][0][ns]

sentence = loadTXT("input.txt")
grammar = grammar_converter.GetGrammar("grammar_python.txt")
variable = grammar_converter.GetNonTerminals("grammar_python.txt")

nt = len(variable)
ng = len(grammar)
ns = len(sentence) 

if CYK():
    print("Accepted")
else:
    print("Syntax Error")
