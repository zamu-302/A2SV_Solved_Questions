class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        seen={}
        res=[]
        for i in range(len(list1)):
            seen[list1[i]]=i
        for i in range(len(list2)):
            if list2[i] in seen:
                res.append([list2[i],seen[list2[i]]+i])
        res=sorted(res,key=lambda x:x[1])
        lowest=res[0][1]

        return [res[i][0] for i in range(len(res))if res[i][1]==lowest]