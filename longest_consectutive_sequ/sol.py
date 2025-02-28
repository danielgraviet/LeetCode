class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        numList = list(numSet)
        numList.sort()
        count, maxSequence = 0, 0
        
        if not numList:
            return 0
        if len(numList) == 1:
            return 1
        
        for i in range(len(numList) - 1):
            if numList[i + 1] == numList[i] + 1:
                count += 1
            else:
                maxSequence = max(maxSequence, count)
                count = 0
        maxSequence = max(maxSequence, count)
        return maxSequence + 1
        
def main():
    nums = [0,3,7,2,5,8,4,6,0,1]
    sol = Solution()
    print(sol.longestConsecutive(nums))

if __name__ == "__main__":
    main()