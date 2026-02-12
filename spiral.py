class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(given):
            if not given:
                return []
            x=given.pop(0)
            rotated = list(zip(*given))[::-1]
            rotated=[list(row) for row in rotated]
           
            return x+spiral(rotated)
        res=spiral(matrix)
        return res
     
