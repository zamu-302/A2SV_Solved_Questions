class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[]
     
        def dfs(ans,i):
        
            #not base case
           
            #A solution
            if len(ans)==k:
                arr.append(ans[:])
                return
            if i>n:
                return 

            
            #pick 
            ans.append(i)
            dfs(ans,i+1)
            ans.pop()
            #no pick
            dfs(ans,i+1)

                
            
        dfs([],1)
        return arr
        


            





        