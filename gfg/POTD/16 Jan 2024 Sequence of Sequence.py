#User function Template for python3

class Solution:
    def numberSequence(self, m, n):
        # code here
        if m == 0 or n == 1:
            return m

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][1] = i

        for j in range(2, n + 1):
            for i in range(1, m + 1):
                for k in range(i, 0, -1):
                    dp[i][j] += dp[k // 2][j - 1]

        return dp[m][n]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        arr = input().split()
        m = int(arr[0])
        n = int(arr[1])
        
        ob = Solution()
        print(ob.numberSequence(m, n))
# } Driver Code Ends
