class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = [s for s in s if s.isalnum()]
        revString = ''.join(result[::-1])
        revString = revString.lower()
        return revString == revString[::-1]
    
def main():
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    
if __name__ == "__main__":
    main()