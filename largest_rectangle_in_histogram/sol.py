class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        n = len(heights)
        max_area = 0
        
        for i in range(n):
            # While the current bar is shorter than the bar at the stack's top, process     the stack
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]  # Height of the bar
                width = i if not stack else i - stack[-1] - 1  # Width calculation
                max_area = max(max_area, h * width)
            stack.append(i)
        
        # Process remaining bars in the stack
        while stack:
            h = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, h * width)
        
        return max_area
        

        
def main():
    sol = Solution()
    heights = [2,1,5,6,2,3]
    print(sol.largestRectangleArea(heights))

if __name__ == "__main__":
    main()