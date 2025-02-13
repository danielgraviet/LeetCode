from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        maxNum = 0
        resultList = []
        
        # slide the window over
        for right in range(k, len(nums) + 1):
            window = nums[left:right]
            left += 1
            maxNum = max(window)
            resultList.append(maxNum)
            
        return resultList
    
    def optimizedMaxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        result = []
        maxSum = max(nums[:k])
        result.append(maxSum)
        
        
        for right in range(k, len(nums)):
            if nums[left] == maxSum:
                maxSum = max(nums[left + 1: right + 1])
            else:
                maxSum = max(maxSum, nums[right])
            left += 1
            result.append(maxSum)
            
        return result
            
                
    
    
        

def main():
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    
    print(sol.maxSlidingWindow(nums, k))
    print(sol.optimizedMaxSlidingWindow(nums, k))
    
if __name__ == "__main__":
    main()