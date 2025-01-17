class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sort the array
        # loop through items, see if one item is equal to the next for all of them. 
        if not nums:
            return False
        
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
            
        return False
        
def main():
    sol = Solution()
    print(sol.containsDuplicate([1,1]))
    
if __name__ == "__main__":
    main()