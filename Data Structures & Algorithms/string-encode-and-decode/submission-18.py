class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        encode = []
        for s in strs:
            
            encode.append(str(len(s)))
            encode.append("#")
            encode.append(s)
        
        return "".join(encode)

    def decode(self, s: str) -> List[str]:

        i = 0
        result = []
        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length
            
            result.append(s[i:j])
            i = j
        
        return result

