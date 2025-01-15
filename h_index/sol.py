class Solution(object):
    def hIndex(self, citations):
        # this is the online solution
        n = len(citations)
        paper_counts = [0] * (n + 1)

        for c in citations:
            paper_counts[min(n, c)] += 1

        h = n
        papers = paper_counts[n]

        while papers < h:
            h -= 1
            papers += paper_counts[n]

        return h

    
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
    
    def basicForLoop(self, citations):
        for n in citations:
            print(n)
        return 0

def main():
    sol = Solution()
    citations = [3,0,6,1,5]
    citations2 = [11, 15]
    print(sol.hIndex([1,2,3]))
    print(sol.solution2(citations))

if __name__ == "__main__":
    main()