s = "- 042"
output = 42



class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and (s[i] == '+' or s[i]== '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        num = 0
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit

            if sign * num <= INT_MIN:
                return INT_MIN
            
            if sign * num >= INT_MAX:
                return INT_MAX

            i += 1
        return sign * num



        