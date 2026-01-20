class Solution(object):
    def climbStairs(self, n, dict=None):
        """
        :type n: int
        :rtype: int
        """
        if dict is None:
            dict = {}

        if n == 1 or n == 2:
            return n

        if n in dict:
            return dict[n]

        dict[n] = self.climbStairs(n - 1, dict) + self.climbStairs(n - 2, dict)
        return dict[n]
