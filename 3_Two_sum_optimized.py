# optimized solution for Two Sum leetcode problem
# create an empty dict
# for each number in the list do the following
# 1 : calculate the complement i.e complement = target - num
# 3 : if complement exist in the dict: return the indices
# 4 : otherwise the current number and index is added to the dict
# 5 : if no pair sums to the target an empty list is returned

class Solution:

   def twoSum(self, nums, target):
      numsDict= {}
      for i, num in enumerate(nums):
         complement = target - num
         if complement in numsDict:
            return[ i,numsDict[complement]]
         numsDict[num]=i

      return []
   
listt = [20,30,80,90]
target_num= 50
s1 = Solution()
print(s1.twoSum(listt,target_num))