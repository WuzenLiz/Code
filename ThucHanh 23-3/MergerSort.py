def merge(start, end):
    a = []
    i = j = 0
    while i < len(start) and j < len(end):
        if start[i] <= end[j]:
            a.append(start[i])
            i += 1
        else:
            a.append(end[j])
            j += 1
    a += start[i:]
    a += end[j:]
    return a


from memory_profiler import profile
@profile
def sort(a):
    if len(a) == 1:
        return a
    mid = len(a)//2
    start = a[:mid]
    end = a[mid:]
    start = sort(start)
    end = sort(end)
    return list(merge(start, end))

if __name__ == '__main__':
    A = [60, 59, 3, 7, 30, 80, 100, 25, 8, 1,
         6, 70, 17, 31, 95, 6, 9, 1, 5, 2, 10]
    from qsort import zi
    print(zi(A))
    print(sort(A))
