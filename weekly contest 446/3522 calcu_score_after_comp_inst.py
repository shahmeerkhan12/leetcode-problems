class program:
   def cal_score(self,inst,values):
      
      visited = set()
      n = len(inst)
      score = 0
      i=0
       
      while (0 <= i < n and i not in visited):  
            visited.add(i)
            if(inst[i]=='add'): 
               score += values[i]
               i += 1
            elif (inst[i]=='jump'):
               i = i + values[i]
            else:
               print("invalid instruction")
               break
      return score
        
instruction = ["add","add","add","add","jump"]
value = [1,2,4,3,3]
p1 = program()
print(p1.cal_score(instruction,value))


