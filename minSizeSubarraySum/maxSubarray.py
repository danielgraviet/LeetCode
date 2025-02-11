class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        l, maxWindow = 0, 0
        windowSum = sum(nums[:k])
        maxWindow = windowSum / k

        for r in range(k, n):
            windowSum = windowSum - nums[l] + nums[r]
            windowAvg = windowSum / k
            maxWindow = max(maxWindow, windowAvg)
            l += 1
            
        return maxWindow
       
    
def main():
    sol = Solution()
    print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
    
if __name__ == "__main__":
    main()