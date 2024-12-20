class Solution(object):
    def rotate(self, nums, k):
        # indexs get pushed the the right k times
        # if k gets out of bounds, it gets pushed to the front, makes a loop type
        if k == len(nums):
            return nums
        
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return nums

        n = len(nums)
        k = k % n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        return nums

def main():
    sol = Solution()
    print(sol.rotate([1,2], 1))
    print(len([1,2]))

if __name__ == "__main__":
    main()