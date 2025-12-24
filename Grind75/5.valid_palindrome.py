class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum() :
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[right].lower() != s[left].lower():
                return False

            left += 1
            right -= 1

        return True


solution = Solution()

print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))
