class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length=max(citations)
        curr=0
        for i in range(length+1):
            count=0
            for j in range(len(citations)):
                if i<=citations[j]:
                    count+=1
                if count==i:
                    curr=i
                    break
        return curr

        