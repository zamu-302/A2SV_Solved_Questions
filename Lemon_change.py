class Solution:
    def lemonadeChange(self, nums: List[int]) -> bool:
        five=0
        ten=0
        for i in range(len(nums)):
            if nums[i]==5:
                five+=1
            
            elif nums[i]==10:
                    ten+=1
                    if five>0:
                        five-=1
                    else:
                        print(five,ten)
                        return False
            else:
                if ten>0 and five>0:
                    ten-=1
                    five-=1
                elif five>2:
                    five-=3
                else:
                    print(five,ten)
                    return False
        return True
        