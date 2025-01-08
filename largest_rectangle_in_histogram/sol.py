class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # start with numbers left to right
        # put first number as maxArea
        # if next number is greater than maxArea, take max of next number,
        # or area created by the second rectangle. 
        # 
        maxHeight = []
        for num in heights:
            # if stack empty, add to it
            if not maxHeight:
                maxHeight.append(num)
            else:
                if maxHeight[-1] < num:
                    maxHeight.pop()
                    maxHeight.append(num)

        return maxHeight

        
def main():
    sol = Solution()
    heights = [2,1,5,6,2,3]
    print(sol.largestRectangleArea(heights))

if __name__ == "__main__":
    main()