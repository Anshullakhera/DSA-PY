#User function Template for python3

class Solution:
    def kTop(self,a, N, K):
        #code here.
        result = []  # List to store arrays for each iteration
        freq_dict = {}  # Dictionary to store frequency of each number

        for i in range(N):
            num = a[i]
            freq_dict[num] = freq_dict.get(num, 0) + 1

            # Sort numbers based on frequency and value
            sorted_nums = sorted(freq_dict.keys(), key=lambda x: (freq_dict[x], -x), reverse=True)

            # Keep only top K numbers
            sorted_nums = sorted_nums[:K]

            result.append(sorted_nums[:])

        return result

#{ 
 # Driver Code Starts


t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.kTop(a,n,k)
    for line in ans:
        print(*line)



# } Driver Code Ends
