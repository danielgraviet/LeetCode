from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
            
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False
            
        return True
    
def main():
    solution = Solution()
    print(solution.canConstruct("abc", "def"))
    name = "daniel thi graviet"
    print(name.count("a"))

    newSet = set("Daniel Thi Graviet")
    print(len(newSet))
        
    
if __name__ == "__main__":
    main()