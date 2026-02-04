#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        count_a=Counter(a)
        count_b=Counter(b)
        return count_a>=count_b
        
        
        # Your code here
        
    
    
    
