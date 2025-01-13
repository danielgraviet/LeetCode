class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        newlist = []
        s_index = 0
        # loop through each character in t
        # add it, if that character is found in s.
        for char in t:
            if s_index < len(s) and char == s[s_index]:
                newlist.append(char)
        return ''.join(newlist) == s

    
    def aiSolution(self, s, t):
        i, j = 0, 0  # Initialize pointers for s and t
        while i < len(s) and j < len(t):  # Traverse both strings
            if s[i] == t[j]:  # If characters match, move the pointer for s
                i += 1
            j += 1  # Always move the pointer for t
        return i == len(s)  # Check if all characters in s were matched
        
def main():
    sol = Solution()
    print(sol.aiSolution("ab", "baab"))

if __name__ == "__main__":
    main()