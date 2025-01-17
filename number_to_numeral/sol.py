class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanList = [["I", 1],
                     ["IV", 4],
                     ["V", 5],
                     ["IX", 9],
                     ["X", 10],
                     ["XL", 40],
                     ["L", 50],
                     ["XC", 90],
                     ["C", 100],
                     ["CD", 400],
                     ["D", 500],
                     ["CM", 900],
                     ["M", 1000]]
        
        res = ""
        
        for sym, digit in romanList[::-1]:
            if num // digit:
                count = num // digit
                res += (count * sym)
                num = num % digit
        return res
    
    def extract_places(self, number):
        place_values = []
        place = 1
        
        while number > 0:
            digit = number % 10
            place_values.append(digit * place)
            number //= 10
            place *= 10

        return place_values[::-1]

        
def main():
    sol = Solution()
    print(sol.intToRoman(3749))

if __name__ == "__main__":
    main()