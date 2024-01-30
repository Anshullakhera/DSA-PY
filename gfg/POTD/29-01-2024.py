#User function Template for python3
from bisect import bisect_left

class Solution:
    def help(self, ind, _sum, s, dp):
        if ind == len(s):
            return 1

        if dp[ind][_sum] != -1:
            return dp[ind][_sum]

        x = 0
        ans = 0
        for i in range(ind, len(s)):
            x += int(s[i])
            if x >= _sum:
                ans += self.help(i + 1, x, s, dp)

        dp[ind][_sum] = ans
        return ans
    def TotalCount(self, s):
        n = len(s)
        dp = [[-1] * 901 for _ in range(n)]
        return self.help(0, 0, s, dp)
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends
