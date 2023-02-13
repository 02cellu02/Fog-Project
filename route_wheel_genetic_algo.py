import random
capacity=int(input(">>> Enter capacity of knapsack: "))
n=int(input(">>> Enter no of items: "))
itemsString=input(">>> Enter items:    ")
items=list(map(int, itemsString.split(',')))
# items=[int(input(f">>>enter item {i+1}: ")) for i in range(n)]
print(items)
setInitpop=50
generations=500
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
    parents=random.choices(population,weights=list(map(fitness,population)),k=2)
    # parents=[]
    # parent1=random.choice(population,)
    # parent2=random.choice(population)
    # if fitness(parent1)>=fitness(parent2):
    #     parents.append(parent1)
    # else:
    #     parents.append(parent2)

    # parent3=random.choice(population)
    # parent4=random.choice(population)
    # if fitness(parent3)>=fitness(parent4):
    #     parents.append(parent3)
    # else:
    #     parents.append(parent4)
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
    return newChild if fitness(newChild) else child

def mutate10(child ,idx):
    newChild=''
    for i in range(n):
        if i==idx:
            newChild+='0'
            continue
        newChild+=child[i]
    return

def mutation(children):
    idx1=random.randint(0,n-1)
    idx2=random.randint(0,n-1)
    children[0]=mutate(children[0],idx1)
    children[1]=mutate(children[1],idx2)

def nextGen(population):
    newGen=[]
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
    return newGen
def avgFit(population):
    return sum([fitness(elt) for elt in population])/setInitpop

def solveKnapsack(n):
    population=[genRandBinString(n) for i in range(setInitpop)]
    for i in range(generations):
        population=nextGen(population)
        print(f"avg fitness for gen {i}: {avgFit(population)}")
    population = sorted(population, key=lambda i: fitness(i), reverse=True)
    print(population)
    return population[0]

print(solveKnapsack(n))