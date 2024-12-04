class Solution(object):
    def fibonacci(self, num):
        if num < 0:
            raise ValueError
        if num == 1:
            return 1
        
        a,b = 1, 1
        for _ in range(2, num):
            a, b = b, a + b
            
        return b
        
def main():
    solution = Solution()
    print(solution.fibonacci(7))
    

if __name__ == "__main__":
    main()