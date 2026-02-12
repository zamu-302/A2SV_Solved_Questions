import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        j=len(matrix)
        res=[]
        for i in range(len(matrix[0])):
            res.append([matrix[k][i] for k in range(j)])
        return res


    

        