class program:
   def cal_score(self,inst,values):
      
      visited = set()
      score = 0
      
      for i in inst:
         if i not in visited:
            if inst[i]=="add":
               score += values[i]
               i+1
               visited.add(i)
            else:
               i += values[i]
               visited.add(i)
      return score
        
instruction = ["add","add","jump","add","jump"]
value = [1,2,-1,2,-2,8]
p1 = program()
# print the return value
result = p1.cal_score(instruction,value)


