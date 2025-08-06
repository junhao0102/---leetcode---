class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        return min(len(candyType) // 2, len(set(candyType)))


sol = Solution()

print(sol.distributeCandies([1, 1, 2, 2, 3, 3]))  # return 3
print(sol.distributeCandies([1, 1, 2, 3]))  # return 2
print(sol.distributeCandies([6, 6, 6, 6]))  # return 1
