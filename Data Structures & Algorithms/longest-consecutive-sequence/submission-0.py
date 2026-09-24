class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach:
        # Add all elements to set
        # Iterate through nums
        # Check if current is start of sequence
        # by checking if previous is in set
        # If yes, keep expanding until not
        # If no, move to next

        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest