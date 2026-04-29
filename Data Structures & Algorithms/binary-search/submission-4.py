class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        print(left)
        return left if target == nums[left] else -1
        

        