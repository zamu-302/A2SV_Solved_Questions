class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res=[[0]*len(img[0]) for _ in range(len(img)) ]
        for i in range(len(img)):
            for j in range(len(img[0])):
                total=0
                count=0
                for r in range(i-1,i+2):
                    for c in range(j-1,j+2):
                        if 0<=r<len(img) and 0<=c<len(img[0]):
                            total+=img[r][c]
                            count+=1
                res[i][j]=total//count
        return res

        