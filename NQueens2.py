class Solution:
    def totalNQueens(self, n: int) -> int:
        dy=set()
        dx=set()
        col=set()
        arr=[["."]*n for i in range(n)]
        count=0
        def dfs(i):
            nonlocal count
            #base case
            if i==n:
                count+=1




           
            for j in range(n):
                if ((i-j) not in dx)and ((i+j) not in dy) and (j not in col):
                        #valid
                    dx.add(i-j)
                    dy.add(i+j)
                    col.add(j)
                    arr[i][j]="Q"
                    dfs(i+1)
                    dx.remove(i-j)
                    dy.remove(i+j)
                    col.remove(j)
                    arr[i][j]="."
            
        dfs(0)
       
        
        return count
            

        
                    

                    
                        
                

                  




            


