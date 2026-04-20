class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dict = defaultdict(list)

        for index, num in enumerate(nums):
            value = target - num
            if value not in num_dict:
                num_dict[num].append(index)
            else:
                return [num_dict[value].pop(), index]
        
        return []
        

        