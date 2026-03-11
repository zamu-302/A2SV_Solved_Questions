class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        event=[0]*(len(s)+1)
        for left,right,dire in shifts:
            if dire==0:
                event[left]+=-1
                event[right+1]+=1
            else:
                event[left]+=1
                event[right+1]+=-1
    
        for i in range(1,len(event)):
            event[i]+=event[i-1]
        event=event[:-1]
        ans=""
        print(event)
        for i in range(len(s)):
            shift = event[i]
            old = ord(s[i]) - ord('a')
            new = (old + shift) % 26
            ans += chr(new + ord('a'))
        return ans

        


        