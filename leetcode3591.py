import math 

class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        # 建立各個數字與出現次數的 map
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        # 遍歷 map 查看是否有出現質數的
        for item in map:
            if self.isPrime(map[item]):
                return True
        return False
    # 檢查是否為質數
    def isPrime(self,n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    

sol = Solution()

print(sol.checkPrimeFrequency([1,2,3,4,5,4])) # return True
print(sol.checkPrimeFrequency([1,2,3,4,5])) # return False
print(sol.checkPrimeFrequency([2,2,2,4,4])) # return True
