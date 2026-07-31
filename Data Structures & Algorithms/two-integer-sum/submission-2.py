class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}

        for i in range(len(nums)):

            substract = target - nums[i]

            if substract in dict:
                return [dict[substract], i]
            
            else:
                dict[nums[i]] = i
        
        
