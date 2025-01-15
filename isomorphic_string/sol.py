class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        for c1, c2 in zip(s, t):
            if s.count(c1) != t.count(c2):
                return False
        return True
        
    def solution(self, s, t):
        if len(s) != len(t):
            return False
        
        hashS = {}
        hashT = {}

        for c1, c2 in zip(s, t):
            if c1 in hashS and hashS[c1] != c2:
                return False
            if c2 in hashT and hashT[c2] != c1:
                return False

            # Establish the mappings
            hashS[c1] = c2
            hashT[c2] = c1

        return True

def main():
    solution = Solution()
    print(solution.isIsomorphic("bbbaaaba", "aaabbbba"))
    print(solution.solution("dog", "acc"))

if __name__ == "__main__":
    main()