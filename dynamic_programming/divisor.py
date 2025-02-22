class Solution(object):
    def divisorGame(self, n):
        dp = [False] * (n + 1)
        for i in range(2, n + 1):
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        
        return dp[n]
    
def main():
    
    sol = Solution()
    print(sol.divisorGame(2))
    
    
if __name__ == "__main__":
    main()