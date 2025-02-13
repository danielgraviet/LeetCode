class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left, longest = 0, 0
        n = len(s)
        letters = set()
        
        for r in range(n):
            while s[r] in letters:
                letters.remove(s[left])
                left += 1
            window = (r - left) + 1
            letters.add(s[r])
            longest = max(longest, window)
            
        return longest
    
    def maxSubarray(self, nums, k):
        l = 0
        windowSum = sum(nums[:k])
        windowAvg = windowSum / k
        maxAvg = windowAvg
        
        for right in range(k, len(nums)):
            windowSum = windowSum - nums[right - k] + nums[right]
            windowAvg = windowSum / k
            maxAvg = max(maxAvg, windowAvg)
        
        return maxAvg
        
def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring('pwwek'))
    
    nums = [1,3,4,5,12,4,5,1,2,3]
    k = 2
    
    print(sol.maxSubarray(nums, k))

if __name__ == "__main__":
    main()