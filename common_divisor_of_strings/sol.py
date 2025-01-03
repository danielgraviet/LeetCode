class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        res = []
        if str1[0] != str2[0]:
            return ""
        else:
            for firstChar, secondChar in zip(str1, str2):
                if firstChar == secondChar:
                    res.append(firstChar)
        return "".join(res)
                
def main():
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))

if __name__ == "__main__":
    main()