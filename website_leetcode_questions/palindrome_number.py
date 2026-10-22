x = 121

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        if x != 0 and X % 10 == 0:
            return False
        org = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return org == reversed_num

        