class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        num = 0
        n = len(s)
        for i in range(n):
            if i + 1 < n and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                num -= roman_to_int[s[i]]
            else:
                num += roman_to_int[s[i]]
                
        return num
