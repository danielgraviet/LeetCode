class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            result.append(count)
        return result
    
    def optimizedSol(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([temp, i])
        return res
    # 
def main():
    solution = Solution()

    print(solution.dailyTemperatures([30,40,70,20]))
    print(solution.optimizedSol([30,40,70,20]))
    

if __name__ == "__main__":
    main()