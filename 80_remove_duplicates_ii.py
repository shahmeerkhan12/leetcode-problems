class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        // optimized solution
        n = len(nums)
        // basic/initial check for immediate exit
        if n <= 2:
            return n
        valid_elements = 2
        for cur in range(2,n):
            if nums[valid_elements-2] != nums[cur]:
                nums[valid_elements] = nums[cur]
                valid_elements += 1
        return valid_elements
