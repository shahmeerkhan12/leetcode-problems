class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
# let's find the possible rectangles sizes
        for i in range(n):
# lets say current element is the max possible height for a recatangle
            cur = heights[i]

# now traverse left if element/bar is higher than heights[i]
            j = i-1
            while j>=0 and heights[j]>=heights[i]:
                cur += heights[i]
                j -= 1
# now traverse to the left side for element higher than or equal to the heights[i]
            j = i + 1
            while j<n and heights[j] >= heights[i]:
                cur += heights[i]
                j += 1

            res = max(cur, res)

        return res
            
