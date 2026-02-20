class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left=0
        right=len(piles)-1
        total=0
        while left<right:
            total+=piles[right-1]
            right-=2
            left+=1
        return total



        