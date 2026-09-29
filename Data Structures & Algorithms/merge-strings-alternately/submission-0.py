class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        l = r = 0
        
        while l < len(word1) or r < len(word2):
            # Take from left
            if l < len(word1):
                merged += word1[l]
                l += 1
            if r < len(word2):
                merged += word2[r]
                r += 1
        return merged
        