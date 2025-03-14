class Solution(object):
    def fib(self, num):
        if num < 0:
            return "Error"
        if num == 1:
            return 1
        
        a,b = 1, 1
        for _ in range(2, num):
            a, b = b, a + b
        
        return b
        
        
def main():
    solution = Solution()
    num = 7
    print(solution.fib(num))

if __name__ == "__main__":
    main()