class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i,num in enumerate(numbers):
            comp = target - num
            if comp in dict and dict[comp] != i:
                return [dict[comp]+1,i+1]

            dict[num] = i
