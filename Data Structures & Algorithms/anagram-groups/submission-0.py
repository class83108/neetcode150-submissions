class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # set()
        res = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            
            if sorted_s not in res:
                res[sorted_s] = [s]
            else:
                res[sorted_s].append(s)
        
        ans = []
        for k, v in res.items():
            ans.append(v)
        return ans

        




        