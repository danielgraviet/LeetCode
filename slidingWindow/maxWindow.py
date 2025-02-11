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
        resultList = []
        
        # initialize the first window and max. 
        maxNum = max(nums[:k])
        resultList.append(maxNum)
        
        for right in range(k, len(nums)):
            # Check if the element that slid out was the max
            if nums[left] == maxNum:
                # find new max
                maxNum = max(nums[left + 1:right + 1])
            else:
                # Update max if the new element is greater
                maxNum = max(maxNum, nums[right])
                
            resultList.append(maxNum)
            left += 1
        
        return resultList
    
    
        

def main():
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    
    print(sol.maxSlidingWindow(nums, k))
    print(sol.optimizedMaxSlidingWindow(nums, k))
    
if __name__ == "__main__":
    main()