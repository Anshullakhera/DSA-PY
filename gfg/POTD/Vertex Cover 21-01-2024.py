from typing import List





class Solution:

    def next(self, x):

        smallest = x & -x

        ripple = x + smallest

        new_smallest = ripple & -ripple

        ones = ((new_smallest // smallest) >> 1) - 1

        return ripple | ones

    def vertexCover(self, n : int, edges : List[List[int]]) -> int:

        # code here

        ans = 20



        def check(bits):

            cur = (1 << bits) - 1



            while cur < (1 << n):

                m = len(edges)



                for edge in edges:

                    x, y = edge

                    x -= 1

                    y -= 1



                    if (cur >> x) & 1 or (cur >> y) & 1:

                        m -= 1



                if m == 0:

                    return True



                cur = self.next(cur)



            return False



        low = 0

        high = n



        while low < high - 1:

            mid = low + (high - low) // 2



            if check(mid):

                high = mid

            else:

                low = mid



        return high





#{ 

 # Driver Code Starts

class IntMatrix:

    def __init__(self) -> None:

        pass

    def Input(self,n,m):

        matrix=[]

        #matrix input

        for _ in range(n):

            matrix.append([int(i) for i in input().strip().split()])

        return matrix

    def Print(self,arr):

        for i in arr:

            for j in i:

                print(j,end=" ")

            print()





if __name__=="__main__":

    t = int(input())

    for _ in range(t):

        

        n = int(input())

        

        

        m = int(input())

        

        

        edges=IntMatrix().Input(m, m)

        

        obj = Solution()

        res = obj.vertexCover(n, edges)

        

        print(res)

        



# } Driver Code Ends
