class Solution:
    def romanToInt(self, s: str) -> int:
        char_dict = {'M': 1000, 'D': 500, 'C': 100,
                     'L': 50, 'X': 10, 'V': 5, 'I': 1}
        diff_dict = {'IV': 1, 'IX': 1, 'XL': 10,
                     'XC': 10, 'CD': 100, 'CM': 100}

        ans = 0

        for char in s:
            ans += char_dict[char]

        for i in range(len(s) - 1):
            char = s[i] + s[i + 1]
            if char in diff_dict:
                ans = ans - 2 * diff_dict[char]

        return ans


a = Solution()
print(a.romanToInt('IX'))
