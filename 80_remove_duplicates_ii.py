class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        valid_elements = 2
        for cur in range(2,len(nums):
            if nums[valid_elements-2] != nums[cur]:
                nums[valid_elements] = nums[cur]
                valid_elements += 1
        return valid_elements
