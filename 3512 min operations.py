"""   
define a function that takes an int array, and another int K,
and then it should return the minimum number of operations(array[i]-1) performed
while sum(array)%K is zero.
"""
def min_operations(nums:list(int),K:int):
   # we know that the remainder would be the number of operations required, so
   return sum(nums) % K
   # return the total number of operations

min_operations([2,3,4],4)

