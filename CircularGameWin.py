class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def dfs(n):
            if n==1:
                return 0
            
            return (k+dfs(n-1))%n
        return dfs(n)+1