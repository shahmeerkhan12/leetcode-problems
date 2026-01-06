def sum_matrix(matrix):
   total_abs = sum(abs(item) for sublist in matrix for item in sublist)
   #smallest absolute value in the matrix
   min_abs = min(abs(x) for sublist in matrix for x in sublist)
   neg_count = sum(1 for row in matrix for item in row if item<0)
   if neg_count%2 == 0:
      return total_abs
   return total_abs - 2*min_abs
  

matrix = [[1,-1],[-1,1]]
m2 = [[1,2,3],[-1,-2,-3],[1,2,3]]
print(sum_matrix(matrix))
print(sum_matrix(m2))



