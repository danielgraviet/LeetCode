class Solution(object):
    def maxProfit(self, prices):
        if (len(prices) <= 1):
           return 0
       
        minPrice = float('inf')
        maxProfit = 0
       
        for num in prices:
            if num < minPrice:
               minPrice = num
            else:
                profit = num - minPrice
                maxProfit = max(maxProfit, profit)
               
        return maxProfit
def main():
    solution = Solution()
    prices = [1,7,6,8,2,1]
    print(solution.maxProfit(prices))
if __name__ == "__main__":
    main()