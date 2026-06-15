class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort( key = lambda x : x[0])
        cur = left

        for start,end in ranges:

            if start <= cur:

                cur = max(cur,end+1) # 3

            if cur>right:
                return True
           
        return cur>right
