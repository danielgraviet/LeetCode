class Solution(object):
    def majorityElement(self, nums):
        dict = {}
        threshold = len(nums) // 2
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
            if (dict[num] > threshold):
                return num
        
        return 0
    
    def solution2(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]

def main():
    solution = Solution()
    print(solution.majorityElement([6,5,5]))
    print(solution.solution2([6,5,5]))
    print(3//2)
    
if __name__ == "__main__":
    main()