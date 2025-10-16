'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """    
        def repeat(cur, open, close):
            
# check if the cur.len == 2 * n, simply quit
            if(len(cur) ==  2 * n):
                result.append(cur)
                return

# any room for adding more open parenthesis
            if open < n:
                repeat(cur + "(", open+1, close)
            
# any room for adding closing parenthesis
            if close < open :
                repeat(cur + ")",open, close+1)

        result = []
        repeat("",0,0)
        return result