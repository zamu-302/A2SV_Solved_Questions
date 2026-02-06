from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count=Counter(chars)
        ans=0
        for word in words:
            word_counter=Counter(word)
            if word_counter<=char_count:
                ans+=len(word)
        return ans