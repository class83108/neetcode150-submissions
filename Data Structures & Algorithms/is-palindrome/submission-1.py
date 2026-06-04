class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for character in s:
            if character.isalnum():
                new_str += character.lower()
        
        return new_str == new_str[::-1]

        