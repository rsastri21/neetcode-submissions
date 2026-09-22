class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        outputLength = len(nums) * 2
        numsLength = len(nums)
        ans = [0] * outputLength
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + numsLength] = nums[i]
        
        return ans
        