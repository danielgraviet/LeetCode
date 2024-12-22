class Solution(object):
    def fib(self, n):
        if n <= 0:
            raise ValueError
        if n == 1:
            return 1
        
        a, b = 1, 1
        for i in range(1, n - 1):
            a, b = b, a + b
        return b
        
        # 1 1 2 3 5 8 

def main():
    sol = Solution()
    print(sol.fib(3))

if __name__ == "__main__":
    main()