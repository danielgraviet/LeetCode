class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_seen = {}
        for i, n in enumerate(nums):
            if n in last_seen:
                if i - last_seen[n] <= k:
                    return True
            last_seen[n] = i
        return False

def main():
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))
if __name__ == "__main__":
    main()