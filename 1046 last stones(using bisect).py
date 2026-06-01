import bisect
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        stones.sort()

        # do this until the len of max_heap is 1

        while len(stones)>1:

            y = stones.pop() 
            x = stones.pop() 
            

            # now follow the game instructions
       
        # 1. the condition if x==y, is done implicitly

        # 2. then implement if x!=y

            if x!=y:

                bisect.insort(stones,y-x)

    # 3. now return the last remaining element if exist else return 0

        return stones[0] if stones else 0
