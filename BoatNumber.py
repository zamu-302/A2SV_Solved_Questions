class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left=0
        right=len(people)-1
        people.sort()
        count=0
        while left<=right:
            if people[right]==limit:
                right-=1
                count+=1
            elif left!=right and people[left]+people[right]<=limit:
                count+=1
                left+=1
                right-=1
            else:
                right-=1
                count+=1
            
        return count

        