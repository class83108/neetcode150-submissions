class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}

        left, right = 0, 0

        max_freq = 0
        max_window = 0

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            need_num = (right - left + 1) - max_freq

            if need_num > k:
                freq[s[left]] -= 1
                left += 1

            # 右指針繼續走
            max_window = max(max_window, right - left + 1)
            right += 1
        
        return max_window





        