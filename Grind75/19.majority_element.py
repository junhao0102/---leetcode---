class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        max = 0
        major = nums[0]
    
        for key in dict:
            if dict[key] > max:
                max = dict[key]
                major = key

        return major


solution = Solution()

print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
