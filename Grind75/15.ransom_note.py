class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNoteDict = {}
        magazineDict = {}

        for char in ransomNote:
            if char not in ransomNoteDict:
                ransomNoteDict[char] = 1
            else:
                ransomNoteDict[char] += 1

        for char in magazine:
            if char not in magazineDict:
                magazineDict[char] = 1
            else:
                magazineDict[char] += 1

        for key in ransomNoteDict:
            if key not in magazineDict:
                return False
            if ransomNoteDict[key] > magazineDict[key]:
                return False
        return True


solution = Solution()

print(solution.canConstruct("a", "b"))
print(solution.canConstruct("aa", "ab"))
print(solution.canConstruct("aa", "aab"))
