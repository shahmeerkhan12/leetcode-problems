target,nums = 5, [2,3,4,5]
# the combinations tha sum up to the target
"""
1.combinations = []
2. start from the beggining value of the list:
2a.   if i == target: add to combination
3.    start from the second value:
3a.      if prev + next == target:
4.         add prev and next to the combination
5.       else if 2*prev + next == target:
6.          add prev,prev,next to combination

7.return combinations
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def bk(remain,comb,start):
            if remain == 0:
                result.append(list(comb))
                return
            elif remain < 0:
                return
            for i in range (start, len(candidates)):
                comb.append(candidates[i])
                bk(remain - candidates[i],comb, i)
                comb.pop()
        result = []
        bk(target,[],0)
        return result

        