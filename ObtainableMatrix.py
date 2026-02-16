class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target:
            return True
        for i in range(4):
             mat = [list(x) for x in zip(*mat[::-1])]
             if mat==target:
                return True
        return False
             