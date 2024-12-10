class MinStack(object):
    def __init__(self):
        # Initialize your data structures here
        self.stack = []
        self.min_stack = []  # Keeps track of the minimums

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # if min stack is empty or the val is less than top of min stack, append. 
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
            
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
        


def main():
    # Example usage of MinStack
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.getMin())
    
    # Print the stack and the min_stack
    print("Stack contents:", min_stack.stack)
    print("Min stack contents:", min_stack.min_stack)

if __name__ == "__main__":
    main()
