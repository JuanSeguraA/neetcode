class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_len = 0
        start = 0

        for i, char in enumerate(s):
            while char in substring:
                substring.remove(s[start])
                start += 1
            substring.add(char)
            max_len = max(max_len, i - start + 1)

        return max_len