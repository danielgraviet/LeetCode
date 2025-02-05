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
        
            

def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring('pwwek'))

if __name__ == "__main__":
    main()