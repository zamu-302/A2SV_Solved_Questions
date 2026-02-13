class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
       total=[]
       rows=len(mat)
       cols=len(mat[0])
       for n in range(rows+cols-1): 
           diagonal=[]
           for i in range(n + 1):
                j = n - i
                if 0 <= i < rows and 0 <= j < cols:
                    diagonal.append(mat[i][j])
           if n%2==0:
                diagonal.reverse()
           total.extend(diagonal)
            
       return total
