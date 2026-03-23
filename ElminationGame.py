class Solution:
    def lastRemaining(self, n: int) -> int:
        def fn(n):
            if n==1:
                return 1
            if n%2==1:
                n-=1
            return n+2*(1-fn(n//2))
        return fn(n)
            
        