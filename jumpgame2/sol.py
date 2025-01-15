class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter, maxReach = 0, 0
        for i, n in enumerate(nums):
            if i > maxReach:
                return 0
            maxReach = max(maxReach, i + n)
            counter += 1
            if maxReach + i >= len(nums):
                return counter
        return 0
    
    def correctSolution(self, nums):
        if len(nums) <= 1:
            return 0
        
        jumps, current_end, maxReach = 0, 0, 0
        for i in range(len(nums) - 1):
            maxReach = max(maxReach, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = maxReach
                if current_end >= len(nums) - 1:
                    break
        return jumps
        
def main():
    sol = Solution()
    print(sol.correctSolution([2,3,1,1,4]))


if __name__ == "__main__":
    main()