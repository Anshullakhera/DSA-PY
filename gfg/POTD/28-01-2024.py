
from typing import List

class Solution:
    def findNthNumber(self, n : int, k : int ) -> int:
        def ncr(n, r):
            ans = 1
            
            # n! / ((n - r)! * r!)
            for i in range(n, max(r, n - r), -1):
                ans *= i
                
            den = 1
            
            for i in range(1, min(r, n - r) + 1):
                den *= i
                
            ans //= den
            
            return ans
        
        dp = [[0] * (k + 1) for _ in range(63)]
        
        for i in range(63):
            for j in range(k + 1):
                for x in range(min(i + 1, j) + 1):
                    dp[i][j] += ncr(i + 1, x)
        
        pos = 0
        
        for i in range(63):
            if dp[i][k] >= n:
                pos = i
                break
        
        ans = 0
        while pos > -1 and n > 0:
            if pos + 1 <= k:
                ans += n - 1
                break
            
            if pos > 0 and dp[pos - 1][k] < n:
                ans |= (1 << pos)
                n -= dp[pos - 1][k]
                k = max(k - 1, 0)
            
            pos -= 1
        
        return ans


#{ 
 # Driver Code Starts



if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k=map(int,input().split())
        
        obj = Solution()
        res = obj.findNthNumber(n,k)
        
        print(res)
        

# } Driver Code Ends
