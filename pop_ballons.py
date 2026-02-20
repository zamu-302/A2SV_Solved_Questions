class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0],x[1]))
        arrow=1
        maxi=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]>maxi:
                arrow+=1
                maxi=points[i][1]
            else:
                maxi=min(maxi,points[i][1])
        return arrow
            
        