import grammar_converter

left, right = 0, 1

def loadTXT(txtfile):
    file = open(txtfile).read()
    sentence = file.split()
    return sentence

def CYK():
    P = [[[False for k in range(nt+1)] for j in range(ns+1)] for i in range(ns+1)]
    for i in range(1, ns+1):
        for j in range(ng):
            
            if grammar[j][right][0] == sentence[i-1] and len(grammar[j][right]) == 1:
                print(sentence[i-1])
                print("pass if")
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
                print("is true")
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

                            #print("passed")
                            #print(P[k][j][m+1])
                            #print(P[i-k][j+k][n+1])
                            if P[k][j][m+1] and P[i-k][j+k][n+1]:
                             #   print("passed again")
                                P[i][j][o+1] = True
    return P[ns][1][1]

sentence = loadTXT("input.txt")
grammar, variable = grammar_converter.main("grammar_python.txt")

nt = len(variable)
ng = len(grammar)
ns = len(sentence) 

print(sentence)
print("\n\n")
print(variable)
print(nt,ng,ns)

if CYK():
    print("Accepted")
else:
    print("Syntax Error")