import math
import time as tm
# define
PI = math.acos(-1.0)
n = f = 0
a = []
va = []


def check(md):
    sum = 0
    for i in va:
        sum += int(i/md)
    return sum


def main():
    ans = l = v = 0.0
    n, f = input("Nhập số miếng bánh và số khách: ").split()
    f = int(f)+1
    for i in range(int(n)):
        a.append(int(input("Nhập bán kính của bánh thứ %d: " % (i+1))))
    for i in a:
        v = pow(i, 2)*PI
        va.append(v)
    s = 100
    r = 1000000.0
    while (s >= 0):
        mid = (r+l)/2
        if(check(mid) >= f):
            ans = mid
            l = mid
        else:
            r = mid
        s -= 1
    print('%.6f' % ans)


if __name__ == '__main__':
    main()
    a = []
