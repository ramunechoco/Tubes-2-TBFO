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
            print("sentence[", i, "]: ", sentence[i])
            print("grammar[", j, "][right][0]: ", grammar[j][right][0])
            print(grammar[j][right][0] == sentence[i])
            if grammar[j][right][0] == sentence[i]:
                a = grammar[j][left]
                found = False
                k = 0
                while not found and k < nt:
                    if variable[k] == a:
                        found = True
                    if not found:
                        k += 1
                print("k", str(k))
                P[0][i][k-1] = True
    for i in range(1, ns):
        print("i: ", str(i))
        for j in range(ns-i+1):
            print("j: ", str(j))
            for k in range(i-1):
                print(k)
                for l in range(ng):
                    print(l)
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
                        print(m,n,o)
                        # Vo -> VmVn
                        if P[k][j][m-1] and P[i-k][j+k][n-1]:
                            P[i][j][o-1] = True
    return P[ns-1][0][0]

sentence = loadTXT("newinput.txt")
grammar = grammar_converter.GetGrammar("input.txt")
variable = grammar_converter.GetNonTerminals("input.txt")

nt = len(variable)
ng = len(grammar)
ns = len(sentence) 

print(nt,ng,ns)

if CYK():
    print("Accepted")
else:
    print("Syntax Error")
