import random
from test_run_fog_project1 import runner_code
noOfFogNodes=3
capacity=[9*(10**11),9*(10**11),9*(10**11)]
alpha=0.2
noOfUsers=[]
for i in range(noOfFogNodes):
    noOfUsers.append(random.randint(10,100))

input_data=[]
clock_cycles=[]
clock_speed_user=[]
clock_speed_fog=[]
upload_rate=[]
download_rate=[]
for i in range(noOfFogNodes):
    input_data1=[]
    clock_cycles1=[]
    clock_speed_user1=[]
    clock_speed_fog1=[]
    upload_rate1=[]
    download_rate1=[]
    for j in range(noOfUsers[i]):
        input_data1.append((random.randint(100,500)))
        clock_cycles1.append((random.randint(500,1500)))
        clock_speed_user1.append((random.choice([i*0.1 for i in range(1,11)])))
        clock_speed_fog1.append(100)
        upload_rate1.append((random.randint(15,25)))
        download_rate1.append((random.randint(20,30)))
    input_data.append(input_data1)
    clock_cycles.append(clock_cycles1)
    clock_speed_user.append(clock_speed_user1)
    clock_speed_fog.append(clock_speed_fog1)
    upload_rate.append(upload_rate1)
    download_rate.append(download_rate1)

runner_code(noOfFogNodes,capacity,alpha,noOfUsers,input_data,clock_cycles,clock_speed_user,clock_speed_fog,upload_rate,download_rate)