class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        old = image[sr][sc]
        if old == color:
            return image

        m = len(image)
        n = len(image[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != old:
                return
            image[i][j] = color

            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

        dfs(sr, sc)
        return image


solution = Solution()

print(solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(solution.floodFill([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1, 1, 2))
print(solution.floodFill([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1, 1))
