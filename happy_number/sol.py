class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
            if n == 89 or n == 85 or n == 58:
                return False
        return False
        
       
    def sumOfSquares(self, n):
        output = 0
        while n: # if n is not zero, the loop continues.
            digit = n % 10
            digit = digit ** 2
            n = n // 10
            output += digit
        return output
    
def main():
    sol = Solution()
    print(sol.isHappy(0))
    print(sol.sumOfSquares(29))
    print(1//10)
    

if __name__ == "__main__":
    main()