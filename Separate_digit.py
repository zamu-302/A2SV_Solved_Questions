import sys
sys.set_int_max_str_digits(0)
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        k="".join(str(num) for num in nums)
        res=[]
        for i in range(len(k)):
            res.append(int(k[i]))
        return res
        
       
            
                
        