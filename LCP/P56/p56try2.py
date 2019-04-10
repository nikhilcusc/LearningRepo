# method 2 : use the intervals - check second element from one interval to first element of next interval and merge if first one is >= second one.
def merge( intervals) :
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out


int1 = [[1,3],[2,6],[8,10],[15,18]]
int2 = [[1,4],[4,5]]

print(merge(int1))