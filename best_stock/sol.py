class Solution(object):
    def maxProfit(self, prices):
        return max(prices)
        
def main():
    solution = Solution()
    prices = [1,2,3,4]
    print(solution.maxProfit(prices))
if __name__ == "__main__":
    main()