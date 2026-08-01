class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = []
        right = []
        res = []
        
        for i in range(len(nums)):
            if i == 0:
                item = 1
            else:
                item = left[i-1] * nums[i-1]
            left.append(item)
        
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                item = right_product
            else:
                item = right_product * nums[i+1]
                right_product = item
            right.append(item)
        right = right[::-1]
        print(left)
        print(right)
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        
        return res



