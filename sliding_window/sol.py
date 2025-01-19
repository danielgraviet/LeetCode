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
    
    def max_sum_subarray(self, arr, k):
        # Your code here
        curSub = sum(arr[:k])
        maxSub = curSub

        for i in range(k, len(arr)):
            curSub += arr[i]
            curSub -= arr[i-k]

            maxSub = max(maxSub, curSub)
        return maxSub
    
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
    
    def maxSum(self, nums, k):
        # find starting window. 
        startSum = sum(nums[:k])
        maxSum = startSum

        # slide the window over, until the last spot
        for i in range(k, len(nums)):
            startSum += nums[i]
            startSum -= nums[i - k]

            maxSum = max(maxSum, startSum)
        # keep track of the max. 
        return maxSum

def main():
    sol = Solution()


     # Test the function
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    result = sol.max_sum_subarray(arr, k)
    print(f"Maximum sum of subarray of size {k}: {result}")

if __name__ == "__main__":
    main()