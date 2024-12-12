class Solution(object):
    def generateParentheses(self, num):
        parentheses = []
        res = []
        
        def recursive(openN, closedN):
            if openN == closedN == num:
                res.append("".join(parentheses))
            
            if openN < num:
                parentheses.append("(")
                recursive(openN + 1, closedN)
                parentheses.pop()
            
            if closedN < openN:
                parentheses.append(")")
                recursive(openN, closedN + 1)
                parentheses.pop()
                
        recursive(0,0)
        return res
    
def main():
    solution = Solution()
    print(solution.generateParentheses(2))
    
if __name__ == "__main__":
    main()
    
    