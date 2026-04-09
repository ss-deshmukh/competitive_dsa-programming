class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        start = 0
        end = len(height) - 1
        while end >= start:
            if height[start] >= height[end]:
                curr_vol = height[end] * (end - start)
                end -= 1
            else:
                curr_vol = height[start] * (end - start)
                start += 1
            vol = max(curr_vol, vol)

        return vol
