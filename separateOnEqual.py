class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)%2==1:
            return -1
        l=0
        r=len(skill)-1
        skill.sort()
        pre=len(skill)//2
        expected=sum(skill)//pre
        total=0
        while l<r:
            if skill[l]+skill[r]!=expected:
                return -1
            total+=skill[l]*skill[r]
            l+=1
            r-=1
        return total
        