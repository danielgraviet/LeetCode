class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #
        i, length = len(s) - 1, 0
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
    
    def pythonicSolution(self, s):
        #strip the string of leading/trailing spaces
        s.strip()
        if s.strip():
            stringList = s.split()
            return len(stringList[-1])
        else:
            return 0

def main():
    solution = Solution()
    string = "  this is danny  "
    print(solution.lengthOfLastWord(string))
    print(solution.pythonicSolution(string))
    
    print(string.strip()) #this removes trailing 0's
    if string.strip():
        print("The string is not empty!")
    else:
        print("The string is empty.")

    stringList = (string.split())
    for word in stringList:
        print(word)


if __name__ == "__main__":
    main()