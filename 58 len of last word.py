class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count from the last
        # if space: don't count it
        # else count

        last_word = s.split()[-1]

        return len(last_word)
