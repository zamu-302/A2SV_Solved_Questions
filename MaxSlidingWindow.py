from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        ans=[]

        
        left=0
        for right in range(len(nums)):
            if q and q[0]<=right-k:
                q.popleft()
            while q and nums[right]>nums[q[-1]]:
                q.pop()
            q.append(right)
            if right==k+left-1:
                ans.append(nums[q[0]])
                left+=1
            
        
        return ans

        