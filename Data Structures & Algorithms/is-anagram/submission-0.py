class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)

        for letter in s:
            s_dict[letter] += 1

        for letter in t:
            if letter not in s_dict:
                return False
            else:
                s_dict[letter] -= 1
                if s_dict[letter] == 0:
                    del s_dict[letter]
        
        if len(s_dict) != 0:
            return False
        return True


        