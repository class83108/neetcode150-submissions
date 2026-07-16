class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        counts = defaultdict(int)
        result_set = set()

        for num in nums:
            counts[num] += 1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            counts[nums[i]] -= 1
            
            for j in range(i+1, len(nums)):
                counts[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i] + nums[j])

                if counts[target]:
                    result_set.add(tuple((nums[i], nums[j], target)))
            for j in range(i+1, len(nums)):
                counts[nums[j]] += 1

        return [list(i) for i in result_set]









        