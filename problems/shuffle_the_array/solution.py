class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = list()
        n = int(len(nums) / 2)

        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])

        return result
