class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        res = ""
        stack = []
        for c in s:
            if c.isalnum():
                res += c
        # find half way, put into a stack
        half = len(res) // 2
        for i in range(half):
            stack.append(res[i])

        # pop the top and check if equals end of res
        i = -1
        stackIndex = 0
        for _ in range(half):
            if stack[stackIndex] != res[i]:
                return False
            else:
                i -= 1
                stackIndex += 1
        return True
    
    def pythonicSolution(self, s):
        char_result = "".join([s.lower() for s in s if s.isalnum()])
        return char_result[::-1] == char_result
        
def main():
    sol = Solution()
    print(sol.isPalindrome(""))
    print(sol.pythonicSolution("Amannama"))

if __name__ == "__main__":
    main()