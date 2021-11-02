
def eraseOverlapIntervals(intervals):
    intervals.sort()
    cur_intv = [intervals[0]]
    for i,j in intervals[1:]:
        cur_start, cur_end = cur_intv[0][0], cur_intv[-1][1]
        if j <= cur_start:
            cur_intv.insert(0, [i,j])
        elif i >= cur_end:
            cur_intv.append([i,j])
        elif i<cur_start and j > cur_end:
            continue
        else:
            for n,intv in enumerate(cur_intv):
                if i > intv[1]:
                    continue
                elif j <= intv[1]:
                    if n > 0 and i < cur_intv[n-1][1]:
                        continue
                    cur_intv[n] = [i,j]
                else:
                    continue
    return len(intervals)-len(cur_intv)

l = [[1,100],[11,22],[1,11],[2,12]]

print(eraseOverlapIntervals(l))


