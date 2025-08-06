class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        result = 0
        for char in stones:
            if char in jewels:
                result += 1
        return result


sol = Solution()

print(sol.numJewelsInStones("aA", "aAAbbbb"))  # return 3
print(sol.numJewelsInStones("z", "ZZ"))  # return 0
