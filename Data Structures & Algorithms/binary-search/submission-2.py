class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        print(left)
        if left < len(nums):
            if target == nums[left]:
                return left
            else:
                return -1
        return -1

        