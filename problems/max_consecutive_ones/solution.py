class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        result = 0
        curr_max = 0

        for i in nums:
            if i == 1:
                curr_max += 1
            else:
                result = max(curr_max, result)
                curr_max = 0

        result = max(curr_max, result) 
        return result
