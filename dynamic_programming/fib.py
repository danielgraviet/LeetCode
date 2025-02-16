class Solution(object):
    def fib_dp(self, k):
        # check for edge cases
        if k <= 1:
            return 1
        
        # 1 1 2 3 5 8 13
        fib = [0] * (k + 1)
        fib[0] = 1
        fib[1] = 1
        
        # this is a solution using tabulation.
        # bottom up programming where we store solutions to sub problems. 
        for i in range(2, k + 1):
            fib[i] = fib[i-1] + fib[i-2]
            
        return fib[k]
    
    def fib(self, k):
        if k <= 1:
            return 1
        
        a, b = 1, 1
        for _ in range(2, k + 1):
            a, b = b, a + b
            
        return b
    
    def climingStairs(self, k):
        if k == 0:
            return 0
        
        if k == 1: 
            return 1
        
        dp = [0] * (k + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, k + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[k]
            
def main():
    sol = Solution()
    print(sol.fib_dp(5))
    print(sol.fib(5))
    print(sol.climingStairs(5))
    
if __name__ == "__main__":
    main()