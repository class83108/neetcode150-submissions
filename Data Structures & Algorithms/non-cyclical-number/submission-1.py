class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.createNextNumber(n)
        while slow != fast:
            fast = self.createNextNumber(fast)
            fast = self.createNextNumber(fast)
            slow = self.createNextNumber(slow)
            
        return True if fast == 1 else False



    def createNextNumber(self, n: int) -> int:
        
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output

        
        