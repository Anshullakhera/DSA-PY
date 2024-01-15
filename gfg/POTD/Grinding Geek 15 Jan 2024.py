

from typing import List


class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        # code here
        dp = [[0] * (total + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(total + 1):
                take, notake = 0, 0

                notake = dp[i + 1][j]

                if cost[i] <= j:
                    rem = j - cost[i] + int(cost[i] * 0.9)
                    take = 1 + dp[i + 1][rem]

                dp[i][j] = max(take, notake)

        return dp[0][total]
#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        total = int(input())
        
        
        cost=IntArray().Input(n)
        
        obj = Solution()
        res = obj.max_courses(n, total, cost)
        
        print(res)
        

# } Driver Code Ends
