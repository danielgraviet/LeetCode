class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use a dictionary
        num_map = {}
        # map over each element, and keep track in indicies
        for i, x in enumerate(nums):
            # caluclate a complement number
            complement = target - x
            # search for comp. num, if found return indices
            if complement in num_map:
                return [num_map[complement], i]
            num_map[x] = i
        return []
        
def main():
    solution = Solution()
    print(solution.twoSum([2,11,5,7], 9))
    
if __name__ == "__main__":
    main()