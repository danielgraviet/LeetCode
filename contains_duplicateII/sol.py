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

    # test_dict = {1:[0, -3], 2:[1], 3:[2]}
    # for key in test_dict:
    #     if len(test_dict[key]) >= 2:
    #         # subtract the values, get the abs.
    #         print(abs(test_dict[key][0] + test_dict[key][1]))
    #     else:
    #         print(False)
    array = [0,2,3]
    print(array[-1])
    print(array[-2])

if __name__ == "__main__":
    main()