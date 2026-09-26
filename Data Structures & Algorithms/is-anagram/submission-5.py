class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_t = ''.join(sorted(t))
        sorted_s = ''.join(sorted(s))
        if len(s) == len(t):
            for i in range(len(s)):
                if sorted_s[i] == sorted_t[i]:
                    continue
                return False
            return True
        return False

                    
                    