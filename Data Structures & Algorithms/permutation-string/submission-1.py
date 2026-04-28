class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        pointer = 0
        while pointer < len(s2):
            if s2[pointer] in s1:
                
                
                test_str = s2[pointer:pointer+len(s1)]
                s1_array = sorted(s1)
                s2_array = sorted(test_str)
                



                if s1_array == s2_array:
                    return True
                
            pointer += 1

        return False
        