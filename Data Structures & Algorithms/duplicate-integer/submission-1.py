class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) < 2:
            return False

        dict = {}

        for num in nums:
            if num in dict:
                return True
            else:
                dict[num] = 1
        
        return False
        