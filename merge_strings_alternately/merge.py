class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        length = max(len(word1), len(word2))
        for i in range(length):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return result

def main():
    # Example usage of the Solution class
    solution = Solution()
    word1 = "AAA"  # Example input
    word2 = "BBB"  # Example input
    
    # Call the method (replace with actual problem-solving code later)
    print(solution.mergeAlternately(word1, word2))
    

if __name__ == "__main__":
    main()
