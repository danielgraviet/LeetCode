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
        
def main():
    sol = Solution()
    print(sol.maximumSubarraySum([1,2,2], 2))
    
    
if __name__ == "__main__":
    main()