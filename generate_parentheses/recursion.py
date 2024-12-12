class Solution(object):
    def recursive(self, num):
        return num
    
    def countdown(self, n):
        print(n)
        if n == 0:
            return
        else:
            self.countdown(n-1)
    
    def squares(self, n):
        if n == 0:
            return
        else:
            print(n**2)
            self.squares(n-1)
            
    def steps(self, num):
        if num == 0:
            return
        else:
            print(f"you took step {num}")
            self.steps(num -1)
            
    def sum_digits(self, num):
        if num < 10:
            return num
        else:
            return num % 10 + self.sum_digits(num // 10)
        

def main():
    solution = Solution()
    solution.countdown(5)
    solution.squares(5)
    solution.steps(5)
    print(solution.sum_digits(5234))
    
    
if __name__ == "__main__":
    main()