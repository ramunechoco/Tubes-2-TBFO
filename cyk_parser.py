import grammar_converter

left, right = 0, 1

def loadTXT(txtfile):
    result = []
    file = open(txtfile, 'r')
    while 1:
        char = file.read(1).replace(" ","space")
        if not char: break
        result.append(char)
    file.close()
    print(result)
    return result

'''
let the input be a string I consisting of n characters: a1 ... an.
let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
for each s = 1 to n
  for each unit production Rv → as
    set P[1,s,v] = true
for each l = 2 to n -- Length of span
  for each s = 1 to n-l+1 -- Start of span
    for each p = 1 to l-1 -- Partition of span
      for each production Ra  → Rb Rc
        if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
if P[n,1,1] is true then
  I is member of language
else
  I is not member of language
'''

def CYK():
    P = [[[False for k in range(nt+1)] for j in range(ns+1)] for i in range(ns+1)]
    for i in range(1, ns+1):
        for j in range(ng):
            if grammar[j][right][0] == sentence[i-1] and len(grammar[j][right]) == 1:
              #  print("sentence[", i-1, "]: ", sentence[i-1])
             #   print("grammar[", j, "][right][0]: ", grammar[j][right][0])
            #    print(grammar[j][right][0] == sentence[i-1])
                a = grammar[j][left]
           #     print("grammar[j][left]:", str(a))
                found = False
                k = 0
                while not found and k < nt:
          #          print("k:", str(k))
                    if variable[k] == a:
                        found = True
                    if not found:
                        k += 1
         #       print("k:", str(k))
        #        print("i:", str(i))
                P[1][i][k+1] = True
       #         print("P[0]" + "[" + str(i) + "][" + str(k+1) + "] = ", P[1][i][k+1]    )
    for i in range(2, ns+1):
      #  print("i: ", str(i))
        for j in range(1, ns-i+2):
            #print("j: ", str(j))
            for k in range(1, i):
                #print("k: ",k)
                for l in range(ng):
                    #print("l:",l)
                    if len(grammar[l][right]) == 2:
                        a = grammar[l][right][0]
                        found = False
                        m = 0
                        while not found and m < nt:
                            #print("m:", m)
                           # print("variable[", str(m), "] = ", variable[m])
                          #  print("a:",a)
                            if variable[m] == a:
                                found = True
                            if not found:
                                m += 1
                         #       print("m1:", m)
                        b = grammar[l][right][1]
                        #print("b:", b)
                        found = False
                        n = 0
                        while not found and n < nt:
                            if variable[n] == b:
                                found = True
                            if not found:
                                n += 1
                        c = grammar[l][left]
                        #print("c:",c)
                        found = False
                        o = 0
                        while not found and o < nt:
                            if variable[o] == c:
                                found = True
                            if not found:
                                o += 1
                        #print(m,n,o)
                        # Vo -> VmVn
                        if m < nt and n < nt and o < nt:
                            if P[k][j][m+1] and P[i-k][j+k][n+1]:
                                P[i][j][o+1] = True
    return P[ns][1][1]

sentence = loadTXT("input.txt")
grammar, variable = grammar_converter.main("grammar_python.txt")

nt = len(variable)
ng = len(grammar)
ns = len(sentence) 

if CYK():
    print("Accepted")
else:
    print("Syntax Error")
