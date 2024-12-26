class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # sort the array, to start in the middle.
        citations.sort()

        # find the middle index to start
        middleIndex = len(citations) // 2
        targetVal = citations[middleIndex]

        count = 0
        for c in citations:
            if c >= targetVal:
                count += 1
        
        if count >= targetVal:
            print(f"{targetVal} is a valid h-index because it appeared {count} times.")

        return citations
    
    def solution2(self, citations):
        count = 0
        maxVal = 0

        for i in range(len(citations) + 1):
            count = 0
            for p in citations:
                if p >= i:
                    count += 1
            if count >= i:
                maxVal = max(i, maxVal)
                count = 0
        
        return maxVal


        
def main():
    sol = Solution()
    citations = [3,0,6,1,5]
    citations2 = [11, 15]
    print(sol.hIndex(citations))
    print(sol.solution2(citations))

if __name__ == "__main__":
    main()