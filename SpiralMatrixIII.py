class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i,j=rStart,cStart
        moves=1
        new_moves=2
        res=[]
        twice=2
        di,dj=0,1
        while len(res)<(rows*cols):
            if -1<i<rows and -1<j<cols:
                res.append([i,j])
            i+=di
            j+=dj
            moves-=1
            if moves==0:
                di,dj=dj,-di
                twice-=1
                if  twice==0:
                    twice=2
                    moves=new_moves
                    new_moves+=1
                else:
                    moves=new_moves-1
        return res

        