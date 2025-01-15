class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # each letter in pattern maps to a unique word in s

        # Main Logic # 
        # start with the characters in pattern, and create a dictionary
        # split up s into list of words. 
        wordList = s.split()
        char_to_word = {}
        word_to_char = {} 
        for char, word in zip(pattern, wordList):
            if char in char_to_word:
                if word_to_char[word] != char:
                    return False
            
            if word in word_to_char:
                if char_to_word[char] != word:
                    return False
              
            # dict[char from pattern] = word in s
            char_to_word[char] = word
            word_to_char[word] = char
                
        return True
        
def main():
    sol = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(sol.wordPattern(pattern, s))


if __name__ == "__main__":
    main()