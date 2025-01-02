import random
class Solution(object):
    def __init__(self):
        self.numList = []
        self.numDict = {}
        
    def insert(self, val):
        # if val is empty, add to both 
        if not self.numDict:
            self.numDict[val] = True
            self.numList.append(val)
        else:
            if val not in self.numDict:
                self.numDict[val] = True
                self.numList.append(val)
            else:
                return ValueError

    def remove(self, val):
        # if dict is empty, return error
        if not self.numDict:
            return IndexError
        else:
            if val in self.numDict:
                del self.numDict[val] 
                self.numList.remove(val)
            else:
                return IndexError
        # else throw error
        return 0

    def getRand(self):
        return 
    
    def print(self):
        return random.choice(self.numList)


def main():
    sol = Solution()
    sol.insert(1)
    sol.insert(2)
    sol.insert(3)
    sol.insert(1)
    print(sol.getRand())
    print(sol.print())


if __name__ == "__main__":
    main()