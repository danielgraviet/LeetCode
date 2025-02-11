from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left, currentSum, maxSum = 0,0,0
        numSet = set()
        n = len(nums)
        
        for right in range(n):
            while nums[right] in numSet:
                numSet.remove(nums[left])
                currentSum -= nums[left]
                left += 1
                
            numSet.add(nums[right])
            currentSum += nums[right]
            
            if right - left + 1 == k:
                maxSum = max(maxSum, currentSum)
                numSet.remove(nums[left])
                currentSum -= nums[left]
                left += 1
                
        return maxSum
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return 0
        
        windowSum = sum(nums[:k])
        left = 0
        maxWindow = windowSum / k
        
        for right in range(k, len(nums)):
            windowSum = windowSum + nums[right] - nums[left]
            windowAvg = windowSum / k
            maxWindow = max(maxWindow, windowAvg)
            left += 1
        
        return maxWindow
    
    def slidingTemplate(self, nums: List[int], k: int) -> float:
        left = 0
        result = 0 # Or float('-inf')/float('inf') depending on the problem
        window_sum = 0

        for right in range(len(nums)):
            # Add the right element to the window
            window_sum += nums[right]
            
            # Check if window size is equal to k
            if right - left + 1 == k:
                result = max(result, window_sum)  # or any condition you're solving for
                
                # Slide the window: remove left element
                window_sum -= nums[left]
                left += 1
                
        return result
    
    def maxProfit(self, nums: List[int]) -> int:
        left = 0
        maxProf = 0
        
        for right in range(1, len(nums)):
            profit = nums[right] - nums[left]
            if profit > 0:
                maxProf = max(maxProf, profit)
            else: 
                left = right
        return maxProf
        
        
        
    
        
def main():
    sol = Solution()
    print(sol.maximumSubarraySum([1,2,2], 2))
    print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
    print(sol.slidingTemplate([2,1,5,1,3,2], 3))
    
    print(sol.maxProfit([7,1,2,4,0,6,5]))
    # answer should be 5
    
    
if __name__ == "__main__":
    main()