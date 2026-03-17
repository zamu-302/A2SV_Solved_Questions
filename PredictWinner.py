class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total=sum(nums)
        memo={}
        def maxi(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if i>j:
                return 0
            
            sa=nums[i]+min(maxi(i+1,j-1),maxi(i+2,j))
            sb=nums[j]+min(maxi(i,j-1),maxi(i+1,j-2))
            score=max(sa,sb)
            memo[i,j]=score
            return score
        pa=maxi(0,len(nums)-1)
        return pa>=(total-pa)

        