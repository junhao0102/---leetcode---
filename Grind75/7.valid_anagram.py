class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sDict = {}
        tDict = {}

        for char in s:
            if char not in sDict:
                sDict[char] = 1
            else:
                sDict[char] += 1

        for char in t:
            if char not in tDict:
                tDict[char] = 1
            else:
                tDict[char] += 1

        if len(sDict) != len(tDict):
            return False

        for key in sDict:
            if key not in tDict or sDict[key] != tDict[key]:
                return False

        return True


class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))

        return sortedS == sortedT


solution = Solution2()

print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
