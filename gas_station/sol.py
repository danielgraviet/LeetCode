class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gasCost = []
        starting_points = []
        gasTank, gasValue, index = 0, 0, -1
        for g, c in zip(gas, cost):
           gasCost.append([g,c])
           index += 1
           if g >= c:
            starting_points.append(index)
        
        # start at the first index and construct new array order
        for start_index in starting_points:
            gasTank, gasValue = 0,0
            reordered_gasCost = gasCost[start_index:] + gasCost[:start_index]
            for i in reordered_gasCost:
                gasTank += i[0]
                gasValue += i[1]
                if gasTank < gasValue:
                    break
            else:
                return start_index
        return -1

        

def main():
    sol = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    print(sol.canCompleteCircuit(gas, cost))

    # array = [1,2,3,4,5]
    # pivot = 0
    # print(array[pivot:])
    # print(array[:pivot])
    # array = array[pivot:] + array[:pivot]
    # print(array)



if __name__ == "__main__":
    main()