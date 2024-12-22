class Solution(object):
    def rotate(self, nums, k):
        if k == 0:
            return nums
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return nums
        
        n = len(nums)
        k = k % n

        nums.reverse()

        nums[k:] = reversed(nums[k:])
        nums[:k] = reversed(nums[:k])
        return nums

def main():
    sol = Solution()
    print(sol.rotate([1,2,3,4,5,6], 1))
    numList = [1,2,3,4,5]
    print(numList[3:])
    

if __name__ == "__main__":
    main()