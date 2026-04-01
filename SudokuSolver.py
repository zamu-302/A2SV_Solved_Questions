class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        box=[set() for i in range(9)]
        empty=[]

        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val!=".":
                    row[i].add(val)
                    col[j].add(val)
                    box[(i // 3) * 3 + (j // 3)].add(val)
                else:
                    empty.append((i,j))
        

        def dfs(index):
            if index==len(empty):
                return True
            

            r,c=empty[index]
            box_idx=((r//3)*3+(c//3))

            for num in "123456789":
                if num not in row[r] and num not in col[c] and num not in box[box_idx]:
                    board[r][c]=num
                    row[r].add(num)
                    col[c].add(num)
                    box[box_idx].add(num)
                    if dfs(index+1):
                        return True
                    board[r][c]="."
                    row[r].remove(num)
                    col[c].remove(num)
                    box[box_idx].remove(num)
            return False
        dfs(0)

                
                    

       
      
        
        