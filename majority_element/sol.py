class Solution(object):
    def majorityElement(self, nums):
        dict = {}
        threshold = len(nums) // 2
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
            if (dict[num] > threshold):
                return num
        
        return 0

def main():
    solution = Solution()
    print(solution.majorityElement([6,5,5]))
    
if __name__ == "__main__":
    main()