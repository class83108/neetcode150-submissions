class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        string_set = set()
        left, right = 0, 0
        max_length = 0

        while right < len(s):
            if s[right] not in string_set:
                string_set.add(s[right])
                curr = right - left + 1
                max_length = max(max_length, curr)
                right += 1
            else:
                string_set.remove(s[left])
                left += 1


        return max_length
        