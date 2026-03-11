class Solution:
    def decodeString(self, s: str) -> str:
        stk=[]
        ans=""
        for char in s:
            if char!= ']':
                stk.append(char)
            else:
                string=""
                while stk and stk[-1]!='[':
                    string=stk.pop()+string
                stk.pop()
                num=""

                while stk and stk[-1].isdigit():
                    num=stk.pop()+num
                string=string*int(num)
                
                stk.append(string)
        return "".join(stk)





        