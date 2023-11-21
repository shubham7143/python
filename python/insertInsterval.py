def insert_interval(intervals, new_interval):
    ans = []
    i = 0
    while i < len(intervals) and intervals[i][0] <= new_interval[0]:
        ans.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][0], new_interval[1])
        i += 1

    ans.append(new_interval)

    while i < len(intervals):
        ans.append(intervals[i])
        i += 1

    return ans


if __name__ == '__main__':
    intervals = [[1, 3], [5, 7], [8, 12], [13, 17]]
    new_interval = [4, 9]
    ans = insert_interval(intervals, new_interval)
    print(ans)
