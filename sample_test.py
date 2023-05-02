#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.1 4 5 7 6 11 10 7 8 12 20 15 18 9 3 13 5 21 12 14 9 9 11 17 20
    def knapSack(self,W, wt, val, n):
        t=[[0 for i in range(W+1)]for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        return t[n][W]
       
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends