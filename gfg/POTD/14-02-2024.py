#User function Template for python3

class Solution:
    def criticalConnections(self, v, adj):
        # code here
        result = []
        visited = [False] * v
        ids = [0] * v
        low = [0] * v
        timer = 0

        def dfs(current, parent):
            nonlocal timer
            visited[current] = True
            ids[current] = timer
            low[current] = timer
            timer += 1

            for neighbor in adj[current]:
                if neighbor == parent:
                    continue
                if not visited[neighbor]:
                    dfs(neighbor, current)
                    low[current] = min(low[current], low[neighbor])

                    if low[neighbor] > ids[current]:
                        if current > neighbor:
                            result.append((neighbor, current))
                        else:
                            result.append((current, neighbor))
                else:
                    low[current] = min(low[current], ids[neighbor])

        for i in range(v):
            if not visited[i]:
                dfs(i, -1)
        result.sort()
        return result
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends
