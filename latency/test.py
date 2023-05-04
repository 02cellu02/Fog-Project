import sys
sys.path.append('/Users/celes/OneDrive/Desktop/Celestine/Fog Project')

from knapsack_genetic_algo2 import solveKnapsack
from multi_knapsack_gen_algo_2 import solveMultiKnapsack
# from or_tool1 import main
import matplotlib.pyplot as plt
import random
from standalone2 import main
import fogfed2
noOfFogNodes=3
noOfEndUsers=[]
standTime=0
x=[]
y1=[]
y2=[]
for i in range(noOfFogNodes):
    noOfEndUsers.append(random.randint(10,30))
alpha=0.2
input_data=[[random.randint(100,500) for j in range(noOfEndUsers[i])] for i in range(noOfFogNodes)]
###
# noOfEndUsers=[5,7,6]
# capacity=[10*(10**10),10*(10**10),10*(10**10)]
# input_data=[[350,110,500,200,400],[100,200,300,400,500,250,130],[300,350,375,325,340,350]]
###
clock_cycles=[[random.randint(500,1500) for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
clock_speed_user=[[random.random() for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
clock_speed_fog=[[100 for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
upload_rate=[[random.randint(15,25) for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
download_rate=[[random.randint(20,30) for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
m=[[] for i in range(noOfFogNodes)]#amount of offloaded data
time_cpu_user=[[] for i in range(noOfFogNodes)]
beta=[[] for i in range(noOfFogNodes)]
weights=[[] for i in range(noOfFogNodes)]
# capacity=[]
answer=[]
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
# for i in range(noOfFogNodes):
    # noOfEndUsers.append(int(input(f'>>> Enter no of end-users of node {i+1}:    ')))
    # capacity.append(int(input(f'>>> Enter computational capacity of fog node {i+1}:    ')))
for i in range(noOfFogNodes):
    for j in range(noOfEndUsers[i]):
        # input_data[i].append(int(input(f">>> Enter amount of input data for user {j+1} of fog node {i+1}:   ")))
        # clock_cycles[i].append(int(input(f">>> Enter no of clock cycles of user {j+1} of fog node {i+1}:   ")))
        # clock_speed_user[i].append(int(input(f">>> Enter clock speed of user {j+1} of fog node {i+1}:   ")))
        # clock_speed_fog[i].append(int(input(f">>> Enter clock speed alloted to user {j+1} of fog node {i+1}:   ")))
        # upload_rate[i].append(int(input(f">>> Enter uplink transmission rate between user {j+1} and fog node {i+1}:   ")))
        # download_rate[i].append(int(input(f">>> Enter downlink transmission rate between user {j+1} and fog node {i+1}:   ")))
        beta[i].append(((10**(-6))/(upload_rate[i][j]))+(clock_cycles[i][j]/(clock_speed_fog[i][j]*(10**9)))+(alpha/(download_rate[i][j]*(10**6))))
        m[i].append(clock_cycles[i][j]*input_data[i][j]*(8*(10**3))/((beta[i][j]*clock_speed_user[i][j]*(10**9))+clock_cycles[i][j]))
        weights[i].append(m[i][j]*clock_cycles[i][j])
        time_cpu_user[i].append(clock_cycles[i][j]*(input_data[i][j]*8*(10**3)-m[i][j])/clock_speed_user[i][j])
time_cpu_user_new=time_cpu_user.copy()
for k in range (1):
    
    capacity =[10*(2*k+1)*(10**(9)) for j in range(3)]
    
    a1=main(capacity[0],noOfEndUsers[0],time_cpu_user_new[0],weights[0])
    b1=fogfed2.main(capacity,noOfFogNodes,noOfEndUsers,answer,time_cpu_user_new,weights)
    if a1==-1 or b1==-1:
        continue
    x.append(10*(2*k+1)*(10**(9)))
    y1.append(a1)
    y2.append(b1)
    
print(x,y1,y2)
# Create the plot
plt.plot(x, y1, label='Standalone Fog node',alpha =0.5)
plt.plot(x, y2, label='Fog Federation',alpha= 0.5,linestyle='--')

# Add labels and title to the plot
plt.xlabel('Computational capacity per fog node (CPU cycles/slot)')
plt.ylabel('Latency')


# Add legend to the plot
plt.legend()

# Show the plot
plt.show()