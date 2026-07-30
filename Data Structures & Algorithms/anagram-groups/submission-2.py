class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        dict = {}

        for string in strs:

            sorted_key_list = sorted(string)
            sorted_key = "".join(sorted_key_list)
            if sorted_key in dict:
                dict[sorted_key].append(string)
            else:
                dict[sorted_key] = [string]
        
        result = []
        for k, v in dict.items():

            result.append(v)
        
        return result
