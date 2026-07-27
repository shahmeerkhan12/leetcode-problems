from itertools import permutations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = [list(p) for p in permutations(nums)]

        perm = []
        for item in res:
            if item not in perm:
                perm.append(item)

        return perm
