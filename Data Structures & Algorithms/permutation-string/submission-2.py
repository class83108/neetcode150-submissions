class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_match_array = [0] * 26
        s2_match_array = [0] * 26
        
        for i in range(len(s1)):
            s1_match_array[ord(s1[i]) - ord("a")] += 1
            s2_match_array[ord(s2[i]) - ord("a")] += 1

        if s1_match_array == s2_match_array:
            return True

        left = 0
        right = len(s1)

        while right < len(s2):
            s2_match_array[ord(s2[right]) - ord("a")] += 1
            s2_match_array[ord(s2[left]) - ord("a")] -= 1

            if s2_match_array == s1_match_array:
                return True
            
            right += 1
            left += 1
        
        return False




        
            




        
        
        