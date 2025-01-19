class Solution(object):
    def sliding_window(self, letters):
        l = 0
        longest = 0
        n = len(letters)
        sett = set()

        for r in range(n):
            while letters[r] in sett:
                sett.remove(letters[l])
                l += 1
                
            w = (r-l) + 1
            longest = max(longest, w)
            sett.add(letters[r])

        return longest
    
    def find_max_average(self, nums, k):
        n = len(nums)
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]
        
        max_avg = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]

            avg = cur_sum / k
            max_avg = max(max_avg, avg)
        
        return max_avg
        

def main():
    sol = Solution()
    print(sol.sliding_window("abcda"))
    print(sol.find_max_average([1,12,-5,-6,50,3], 4))

if __name__ == "__main__":
    main()