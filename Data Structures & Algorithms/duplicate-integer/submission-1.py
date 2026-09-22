class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        filtered = set(nums)
        return len(filtered) != len(nums)
        