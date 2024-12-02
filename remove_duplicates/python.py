class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = list(set(nums))
        length = len(new_nums)
        for value in range(length):
            nums[value] = new_nums[value]
        return len(nums[:length])
        
if __name__ == "__main__":
    nums = [1, 1, 2]
    solution = Solution()
    print(solution.removeDuplicates(nums))