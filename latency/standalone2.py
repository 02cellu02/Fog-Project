import sys
sys.path.append('/Users/celes/OneDrive/Desktop/Celestine/Fog Project')
from knapsack_genetic_algo2 import solveKnapsack
from multi_knapsack_gen_algo_2 import solveMultiKnapsack
from or_tool1 import main
import random

def findMaximumTime(answer, t):
    maxTime = 0
    for i,a in enumerate(answer[0]):
          if a=='1':
               maxTime=max(maxTime,t[i])
    # for i, a in enumerate(answer):
        # for j, c in enumerate(a[0]):
            # if c=='1':
                # maxTime = max(maxTime, t[i][j])
    return maxTime

def remainItems(item,time_cpu_user):
    remUsers=[]
    time_cpu=[]
    for i in range(len(item)):
        if item[i]=='0':
            remUsers.append(weights[i])
            time_cpu.append(time_cpu_user[i])
            
    return (remUsers,time_cpu)
def main(capacity,noOfEndUsers,time_cpu_user_new,weight):
    global weights
    answer=[0,0]
    weights=weight
    standTime=0
    time_nodes=time_cpu_user_new.copy()
    while True:
        if noOfEndUsers==1:
             return time_cpu_user_new[0]
        
        answer[0],answer[1]=(solveKnapsack(capacity,noOfEndUsers,weights))
        
        
        standTime+=findMaximumTime(answer,time_nodes)
        # time_cpu_user_new=[[] for i in range(noOfFogNodes)]
        
        
        y,time_nodes=  remainItems(answer[0],time_nodes)
        if answer[1]==0:
            breakpoint
                
                
                
        if y:
                weights=y
                # remUsersWeights[idx].append(y)#adding remaining uses of fog node [idx]
                noOfEndUsers=len(y)
                
        else:
                print("all users offloade their data to primary fog node")
        
                break
        
    return standTime

       
    