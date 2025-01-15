class Solution(object):
    def fibonacci(self, num):
        if num < 0:
            raise ValueError
        if num == 1:
            return 1
        
        a,b = 1, 1
        for _ in range(2, num):
            a, b = b, a + b
            
        return b
    
    def factorial(self, n):
        if n < 0:
            return "Factorial is not defined for negative numbers"
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n+1):
                result *= i
            return result
        
    def fizz_buzz(self, n):
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
        
def main():
    solution = Solution()
    print(solution.fibonacci(7))
    print(solution.factorial(6))
    print(solution.fizz_buzz(15))
    

if __name__ == "__main__":
    main()