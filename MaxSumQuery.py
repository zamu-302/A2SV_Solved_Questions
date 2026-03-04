#freq=freq[:n] because this is only used the n+1 is just a mappper to avoid over counting.

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        freq=[0]*(n)
        for l,r in requests:
            freq[l]+=1
            if r+1<n:
                freq[r+1]-=1
        for i in range(1,n):
            freq[i]+=freq[i-1]
        nums.sort()
        freq.sort()
        ans=0
        mod=10**9+7
        for a,b in zip(nums,freq):
            ans=(ans+a*b)%mod
        return ans

        