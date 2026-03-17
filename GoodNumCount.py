import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=((10**9)+7)
        x=n/2
        x,y=math.ceil(x),math.floor(x)
        print(x,y)
        return (pow(5, x, mod) * pow(4, y, mod)) % mod
