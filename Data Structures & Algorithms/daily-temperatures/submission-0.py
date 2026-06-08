class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # candidates = [{"temperature": xx, "index": xx}, ...]
        candidates = []
        res = [0] * len(temperatures)

        for index in range(len(temperatures)-1, -1, -1):
            while candidates and candidates[-1]["temperature"] <= temperatures[index]:
                candidates.pop()
                       
            res[index] = candidates[-1]["index"] - index if candidates else 0
            
            candidates.append({"temperature": temperatures[index], "index": index})
            
        return res
            