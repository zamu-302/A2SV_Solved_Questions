from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums)
        a=a.most_common()
        
        return [a[i][0] for i in range(k)]