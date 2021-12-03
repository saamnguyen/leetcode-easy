# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = [0]

        for paren in s:
            print(stack)
            # print(stack)
            if paren in dic.values():
                stack.append(paren)
                print(stack)
            # pop se xoa chi muc 0 khi ==
            elif dic[paren] != stack.pop():
                return False

        return len(stack) == 1


a = Solution()
print(a.isValid("()"))
