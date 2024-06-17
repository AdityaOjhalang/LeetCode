class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for j in range(len(t)):
            if  i < len(s) and s[i] == t[j]:
                i += 1

        if i == len(s):
            return True
        else:
            return False
