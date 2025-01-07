class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        char_rows = [""] * numRows
        goingDown = False
        row = 0

        for char in s:
            char_rows[row] += char

            if row == 0 or row == numRows - 1:
                goingDown = not goingDown

            if goingDown:
                row += 1
            else:
                row -= 1

        return "".join(char_rows)
    def coding_challenge_1(self, s, numRows):
        # Write a function to generate the zigzag pattern
        # of a string as a list of strings (one string per row)
        # instead of combining the rows into one output.
        char_rows = [''] * numRows
        goingDown = False
        curr_row = 0

        for char in s:
            char_rows[curr_row] += char

            if curr_row == 0 or curr_row == numRows - 1:
                goingDown = not goingDown
            if goingDown:
                curr_row += 1
            else:
                curr_row -= 1

        return char_rows
    
    def coding_challenge_2(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            print(s)
            return

        # Initialize rows as empty strings
        rows = [''] * numRows
        curRow = 0
        goingDown = False

        # Traverse the string to populate rows
        for char in s:
            rows[curRow] += char
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        # Find maximum row length to pad the rows with spaces for proper zigzag
        max_row_len = max(len(row) for row in rows)

        # Print the rows with proper spacing for the zigzag pattern
        for i, row in enumerate(rows):
            padded_row = [' '] * max_row_len  # Start with spaces
            for j, char in enumerate(row):
                idx = j * (2 * numRows - 2)  # Calculate the zigzag column index
                if i % (numRows - 1) == 0:   # Only align for top or bottom
                    padded_row[idx] = char
            print(''.join(padded_row))  # Join and print the zigzag



def main():
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3

    print(sol.convert(s, numRows))
    print(sol.coding_challenge_1(s, numRows))
    print(sol.coding_challenge_2("HELLOZIGZAG", 3))
    
    

if __name__ == "__main__":
    main()