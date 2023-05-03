import sys
sys.path.append('/Users/celes/OneDrive/Desktop/Celestine/Fog Project')

from fog_simulate1 import main
import random
import matplotlib.pyplot as plt
from multi_knapsack_gen_algo_2 import solveMultiKnapsack
from knapsack_genetic_algo2 import solveKnapsack

def remainItems(item,nodeIdx):
    remUsers=[]
    for i in range(len(item)):
        if item[i]=='0':
            remUsers.append(weights[nodeIdx][i])
x=[]
y1=[]
y2=[]
noOfFogNodes=3
noOfEndUsers=[]
for i in range(noOfFogNodes):
    noOfEndUsers.append(random.randint(10,30*(i+1)))
alpha=0.2
input_data=[[random.randint(100,500) for j in range(noOfEndUsers[i])] for i in range(noOfFogNodes)]
clock_cycles=[[random.randint(500,1500) for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
clock_speed_user=[[random.random() for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
clock_speed_fog=[[100 for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
upload_rate=[[random.randint(15,25) for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
download_rate=[[random.randint(20,30) for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
m=[[] for i in range(noOfFogNodes)]#amount of offloaded data
beta=[[] for i in range(noOfFogNodes)]
weights=[[] for i in range(noOfFogNodes)]

###################
print("No of fog nodes : ",noOfFogNodes)
print("No of end users : ",noOfEndUsers)
for i in range(noOfFogNodes):
    # print(f"capacity of fog node {i+1}:   {capacity[i]}")
    for j in range(noOfEndUsers[i]):
        print(f"    Input data, clock cycles per bit of user {j+1}:   {input_data[i][j]}, {clock_cycles[i][j]}")
print("\n"*5)
print("computing computational resources required for each user")
####################
for i in range(noOfFogNodes):
    for j in range(noOfEndUsers[i]):
        beta[i].append(((10**(-6))/(upload_rate[i][j]))+(clock_cycles[i][j]/(clock_speed_fog[i][j]*(10**9)))+(alpha/(download_rate[i][j]*(10**6))))
        m[i].append(clock_cycles[i][j]*input_data[i][j]*(8*(10**3))/((beta[i][j]*clock_speed_user[i][j]*(10**9))+clock_cycles[i][j]))
        weights[i].append(m[i][j]*clock_cycles[i][j])

for k in range (10):
    answer=[]
    capacity =[10*(2*i+1)*(10**(8)) for j in range(3)]
    x.append(10*(2*i+1)*(10**(9)))
    for i in range(noOfFogNodes):
        answer.append(solveKnapsack(capacity[i],noOfEndUsers[i],weights[i]))
    for i in range(noOfFogNodes):
        print(f"capacity of fog node {i+1}:   {capacity[i]}")
        for j in range(noOfEndUsers[i]):
            print(f"computational resources req for end user {j+1}: {weights[i][j]}")
    print('Standalone Fog node....')
    for i in range(noOfFogNodes):
        print(f"Set of users for node {i+1}:    {answer[i][0]}")
    newCapacity=[]
    remUsersWeights=[]
    remNodes=0
    standAloneRevenue=0
    for idx,value in enumerate(answer):
        standAloneRevenue+=value[1]
        y=  remainItems(value[0],idx)
        if value[1]==0:
            newCapacity.append(capacity[idx])
            remNodes+=1
            remUsersWeights+=weights[idx]
            continue
        if y:
            remUsersWeights+=y#adding remaining uses of fog node [idx]
        else:
            print("all users offloade their data to primary fog node")

        if value[1]<capacity[idx]:
            newCapacity.append(capacity[idx]-value[1])
            remNodes+=1
    print(f"No of nodes having remaing computational resources :    {remNodes}")
    print(f"No of users who haven't offloaded to the primary fog node: {len(remUsersWeights)}")
    for i in range(remNodes):
        print(f"capacity for new fog Node {i+1}:    {newCapacity[i]}")
    for i in range(len(remUsersWeights)):
        print(f"computational resources req for new user {i+1}:  {remUsersWeights[i]}")
    if not remNodes or not remUsersWeights:
        y1.append(standAloneRevenue)
        y2.append(standAloneRevenue)
        continue
    migrated_users,revenue_fed=solveMultiKnapsack(remNodes,newCapacity,len(remUsersWeights),remUsersWeights)
    print(f"set of users who offloaded to secondary node:   {migrated_users}")
    if not revenue_fed:
        y1.append(standAloneRevenue)
        y2.append(standAloneRevenue)
        continue
    y1.append(standAloneRevenue)
    y2.append(revenue_fed+standAloneRevenue)


print(x,y1,y2)
# Create the plot
plt.plot(x, y1, label='Standalone Fog node',alpha =0.5)
plt.plot(x, y2, label='Fog Federation',alpha= 0.5,linestyle='--')

# Add labels and title to the plot
plt.xlabel('Computational capacity per fog node (CPU cycles/slot)')
plt.ylabel('Total revenue (unit price)')


# Add legend to the plot
plt.legend()

# Show the plot
plt.show()