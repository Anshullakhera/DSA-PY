#User function Template for python3

class Solution:
    def isTree(self, n, m, edges):
        # Code here
        if m != n - 1:
            return 0
            
        vis = [0] * n
        g = [[] for _ in range(n)]
        
        for i in range(m):
            g[edges[i][0]].append(edges[i][1])
            g[edges[i][1]].append(edges[i][0])
        
        def dfs(node, parent):
            nonlocal vis
            ans = True
            vis[node] = 1
            
            for child in g[node]:
                if not vis[child]:
                    ans = ans and dfs(child, node)
                elif child != parent:
                    return False
            
            return ans
        ans = True
        cc = 0
        
        for i in range(n):
            if not vis[i]:
                ans = ans and dfs(i, -1)
                cc += 1   
        
        return int(ans and cc == 1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range (int(input())):
    n,m = [int(i) for i in input().split()]
    edges = []
    for i in range(m):
        a,b = map(int,input().split())
        edges.append([a,b])

    ob = Solution()
    print(ob.isTree(n,m,edges))
# } Driver Code Ends
