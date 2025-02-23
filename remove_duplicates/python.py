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
    
    def solution2(self, nums):
        n = len(nums)
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    
    def dictionarySolution(self, nums):
        unique_dict = {}
        write_index = 0
        for num in nums:
            if num not in unique_dict:
                unique_dict[num] = True
                nums[write_index] = num
                write_index += 1
        return write_index
        
if __name__ == "__main__":
    nums = [1, 1, 2]
    nums2 = [1, 1, 2, 2, 3, 4, 4]
    solution = Solution()
    print(solution.removeDuplicates(nums))
    print(solution.solution2(nums2))
    print(nums2)
    print(solution.dictionarySolution(nums2))