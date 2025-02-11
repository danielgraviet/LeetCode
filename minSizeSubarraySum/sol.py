class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, summ, = 0, 0
        shortest = float('inf')
        n = len(nums)
        
        for r in range(n):
            summ += nums[r] # iterate through the array and add the numbers. 
            # if valid move left
             
            while(summ >= target):
                shortest = min(shortest, ((r - left) + 1))
                summ -= nums[left]
                left += 1
            
        return shortest
            
    

def main():
    sol = Solution()
    arr = [2,3,1,2,4,3]
    target = 7
    print(sol.minSubArrayLen(target, arr))
    
if __name__ == "__main__":
    main()