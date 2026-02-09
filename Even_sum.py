class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        total=0
        for j in nums:
            if j%2==0:
                total+=j  
        for i in range(len(queries)):
            if nums[queries[i][1]]%2==0:
                cur=nums[queries[i][1]]
                nums[queries[i][1]]+=queries[i][0]

                if nums[queries[i][1]]%2!=0:
                    total-=cur
                else:
                    total+=queries[i][0]

            else:
                nums[queries[i][1]]+=queries[i][0]
                if nums[queries[i][1]]%2==0:
                    total+=nums[queries[i][1]]
            res.append(total)
        return res

           

           
    