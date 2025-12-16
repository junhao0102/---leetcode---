class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        Brackets = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
    
        stack = [] # 放期望的右括號

        for char in s:
            if char in Brackets:
                stack.append(Brackets[char])
            else:
                # 右括號先出現
                if not stack:
                    return False
                if char != stack.pop():
                    return False

        return not stack


solution = Solution()

print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([])"))
print(solution.isValid("([)]"))
