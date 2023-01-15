class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        count = 0
        if s == "":
            return True
        for word in t:
            if word == s[count]:
                count += 1
            if count == len(s):
                return True

        return False

print(Solution().isSubsequence("abc","ahbgdc"))
print(Solution().isSubsequence("axc","ahbgdc"))
