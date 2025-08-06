class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 用字典記錄 nums1 中每個元素出現的次數
        map1 = dict({})
        result = []

        # 建立數字及出現次數的 map
        for item in nums1:
            if item not in map1:
                map1[item] = 1
            else:
                map1[item] += 1

        # 遍歷 nums2，如果元素在 map1 中且次數 > 0，就加入結果並減少次數
        for num in nums2:
            if num not in map1:
                continue
            if map1[num] > 0:
                result.append(num)
                map1[num] -= 1

        return result


sol = Solution()

print(sol.intersect([1, 2, 2, 1], [2, 2]))  # return [2,2]
print(sol.intersect([4, 9, 5], [9, 4, 8, 9, 4])) # return [9,4]
