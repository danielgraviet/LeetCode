class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        smallStr = min(str1, str2)
        bigStr = max(str1, str2)
        print(bigStr)
        res = []
        if str1[0] != str2[0]:
            return ""
        else:
            for firstChar, secondChar in zip(str1, str2):
                if firstChar == secondChar:
                    res.append(firstChar)
        return "".join(res)

    def fastSolution(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            while b:
                a,b = b, a % b
            return a

        gcd_string = (gcd(len(str1), len(str2)))
        return str1[:gcd_string]

                
def main():
    sol = Solution()
    print(sol.fastSolution("ABCABC", "ABC"))

if __name__ == "__main__":
    main()