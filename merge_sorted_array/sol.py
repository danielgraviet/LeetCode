class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
        return nums1

def main():
    sol = Solution()
    print(sol.merge([1,2,3,0,0,0], 3, [2,3,4], 3))

if __name__ == "__main__":
    main()