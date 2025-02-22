class Solution(object):
    def knapsack(self, values, weights, capacity):
        # check for edge cases: 
        if len(values) != len(weights) or capacity < 0:
            raise ValueError
        
        # initialize an array
        dp = [0] * (capacity + 1)
        n = len(weights)
        
        # double for loop
        for i in range(n):
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
                
        return dp[capacity]
    
def main():
    sol = Solution()
    
    values = [1,3,4]
    weights = [4,3,2]
    capacity = 6
    
    print(sol.knapsack(values, weights, capacity))
    
if __name__ == "__main__":
    main()