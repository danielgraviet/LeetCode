class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ascii_ransom_note = []
        ascii_magazine_note = []
        for char in ransomNote:
            ascii_ransom_note.append(ord(char))
            
        for char in magazine:
            ascii_magazine_note.append(ord(char))
            
        for num in ascii_ransom_note:
            if num not in ascii_magazine_note:
                return False
            else:
                ascii_magazine_note.remove(num)
        return True
        
def main():
    solution = Solution()
    print(solution.canConstruct("aa", "ab"))
    
if __name__ == "__main__":
    main()