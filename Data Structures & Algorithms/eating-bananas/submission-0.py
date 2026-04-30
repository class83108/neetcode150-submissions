class Solution:
    def canEatBeforeRequestHours(self, piles: List[int], k:int, h: int) -> bool:
        
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        
        return total <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0
        for pile in piles:
            max_pile = max(pile, max_pile)

        left, right = 1, max_pile

        while left < right:
            mid = (left + right) // 2

            if not self.canEatBeforeRequestHours(piles, mid, h):
                left = mid + 1
            else:
                right = mid


        return left
        
    
    

        






