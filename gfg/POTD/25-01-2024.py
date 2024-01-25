#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import deque
class Solution:
    def __init__(self):
        self.primes = []
        self.computed = 0
    def sieve(self):
            n = 9999
            primes = []
            prime = [1] * (n + 1)
            prime[0] = prime[1] = 0

            for i in range(2, int(n**0.5) + 1):
                if prime[i]:
                    for j in range(i * i, n + 1, i):
                        prime[j] = 0

            for i in range(1000, n + 1):
                if prime[i]:
                    primes.append(str(i))

            self.primes = primes
            self.computed = 1
    def solve (self,num1,num2):
        #code here
        if num1 == num2:
            return 0

        if not self.computed:
            self.sieve()

        inf = 1e9
        d = {i: inf for i in self.primes}

        start = str(num1)
        end = str(num2)

        d[start] = 0
        q = deque([start])

        while q:
            cur = q.popleft()
            for i in range(4):
                for j in range(ord('1') if i == 0 else ord('0'), ord('9') + 1):
                    j = chr(j)
                    if j != cur[i]:
                        next_str = cur[:i] + j + cur[i + 1:]

                        if next_str in d and d[next_str] > d[cur] + 1:
                            d[next_str] = d[cur] + 1
                            q.append(next_str)

                            if next_str == end:
                                return d[next_str]

        return -1
        



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1,num2=map(int,input().split())
        ob = Solution()
        print(ob.solve(num1,num2))
# } Driver Code Ends
