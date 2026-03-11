class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk=[]
        for i in range(len(logs)):
            if logs[i]=='../':
                if stk:
                    stk.pop()
                continue
            elif logs[i]=='./':
                continue
            else:
                stk.append(logs[i])
        return len(stk)