class Solution(object):
    def evalRPN(self, tokens):
        num_stack = []
        result = 0
        for item in tokens:
            if item not in "+-/*":
                num_stack.append(int(item))
            else:
                a = num_stack.pop()
                b = num_stack.pop()
                if item == "+":
                    result = a + b
                    num_stack.append(result)
                if item == "*":
                    result = a * b
                    num_stack.append(result)
                if item == "-":
                    result = b - a
                    num_stack.append(result)
                if item == "/":
                    result = b / a
                    num_stack.append(int(result))
        return num_stack[0]
        
            
    
def main():
    solution = Solution()
    print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/","*","17","+","5","+"]))
    
if __name__ == "__main__":
    main()