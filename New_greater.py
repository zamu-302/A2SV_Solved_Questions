from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=defaultdict(lambda: -1)
        stk=[]
        for i in range(len(nums2)):
            while stk and stk[-1]<nums2[i]:
                seen[stk[-1]]=nums2[i]
                stk.pop()
            stk.append(nums2[i])
        for i in range(len(nums1)):
                nums1[i]=seen[nums1[i]]
        return nums1



        
