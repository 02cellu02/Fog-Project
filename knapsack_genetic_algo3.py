import random
n,capacity=0,0
items=[]
setInitpop=50
generations=1000
CROSSOVER_RATE = 0.53
MUTATION_RATE = 0.013
REPRODUCTION_RATE = 0.15

def genRandBinString(n):
    number=""
    for i in range(n):
        number+=str(random.randint(0,1))
    return number

def fitness(item):
    fit=0
    for i in range(n):
        if item[i]=='1':
            fit+=items[i]
    return fit if fit<=capacity else 0

def selection(population):
    x,y=0,0
    parents=[]
    parent1,parent2,parent3,parent4="","","",""
    while True:
        parent1=random.choice(population)
        parent2=random.choice(population)
        x=fitness(parent1)
        y=fitness(parent2)
        if x or y:
            break
    if x>=y:
        parents.append(parent1)
    else:
        parents.append(parent2)
    while True:
        parent3=random.choice(population)
        parent4=random.choice(population)
        x=fitness(parent3)
        y=fitness(parent4)
        if x or y:
            break
    
    if x>=y:
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
            newChild+='1' 
            continue
        newChild+=child[i]
    return newChild if fitness(newChild) else (mutate0110(newChild) or child)
def mutate0110(child):
    ones,zeros=[],[]
    for i in range(n):
        if child[i]=='0':
            zeros.append(i)       
        else:
            ones.append(i)
    zeroIdx=random.choice(zeros) if zeros else -1
    oneIdx=random.choice(ones)
    newChild=''
    for i in range(n):
        if i==zeroIdx:
            newChild+='1'
            continue
        elif i==oneIdx:
            newChild+='0'
            continue
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

def solveKnapsack(init_capacity,noOfItems,weights):
    global n,capacity,items
    capacity=init_capacity#int(input(">>> Enter capacity of knapsack: "))
    n=noOfItems#int(input(">>> Enter no of items: "))
    # itemsString=input(">>> Enter items:    ")
    items=weights  #list(map(int, itemsString.split(' ')))
    # items=[int(input(f">>>enter item {i+1}: ")) for i in range(n)]
    # print(items)
    
    population=[genRandBinString(n) for i in range(setInitpop)]
    for i in range(generations):
        population,end=nextGen(population)
        if end:
            break
        # print(f"avg fitness for gen {i}: {avgFit(population)}")
    population = sorted(population, key=lambda i: fitness(i), reverse=True)
    # print(population)
    return (population[0],fitness(population[0]))

# print(solveKnapsack())