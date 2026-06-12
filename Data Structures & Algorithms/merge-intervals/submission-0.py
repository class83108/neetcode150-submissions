class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        merge_intervals = [intervals[0]]
        for interval in intervals[1:]:
            a = merge_intervals[-1]

            # 需合併
            if a[1] >= interval[0]:
                merge_intervals[-1] = [a[0], max(a[1], interval[1])]
            else:
                merge_intervals.append(interval)
        
        return merge_intervals
        