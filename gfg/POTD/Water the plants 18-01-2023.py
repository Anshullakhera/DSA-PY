#User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        # code here
        cover=[(0,0)]*n
        for i in range(n):
            cover[i]=(i-gallery[i], i+gallery[i])
        cover.sort(key = lambda x: x[0])
        take, ans, index=0, 0, 0
        while (take<n):
            nax = take - 1
            while (index < n and cover[index][0] <= take):
                nax = max(nax, cover[index][1])
                index+=1
            if nax + 1 > take:
                ans+=1
                take = nax + 1
            else:
                return -1
        return ans;


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        gallery = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.min_sprinklers(gallery,n))

# } Driver Code Ends
