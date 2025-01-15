import random

class RandomizedSet(object):

    def __init__(self):
        self.data = {}
        self.numList = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        inserts val into the set, if not present.
        returns true if the item was not present
        returns false if the item is present
        """
        # if the dictionary is empty
        if not self.data:
            # add to to dictionary
            self.data[val] = True
            self.numList.append(val)
        # if there are items in the dict
        else:
            # check if already there
            if val in self.data:
                return False
            else:
                self.data[val] = True
                self.numList.append(val)

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # if dict is empty, return false
        if not self.data:
            return False
        # if item in dict
        else:
            # check if matches
            if val in self.data:
                # remove 
                del self.data[val]
                self.numList.remove(val)
                return True
            else:
                return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.numList)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
def main():
    sol = RandomizedSet()
    print(sol.insert(3))
    print(sol.insert(2))
    print(sol.insert(5))
    print(sol.insert(3))
    print(sol.getRandom())
    



if __name__ == "__main__":
    main()