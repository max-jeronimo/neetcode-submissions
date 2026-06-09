class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        low_s = s.lower()
        low_t = t.lower()
        if sorted(low_s) == sorted(low_t):
            return True
        else:
            return False