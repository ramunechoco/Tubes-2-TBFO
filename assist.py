left, right = 0, 1

def union(lst1, lst2):
    final_list = list(set().union(lst1, lst2))
    return final_list

def loadModel(modelPath):
	file = open(modelPath).read()
	T = (file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n",""))
	V = (file.split("Variables:\n")[1].split("Grammar:\n")[0].replace("Variables:\n","").replace("\n",""))
	G = (file.split("Grammar:\n")[1])

	return cleanAlphabet(T), cleanAlphabet(V), cleanProduction(G)

def cleanProduction(expression):
	result = []
	rawRulse = expression.replace('\n','').split(';')
	
	for rule in rawRulse:
		#Explode evry rule on "->" and make a couple
		leftSide = rule.split(' -> ')[0].replace(' ','')
		rightTerms = rule.split(' -> ')[1].split(' | ')
		for term in rightTerms:
			result.append( (leftSide, term.split(' ')) )
	return result

def cleanAlphabet(expression):
	return expression.replace('  ',' ').split(' ')

def seekAndDestroy(target, grammar):
	trash, ereased = [],[]
	for rule in grammar:
		if target in rule[right] and len(rule[right]) == 1:
			trash.append(rule[left])
		else:
			ereased.append(rule)
			
	return trash, ereased