# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""
#Input: strs = ["flower","flow","flight"]
#Output: "fl"


class Solution:
    def longgestCommonPrefix(self, strs: list[str]) -> str:

        # Tim ra tu co do dai ngan nhat
        n = min(len(strs[x]) for x in range(len(strs)))
        res = ''

        #
        for i in range(n):
            # lay charactor dau tien cua vi tri 0
            c = strs[0][i]
            # lay vi tri dau vien cua vi tri 1, 2,....
            for j in range(1, len(strs)):
                # so sanh
                if c != strs[j][i]:
                    # neu k trung thi return res luon
                    return res
            res = res + c
        return res


a = Solution()
print(a.longgestCommonPrefix(['flower', 'flow', 'flight', 'flo']))
