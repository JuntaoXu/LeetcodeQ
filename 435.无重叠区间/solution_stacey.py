# def eraseOverlapIntervals(intervals):
#     intervals.sort()
#     cur_intv = [intervals[0]]
#     for i,j in intervals[1:]:
#         cur_start, cur_end = cur_intv[0][0], cur_intv[-1][1]
#         if j <= cur_start:
#             cur_intv.insert(0, [i,j])
#         elif i >= cur_end:
#             cur_intv.append([i,j])
#         elif i<cur_start and j > cur_end:
#             continue
#         else:
#             for n,intv in enumerate(cur_intv):
#                 if i > intv[1]:
#                     continue
#                 elif j <= intv[1]:
#                     if n > 0 and i < cur_intv[n-1][1]:
#                         continue
#                     cur_intv[n] = [i,j]
#                 else:
#                     continue
#     return len(intervals)-len(cur_intv)

def eraseOverlapIntervals(intervals):
    if len(intervals) < 2: return 0
    intervals.sort()
    count = 0
    pos = 0
    i = 1
    while i < len(intervals):
        if intervals[i][1] < intervals[pos][1]:
            pos = i
            i+=1
            count+=1
        elif intervals[i][0] >= intervals[pos][1]:
            pos = i
            i+=1
        else:
            i+=1
            count += 1
    return count

l = [[1,100],[2,22],[1,11],[11,22]]
print(eraseOverlapIntervals(l))


