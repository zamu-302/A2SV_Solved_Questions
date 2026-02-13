class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        seen=defaultdict(list)
        count=0
        
        for i in range(len(nums)):
            if nums[i] in seen:
              for num in seen[nums[i]]:
                if num*i%k==0:
                    count+=1  
            seen[nums[i]].append(i)   
                
        return count
        