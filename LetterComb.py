class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        seen=defaultdict(list)
        seen={
           
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        ans=[]
        def dfs(i,arr):
            nonlocal ans
            if i==len(digits):
                shallow="".join(arr)
                ans.append(shallow)
                return
            

            k=seen[digits[i]]
            for j in range(len(k)):
                arr.append(k[j])
                dfs(i+1,arr)
                arr.pop()
        dfs(0,[])
        return ans
        
            





        