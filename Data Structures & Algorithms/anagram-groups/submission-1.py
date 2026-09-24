class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            chars = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                chars[idx] += 1
            key = tuple(chars)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        
        return list(res.values())