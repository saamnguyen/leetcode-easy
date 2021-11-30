class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1 = ""
        for i in str(x):
            s1 = i + s1
            print(i)
            print(s1)
        return str(x) == str(s1)

a = Solution()
print(a.isPalindrome(1234))