class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substrings = []  # List to store lengths of substrings
        n = len(s)       # Length of the string

        for i in range(n):  # Start a new substring from each character
            char_map = {}   # Map to store characters of the current substring
            for j in range(i, n):  # Build the substring
                if s[j] in char_map:  # Duplicate found
                    break
                char_map[s[j]] = True
            substrings.append(len(char_map))  # Store the length of the current substring

        return max(substrings) if substrings else 0  # Return the max length

def main():
    solution = Solution()
    print(solution.lengthOfLongestSubstring("ABCABCAA"))
    
if __name__ == "__main__":
    main()