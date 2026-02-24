class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        seen={}
        if c<=2:
            return True
        for i in range(c):
            if c-i**2<0:
                return False
            elif c-i**2 in seen or i**2+i**2==c:
                return True
            seen[i**2]=1
        

        