class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        sorted_nums = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        res = []
        for s in sorted_nums:
            res.append(s[0])

        return res[:k]
        