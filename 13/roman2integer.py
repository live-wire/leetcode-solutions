class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        greater = False
        for i in range(len(s) - 1, 0, -1):
            if greater:
                greater = False
                continue
            if roman2int[s[i]] > roman2int[s[i-1]]:
                res += (roman2int[s[i]] - roman2int[s[i-1]])
                greater = True
            else:
                res += roman2int[s[i]]
        return res if greater else res + roman2int[s[0]]
             
