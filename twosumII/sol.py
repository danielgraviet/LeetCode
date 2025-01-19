class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create dictionary with index and number
        dict = {}
        
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in dict:
                return[dict[complement], i]
            dict[num] = i

        return 0


def main():
    sol = Solution()
    print(sol.twoSum([1,2,4,8], 9))

if __name__ == "__main__":
    main()