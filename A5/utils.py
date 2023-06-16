def mySort(l, relation) :
    for i in range(len(l)) :
        for j in range(i+1, len(l)) :
            if relation(l[i], l[j]) :
                l[i], l[j] = l[j], l[i]

def myFilter(l, predicate) :
    res = []
    for i in l :
        if predicate(i) == True :
            res.append(i)
    return res

def init():
    return 0

def getNext(sol, pos):
    return sol[pos] + 1

def isConsistent(sol):
    isCons = True
    i = 0
    while (i<len(sol)-1) and (isCons==True):
        if (sol[i] == sol[len(sol) - 1]):
            isCons = False
        else:
            i = i + 1
    return isCons

def isSolution(solution, n):
    return len(solution) == n
    
def getNext(index):
    return index+1

def initSolution(domain):
    return domain[0]   

def isConsistent(sol, myList, constraints):
    for c in constraints:
        if not c(sol, myList):
            return False
    return True

def getLast(domain):
    return domain[ len(domain) - 1 ]

def isSolution(sol, param):
    return len(sol) == param[0] 

def myBacktracking(param, myList, constraints):
    '''
    Forms groups of elements from the myList.
    IN: a list, a list, a list with functions.
    OUT: one or more lists with indices
    CONDIS: -
    '''
    domain = [  i  for i in range(-1, len(myList))   ]
    
    k = 0 #indexul curent din solutie 'sol

    sol = [] #solutia, la fiecare pas, lista cu indici

    sol.append(initSolution(domain))

    while(k >= 0):
        isSelected = False
        while not isSelected and sol[k] < getLast(domain):
            sol[k] = getNext( sol[k] )
            isSelected = isConsistent( sol, myList, constraints )
        
        if isSelected:
            if isSolution(sol, param):
                #print("YIELDEZ!!!!", sol)
                yield sol
            else:
                k = k+1
                sol.append(initSolution(domain))
        else:
            sol.pop()
            k = k - 1





