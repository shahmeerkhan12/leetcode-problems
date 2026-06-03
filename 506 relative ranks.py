class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # take a var to save results, remember to give a size equal to len of score
        n = len(score)
        ans = [""] * n

        # 1. turn scores and their indices into a max_heap

        # creating a tuple to track score against indices
        max_heap = [(-s,i) for i,s in enumerate(score)]
        # now creating a heap
        heapq.heapify(max_heap) 

        # 2. iterate the max_heap  and

        # ranking tracker
        rank = 1
        while max_heap:

            # get the original index of the score

            _ , orig_indx = heapq.heappop(max_heap)

            if rank==1:
                ans[orig_indx] = "Gold Medal"
            elif rank==2:
                ans[orig_indx] = "Silver Medal"
            elif rank==3:
                ans[orig_indx] = "Bronze Medal"
            else:

                ans[orig_indx] = str(rank)

            rank += 1

        return ans
