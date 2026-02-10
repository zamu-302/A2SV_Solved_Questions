class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        
        while True:
            total=0
            
            n=str(n)
            for num in n:
                total+=int(num)**2
            a.add(int(n))
            n=total
            if total==1:
                return True
            if total in a :
               return False
            

