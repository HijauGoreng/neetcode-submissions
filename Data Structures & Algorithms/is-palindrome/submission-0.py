class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = s.lower().strip()
        alphanum = "".join([letter for letter in stripped if letter.isalnum()])
        reverse = ""
        for i in range(len(alphanum)-1, -1, -1):
            reverse += alphanum[i]

        return alphanum == reverse
