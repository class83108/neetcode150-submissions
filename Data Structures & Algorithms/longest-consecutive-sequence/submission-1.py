class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        # 先 sort 一次
        nums.sort()

        # 然後遍歷時 看能連續多少
        count = 1
        longest = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
                longest = max(longest, count)
            elif nums[i] == nums[i-1]:
                continue
            else:
                count = 1
                longest = max(longest, count)

        return longest
        