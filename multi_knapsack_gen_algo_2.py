import random
n,noOfKnapsacks=0,0

items,capacity=[],[]
setInitpop=50
generations=100
CROSSOVER_RATE = 0.83
MUTATION_RATE = 0.013
REPRODUCTION_RATE = 0.15
INFILTRATE=3

def genRandIntegerString(n,noOfKnapsacks):
    number=''.join([str(random.choice([(random.randint(0, noOfKnapsacks))])) for i in range(n)])
    return number

def addBasePopl(n,noOfSacks):
    base=[0 for i in range(n)]
    basePopulation=[]
    for i in range(n):
        for k in range(INFILTRATE):
            for j in range(1,noOfSacks+1):
                base[i]=j
                basePopulation.append(''.join(map(str,base)))
                base[i]=0
    return basePopulation
        

def fitness(item):
    sumOfFitness=0
    for i in range(noOfKnapsacks):
        s= individualFitness(item,i+1)
        if s==-1:
            return 0
        sumOfFitness+=s
    return sumOfFitness
        
        
        
def individualFitness(item,knpsack):#knpsack index starting from one
    fit=0
    for i in range(n):
        if item[i]==str(knpsack):
            fit+=items[i]
    return fit if fit<=capacity[knpsack-1] else -1

def selection(population):
    parents=[]
    parent1=random.choice(population)
    parent2=random.choice(population)
    if fitness(parent1)>=fitness(parent2):
        parents.append(parent1)
    else:
        parents.append(parent2)

    parent3=random.choice(population)
    parent4=random.choice(population)
    if fitness(parent3)>=fitness(parent4):
        parents.append(parent3)
    else:
        parents.append(parent4)
    return parents

def crossover(parents):
    idx=random.randint(1,n-1)
    child1=parents[0][:idx]+parents[1][idx:]
    child2=parents[1][:idx]+parents[0][idx:]
    return [child1,child2]
def mutate(child,idx):
    newChild=''
    for i in range(n):
        if i==idx:
            packNo=str(random.randint(1, noOfKnapsacks))
            newChild+=packNo
            continue
        newChild+=child[i]
    return newChild if fitness(newChild) else (mutate0110(newChild,packNo) or child)
def mutate0110(child,packNo):
    zeros,package=[],[]
    for i in range(n):
        if child[i]==packNo:
            package.append(i)       
        elif child[i]=='0':
            zeros.append(i)
    packageIdx=random.choice(package) 
    zeroIdx=random.choice(zeros) if zeros else -1
    newChild=''
    for i in range(n):
        if i==packageIdx:
            newChild+=str(random.choice([0,(random.randint(1, noOfKnapsacks))])) 
            continue
        # elif i==zeroIdx:
        #     newChild+=packNo
        #     continue
        newChild+=child[i]
    return newChild if fitness(newChild) else None
def mutation(children):
    idx1=random.randint(0,n-1)
    idx2=random.randint(0,n-1)
    children[0]=mutate(children[0],idx1)
    children[1]=mutate(children[1],idx2)

def nextGen(population):
    newGen=[]
    end=''
    children=[]
    while len(newGen)< len(population):
        parents=selection(population)
        children=parents
        if random.random()>REPRODUCTION_RATE:
            if random.random()>CROSSOVER_RATE:
                children=crossover(parents)
            if random.random()>MUTATION_RATE:
                mutation(children)
        for i in children:
            newGen.append(i)
            if fitness(i)==capacity:
                end=i
    return (newGen,end)
def avgFit(population):
    return sum([fitness(elt) for elt in population])/setInitpop

def solveMultiKnapsack(initNoOfKnapsack,init_capacity,noOfItems,weights):
    global n,capacity,items,noOfKnapsacks
    noOfKnapsacks=initNoOfKnapsack
    capacity=init_capacity#int(input(">>> Enter capacity of knapsack: "))
    n=noOfItems#int(input(">>> Enter no of items: "))
    # itemsString=input(">>> Enter items:    ")
    items=weights  #list(map(int, itemsString.split(' ')))
    # items=[int(input(f">>>enter item {i+1}: ")) for i in range(n)]
    # print(items)
    
    population=[genRandIntegerString(n,noOfKnapsacks) for i in range(setInitpop-(n*noOfKnapsacks*INFILTRATE))]
    #adding base population
    population+=addBasePopl(n,noOfKnapsacks)
    # adding no of base population = n* no of knapsacks
    
    
    for i in range(generations):
        population,end=nextGen(population)
        if end:
            break
        # print(f"avg fitness for gen {i}: {avgFit(population)}")
    population = sorted(population, key=lambda i: fitness(i), reverse=True)
    # print(population)
    return (population[0],fitness(population[0]))

# print(solveKnapsack())
#runner code
# no_of_knapsack=5
# capacities=[100, 100, 100, 100, 100]
# no_of_items=15
# value=[
#         48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36
#     ]
# print(solveMultiKnapsack(no_of_knapsack,capacities,no_of_items,value))