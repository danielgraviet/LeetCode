class Solution():
    def evalRPN(self, tokens: list[str]) -> int:
        num_stack = []
        result = 0
        for item in tokens:
            if item.isdigit():
                num_stack.append(item)
            else:
                if item == "+":
                    result: int = int(num_stack[0]) + int(num_stack[1])
                    num_stack.clear()
                    num_stack.append(result)
                if item == "*":
                    result: int = int(num_stack[0]) * int(num_stack[1])
                    num_stack.clear()
                    num_stack.append(result)
                if item == "-":
                    result: int = int(num_stack[0]) - int(num_stack[1])
                    num_stack.clear()
                    num_stack.append(result)
        return result
            
    
def main():
    solution = Solution()
    print(solution.evalRPN(["1", "2", "+", "3", "*", "4", "-"]))
    
if __name__ == "__main__":
    main()