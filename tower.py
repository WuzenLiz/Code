def func(start,n):
    s = start
    y = []
    if n>5:
        return
    for i in range(n):
        s = s + 2
        y.append(s)
    print(y)
    func(s,n+1)
func(1,1)