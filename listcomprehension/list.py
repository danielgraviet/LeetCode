import math

class Solution(object):
    def setintersect(self, set1, set2):
        return bool(set1 & set2)
    
    def joinlist(self, list):
        print(" ".join(list))
        
    
def main():
    solution = Solution()
    numList = [1,2,3,4]
    squaredList = [num ** 2 for num in numList]
    print(squaredList)

    prices = [3.99, 2.45, 4.75]
    for i, price in enumerate(prices):
        nearest_dollar = math.ceil(price)
        difference = nearest_dollar - price
        difference_cents = round(difference * 100)
        print(f"Price = {price:.2f}, Difference = {difference_cents} cents")
    
    
if __name__ == "__main__":
    main()