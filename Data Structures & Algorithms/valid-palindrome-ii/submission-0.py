class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] == s[r]:
                    r -= 1
                    l += 1
                else:
                    return False
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # Try either side
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
        return True