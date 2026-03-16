class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Sorting approach - works for unbounded values
        sorted_nums = sorted(nums)

        # Use a dictionary to map unique values to their position in sorted array
        rank = {}
        for i, num in enumerate(sorted_nums):
            if num not in rank:  # Only store first occurrence
                rank[num] = i

        # Build result
        result = []
        for num in nums:
            result.append(rank[num])

        return result