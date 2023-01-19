class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """

        first = ""
        second = ""
        third = ""

        for ch in firstWord: first += str(ord(ch.lower()) - 97)
        for ch in secondWord: second += str(ord(ch.lower()) - 97)
        for ch in targetWord: third += str(ord(ch.lower()) - 97)

        return int(first) + int(second) == int(third)


print(Solution().isSumEqual("aaa", "a", "aab"))