from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        seen={}
        res=[]
        for i in range(len(responses)):
            for j in range(len(responses[i])):
                if responses[i][j] not in seen:
                    seen[responses[i][j]]=1
            res.extend(list(seen.keys()))
            seen={}
        total=Counter(res)
        total=sorted(total.items(),key=lambda x:(-x[1],[x[0]]))
        return total[0][0]
        
     