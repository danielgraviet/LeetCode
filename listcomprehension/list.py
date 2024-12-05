class Solution(object):
    def setintersect(self, set1, set2):
        return bool(set1 & set2)
    
    def joinlist(self, list):
        print(" ".join(list))
        
    
def main():
    solution = Solution()
    set1 = set('dan')
    set2 = set('graviet')
    result = solution.setintersect(set1, set2)
    print("Sets have common elements:", result)
    
    list = ["daniel", "thi", "graviet"]
    solution.joinlist(list)
    
if __name__ == "__main__":
    main()