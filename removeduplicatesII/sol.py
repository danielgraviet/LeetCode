class Solution(object):
    def removeDuplicates(self, nums):
        j, count = 1, 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] == nums[i]
                j += 1
        
        return j

def main():
    sol = Solution()
    print(sol.removeDuplicates([1,2,2,2,3]))
    
if __name__ == "__main__":
    main()