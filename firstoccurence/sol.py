class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
def main():
    solution = Solution()
    print(solution.strStr("daniel thi graviet", "thi"))

if __name__ == "__main__":
    main()