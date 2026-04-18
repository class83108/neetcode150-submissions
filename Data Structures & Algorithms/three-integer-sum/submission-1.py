class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()

        for index, num in enumerate(nums):
            if num > 0:
                break
            if index > 0 and num == nums[index-1]:
                continue
            
            target = 0 - num

            pairs = self.two_sum(nums, index+1, target)
            for pair in pairs:
                ans.append([num] + pair)
        
        return ans

    def two_sum(self, nums: List[int], start:int, target:int) -> List[List[int]]:
        
        pairs = []

        left = start
        right = len(nums) - 1
        while left < right:
            
            my_sum = nums[left] + nums[right]
            if my_sum == target:
                pairs.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif my_sum < target:
                left += 1
            else:
                right -= 1

        return pairs

