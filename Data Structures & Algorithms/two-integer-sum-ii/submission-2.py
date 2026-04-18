class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx, number in enumerate(numbers):
            value = target - number

            for i in range(idx+1, len(numbers)):
                if numbers[i] > value:
                    break
                if numbers[i] == value:
                    return [idx+1, i+1]
        
        return []

        