

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        res = []

        for point in points:
            x, y = point[0], point[1]
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, [dist, x, y])
        
        for _ in range(0, k):
            item = heapq.heappop(heap)
            res.append([item[1], item[2]])

        return res
        
        