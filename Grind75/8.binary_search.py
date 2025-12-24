class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middleIndex = (left + right) // 2
            middleValue = nums[middleIndex]

            if target < middleValue:
                right = middleIndex - 1

            if target > middleValue:
                left = middleIndex + 1

            if target == middleValue:
                return middleIndex

        return -1


solution = Solution()

print(solution.search([-1, 0, 3, 5, 9, 12], 9))
print(solution.search([-1, 0, 3, 5, 9, 12], 2))
