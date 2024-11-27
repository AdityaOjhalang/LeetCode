class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [] , []

        def backtrack(open,close):

            if len(sol) == n*2:
                ans.append(''.join(sol))
                return
            
            if open < n:
                sol.append("(")
                backtrack(open+1,close)
                sol.pop()
            
            if open > close:
                sol.append(")")
                backtrack(open,close+1)
                sol.pop()
        backtrack(0,0)
        return ans
