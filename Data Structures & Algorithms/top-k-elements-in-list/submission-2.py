class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # dict -> value nums

        # sorted (lambda x: dict[x]) -> k

        elements_map = defaultdict(int)

        for num in nums:
            elements_map[num] += 1
        
        frequent_sorted = sorted(elements_map, key=lambda x: elements_map[x], reverse=True)
    
        return frequent_sorted[:k]

