class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        order = []
        result = []
        dict = {}
        
        for str_item in strs:
            sorted_item = sorted(str_item)
            key = ""
            for item in sorted_item:
                key += item
            
            if key in dict:
                dict[key].append(str_item)
            else:
                dict[key] = [str_item]
        
        for key, value in dict.items():
            result.append(value)
        
        return result



