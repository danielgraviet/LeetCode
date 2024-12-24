class Solution(object):
    def canJump(self, nums):
        if nums and nums[0] == 0:
            return False
        
        if not nums:
            return False
        
        maxReach = 0
        dict = {}
        for i, n in enumerate(nums):
            # check the max range
            if i > maxReach:
                return False
            if (i + n >= len(nums) - 1):
                return True
            maxReach = max(maxReach, i + n)
        return True
    
    def activity_selection(self, activities):
        # Sort activities by their finish times
        sorted_activities = sorted(activities, key=lambda x: x[1])
        
        selected = []  # List to store selected activities
        last_end_time = 0  # Track the end time of the last selected activity
        
        for activity in sorted_activities:
            start, end = activity
            if start >= last_end_time:  # Check if activity can be selected
                selected.append(activity)
                last_end_time = end  # Update the end time of the last selected activity
        
        return selected

def main():
    sol = Solution()
    print(sol.canJump([1,2,2,0,4]))

     # Example input: (Start Time, End Time)
    activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (8, 9)]
    result = sol.activity_selection(activities)
    print("Selected activities:", result)

if __name__ == "__main__":
    main()