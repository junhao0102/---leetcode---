class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        length = 0

        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                if dict[char] == 1:
                    dict[char] = 0
                    length += 2
                else:
                    dict[char] += 1
                    
        for key in dict:
            if dict[key] == 1:
                return length + 1
        return length


solution = Solution()
print(solution.longestPalindrome("a"))
print(solution.longestPalindrome("bb"))
print(solution.longestPalindrome("bananas"))
print(solution.longestPalindrome("abccccdd"))
