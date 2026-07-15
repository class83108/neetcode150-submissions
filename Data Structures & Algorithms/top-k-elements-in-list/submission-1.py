class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = defaultdict(int)

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        sorted_nums = sorted(nums_dict, key = lambda key: nums_dict[key], reverse=True)

        return sorted_nums[:k]
