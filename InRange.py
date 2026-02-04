class Solution:
    def isCovered(self, ranges, left: int, right: int) -> bool:
        res=[]
            
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                res.append(j)
        for i in range(left,right+1):
            if i not in res:
                return False
        return True
       
       

        