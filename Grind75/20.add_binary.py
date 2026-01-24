class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry > 0:
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0
            sum = digitA + digitB + carry

            result = str(sum % 2) + result
            carry = sum // 2
            i -= 1
            j -= 1
        return result


solution = Solution()

print(solution.addBinary("11", "1"))
print(solution.addBinary("1101", "1011"))
