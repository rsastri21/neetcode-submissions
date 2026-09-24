class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                chars[idx] += 1
            key = tuple(chars)
            res[key].append(s)
        
        return list(res.values())