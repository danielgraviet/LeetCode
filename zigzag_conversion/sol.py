class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        char_rows = [''] * numRows
        row = 0
        goingDown = False
        
        for char in s:
            char_rows[row] += char
            # check if at top of row
            if row == 0 or row == numRows - 1:
                goingDown = not goingDown
            
            if goingDown:
                row += 1
            else:
                row -= 1
            
        return "".join(char_rows)
        
def main():
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3

    print(sol.convert(s, numRows))
    
    storage = ["first", "second", "third"]
    print(storage[0])

if __name__ == "__main__":
    main()