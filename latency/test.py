def findMaximumTime(answer, t):
    totalMax = 0
    for i, a in enumerate(answer):
        maxScore = 0
        for j, c in enumerate(a[0]):
            if c=='1':
                maxScore = max(maxScore, t[i][j])
        totalMax=max(maxScore, totalMax)
    return totalMax

def findMaximumTime2(answer, t):
    maxTime = 0
    for i, a in enumerate(answer):
        for j, c in enumerate(a[0]):
            if c=='1':
                maxTime = max(maxTime, t[i][j])
    return maxTime

answer = [['0110', 25],['11001', 30]]

t = [[25,30,15,8],[1,50,8,9,12]]


print(findMaximumTime2(answer,t))