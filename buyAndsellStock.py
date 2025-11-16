def maxProfit(buy: list[int]):
   left, right = 0,1
   maxProf = 0

   while right < len(buy):

      if buy[left] < buy[right]:
         profit = buy[right] - buy[left]
         maxProf = max (maxProf,profit)
      else:
         left = right
      right += 1
   return maxProf


stock_price = [7,1,2,7,3,5]
print(maxProfit(stock_price))