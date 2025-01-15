class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s = s[::-1]
        return ' '.join(s)
        
        
def main():
    sol = Solution()
    print(sol.reverseWords("The sky is blue"))
    
    string = "     The     sky     is blue    "
    result = ""
    string = string.split()
    reversed_string = (string[::-1])
    for i, word in enumerate(reversed_string):
        result += "".join(word)
        if i != len(reversed_string) - 1:
            result += " "

    print(result)

if __name__ == "__main__":
    main()