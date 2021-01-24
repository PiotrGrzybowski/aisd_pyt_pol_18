from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) < 2:
        return intervals
    else:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]
        current_interval = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], interval[1])
            else:
                result.append(interval)
                current_interval = interval

        return result


if __name__ == '__main__':
    intervals = [[20, 24], [30, 31], [4, 8], [6, 10], [18, 22], [25, 32]]
    print(merge_intervals(intervals))
