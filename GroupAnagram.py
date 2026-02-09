class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        res=[]
        for i in range(len(strs)):
            val="".join(sorted(strs[i]))
            if val in seen:
                seen[val].append(strs[i])
            else:
                seen[val]=[strs[i]]
        for key,val in seen.items():
            res.append(seen[key])
        return res
        