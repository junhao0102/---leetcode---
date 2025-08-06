class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        # 當位數超過 1 計算每位數字總和
        while len(num) > 1:
            result = 0
            for char in num:
                result += int(char)
            num = str(result)
        return int(num)


sol = Solution()

print(sol.addDigits(38)) # return 2
print(sol.addDigits(0)) # return 0
