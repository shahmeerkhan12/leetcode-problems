class solution:

# two hash_map 
# complexity O(n)

   def two_sum(self,nums,targt):
      # declare an empty dict, and assign nums value to it
      numMap = {}
      for i, num in enumerate(nums):
         numMap[num]=i
      for i, num in enumerate(nums):
         # print(i,num)
         complement = target-num
         if complement in numMap and  numMap[complement] != i:
            return [i, numMap[complement]]     


nums = [4,2,9,3] # list
target = 6  # element to found after adding two list elements
s1 = solution()
print(s1.two_sum(nums,target))      
            