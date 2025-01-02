class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # first make another array with all 1's
        candy_array = [1] * len(ratings)
        # if the left index of the ratings is lower than the right index
        # increment the right index of the candy_array
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i+1]:
                candy_array[i+1] = candy_array[i] + 1
        
        # right to left pass
        # start at 2 to last element, and check if greater
        for i in range(len(candy_array) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # take max
                candy_array[i] = max(candy_array[i], candy_array[i + 1] + 1)

        return sum(candy_array)
def main():
    sol = Solution()
    print(sol.candy([3,4,0,1,2]))
    print(sol.candy([1,2,87,87,87,2,1]))

if __name__ == "__main__":
    main()
        