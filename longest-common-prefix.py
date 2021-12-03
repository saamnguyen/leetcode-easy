# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""
#Input: strs = ["flower","flow","flight"]
#Output: "fl"


# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         n = min([len(strs[x]) for x in range(len(strs))])
#         print(n)
#         res = ""

#         for i in range(n):
#             c = strs[0][i]
#             print(c)
#             for j in range(1, len(strs)):
#                 print(strs[j][i])
#                 if c != strs[j][i]:

#                     print(res + 'res')
#                     return res
#             res = res + c

#         return res

class Solution:
    def longgestCommonPrefix(self, strs: list[str]) -> str:
        n = min(len(strs[x]) for x in range(len(strs)))
        res = ''

        for i in range(n):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if c != strs[j][i]:
                    return res
            res = res + c
        return res


a = Solution()
print(a.longgestCommonPrefix(['flower', 'flow', 'flight', 'flo']))
