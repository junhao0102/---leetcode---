# brute force
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0

        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]

        return maxProfit

# 從賣點往回推看最低買點
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        maxProfit = 0

        for i in range(0, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy:
                maxProfit = max(maxProfit, prices[i] - buy)

        return maxProfit


solution = Solution2()

print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
print(solution.maxProfit([1, 2]))