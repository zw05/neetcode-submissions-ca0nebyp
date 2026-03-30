class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subarray = set()
        n = len(s)
        l = 0
        max_length = 0

        for r in range(n):
            while s[r] in subarray:
                subarray.remove(s[l])
                l += 1
            subarray.add(s[r])
            max_length = max(max_length, len(subarray))
        return max_length
