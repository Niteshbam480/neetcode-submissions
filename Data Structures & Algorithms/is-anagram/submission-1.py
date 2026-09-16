class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        freq_char = [0]*26
        for i in range(len(s)):
            freq_char[ord(s[i])-ord('a')] +=1
            freq_char[ord(t[i])-ord('a')] -=1
        
        for i in freq_char:
            if i !=0:
                return False
        return True
