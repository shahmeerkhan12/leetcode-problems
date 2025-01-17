class solution:

# the brute-force technique
# complexity O(n)^2

   def two_sum(self,nums,targt):
     
      found = False
     
      for i in range(len(nums)):
         
         for j in range(len(nums)):
            if(nums[i]+nums[j]==target):
               found = True
               break
       
         if(found):
            return i,j

nums = [1,2,3,4] # list
target = 7  # element to found after adding two list elements
s1 = solution()
print(s1.two_sum(nums,target))      
            