class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str_list = []
        for i in s:
            if i.isalnum():
                new_str_list.append(i.lower())

        return new_str_list == new_str_list[::-1]
        