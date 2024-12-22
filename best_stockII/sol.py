class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        result = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                result += prices[i+1] - prices[i]
                
        return result
        
def main():
    sol = Solution()
    print(sol.maxProfit([1,2,3,4,5]))
    print(len([7,1,4,7,3,8]))

if __name__ == "__main__":
    main()