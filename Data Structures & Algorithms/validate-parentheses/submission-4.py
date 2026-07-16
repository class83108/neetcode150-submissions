class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True
        
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []

        for item in s:
            if item in mapping:
                stack.append(item)
            else:
                if len(stack) > 0:
                    last_item = stack[-1]
                    if mapping[last_item] == item:
                        stack.pop()
                        continue
                    else:
                        return False
                else:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True