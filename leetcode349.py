class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 建立兩個空集合：set1 用來存 nums1 的不重複元素，set2 用來存交集結果
        set1 = set({})
        set2 = set({})

        # 將 nums1 的所有元素加入 set1
        for item1 in nums1:
            if item1 not in set1:
                set1.add(item1)
            else:
                continue

        # 遍歷 nums2，檢查每個元素是否存在於 set1，如果有就加入 set2
        for item2 in nums2:
            if item2 in set1:
                set2.add(item2)
            else:
                continue

        # 將結果轉為陣列回傳
        return list(set2)


sol = Solution()

print(sol.intersection([1,2,2,1],[2,2])) # return [2]
print(sol.intersection([4,9,5],[9,4,8,9,4])) # return [9,4]