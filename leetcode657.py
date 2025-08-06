class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # 建立初始 map :上下左右次數皆為 0
        map = {"U": 0, "D": 0, "R": 0, "L": 0}

        # 遍歷 moves 計算各個方位次數
        for char in moves:
            map[char] += 1

        # 判斷上次數是否等於下
        if map["D"] != map["U"]:
            return False

        # 判斷左次數是否等於右
        if map["L"] != map["R"]:
            return False

        return True


sol = Solution()

print(sol.judgeCircle("UD"))  # true
print(sol.judgeCircle("LL"))  # false
