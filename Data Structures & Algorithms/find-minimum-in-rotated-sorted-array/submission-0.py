class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        # nums[mid] < nums[right] -> right = mid
        # nums[mid] >= nums[right] -> left = mid
        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] >= nums[right]:
                left = mid + 1
        
        return nums[left]

# [3,4,5,6,1,2] mid = 6 right = 2
# mid = 1 right = 2
# 4 + 3 // 2 = 3


        
        