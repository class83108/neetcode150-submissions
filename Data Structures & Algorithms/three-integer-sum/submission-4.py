class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result_set = set()
        num_map = {}

        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

        for num in nums:
            if num > 0:
                break

            # 固定第一個 num，避免後面重複使用它
            num_map[num] -= 1
            target = -num

            for k, count in num_map.items():
                if count <= 0:
                    continue

                another = target - k

                if another not in num_map:
                    continue

                if another == k:
                    if num_map[k] >= 2:
                        result_set.add(tuple(sorted((num, k, another))))
                elif num_map[another] > 0:
                    result_set.add(tuple(sorted((num, k, another))))

            num_map[num] += 1

        return [list(item) for item in result_set]