class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = s.lower().strip()
        alphanum = "".join([letter for letter in stripped if letter.isalnum()])
        
        return alphanum == alphanum[::-1]
