from typing import List


class Solution:
    def stockPrices(self, nums: List[int], k: int) -> int:
        # find first window
        windowSum = sum(nums[:k])
        maxSum = windowSum
        
        for right in range(k, len(nums)):
            windowSum = windowSum + nums[right] - nums[right - k]
            maxSum = max(maxSum, windowSum)
            
        return maxSum
    
    def longestSubstringWithKCharacters(self, nums, k):
        return nums
    
def main():
    sol = Solution()
    stocks = [10, 230, 32420, 2343234, 1213, 123643]
    k = 3
    print(sol.stockPrices(stocks, k))
    
    characters = "aabacbebebe"
    print(sol.longestSubstringWithKCharacters(characters, k))
    
    
if __name__ == "__main__":
    main()