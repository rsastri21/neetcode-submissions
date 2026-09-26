class Solution:
    def isPalindrome(self, s: str) -> bool:
        seq = ""
        for char in s:
            if char.isalnum():
                seq += char.lower()

        l = 0
        r = len(seq) - 1

        while l < r:
            if seq[l] != seq[r]:
                return False
            l += 1
            r -= 1
        
        return True
        