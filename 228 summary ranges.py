class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        lnth = len(nums)
        while i < lnth:
            start = nums[i]

            while i+1 < lnth and nums[i] + 1 == nums[i+1]:

                i += 1

            if start != nums[i]:

                res.append(str(start) + "->" + str(nums[i]))

            else:
                res.append(str(start))
            i += 1

            
        return res
