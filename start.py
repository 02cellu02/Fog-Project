from knapsack_genetic_algo2 import solveKnapsack
noOfFogNodes=3
noOfEndUsers=[]
alpha=0.2
# input_data=[[] for i in range(noOfFogNodes)]
###
noOfEndUsers=[5,7,6]
capacity=[9*(10**9),9*(10**9),9*(10**9)]
input_data=[[350,110,500,200,400],[100,200,300,400,500,250,130],[300,350,375,325,340,350]]
###
clock_cycles=[[750 for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
clock_speed_user=[[0.5 for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
clock_speed_fog=[[15 for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
upload_rate=[[20 for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
download_rate=[[25 for j in range(noOfEndUsers[i]) ] for i in range(noOfFogNodes)]
m=[[] for i in range(noOfFogNodes)]#amount of offloaded data
beta=[[] for i in range(noOfFogNodes)]
weights=[[] for i in range(noOfFogNodes)]
# capacity=[]
answer=[]


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
    answer.append(solveKnapsack(capacity[i],noOfEndUsers[i],weights[i])[0])

print(answer)

    
