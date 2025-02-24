class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVowel, vowelCount = 0, 0
        vowels = "aeiou"
        
        # init first window and count vowels
        window = s[:k]
        for char in window:
            if char in vowels:
                vowelCount += 1
                
        if vowelCount == k:
            return vowelCount
                
        maxVowel = vowelCount
                
        for right in range(k, len(s)):
            if s[right] in vowels:
                vowelCount += 1
            if s[right - k] in vowels:
                vowelCount -= 1
            maxVowel = max(maxVowel, vowelCount)
            
            if maxVowel == k:
                return maxVowel
        
        return maxVowel
        
        
def main():
    sol = Solution()
    print(sol.maxVowels("aeiou", 2))
    
if __name__ == "__main__":
    main()