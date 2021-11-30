class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        rev = 0
        while n > 0:
            dig = n % 10
            rev = rev * 10 + dig
            n = int(n/10)
        if ( x == rev):
           return True
        else:
           return False
a = Solution()
print(a.isPalindrome(12))