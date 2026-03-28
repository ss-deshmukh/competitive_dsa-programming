class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v_set = set()
        left = 0
        v_max = 0
        
        for right in range(len(s)):
            # If duplicate found, shrink window from the left
            while s[right] in v_set:
                v_set.remove(s[left])
                left += 1
            
            v_set.add(s[right])
            v_max = max(v_max, right - left + 1)
            
        return v_max