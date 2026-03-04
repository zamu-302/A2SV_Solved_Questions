class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)-1
        seen={0:1}
        curr=0
        count=0
        for i in range(len(nums)):
            curr+=nums[i]
            if curr-k in seen:
                count+=seen[curr-k]
            seen[curr]=seen.get(curr,0)+1
        return count
      


        