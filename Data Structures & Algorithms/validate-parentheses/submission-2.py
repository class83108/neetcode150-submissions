class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        
        stack = []

        for item in s:
            if item in dict:
                stack.append(item)
            else:
                if len(stack) > 0:
                    left_brackets = stack.pop()
                    if dict[left_brackets] != item:
                        return False
                else:
                    return False

        if len(stack) > 0:
            return False
        
        return True

        