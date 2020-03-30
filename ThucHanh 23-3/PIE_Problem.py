import math
import time as tm
#define 
PI=math.acos(-1.0)
n=0
f=0
a=[]
va=[]
def main():      
    h,l,v=0.0,0.0,0.0
    n,f=input("Nhập số miếng bánh và số khách: ").split()
    f=int(f)+1
    for i in range(int(n)):
        a.append(int(input("Nhập bán kính của bánh thứ %d: " %(i+1))))
    for i in a:
        v=pow(i,2)*PI
        va.append(v)
        if(v>h):
            h=v
    mid=(h+l)/2
    while ((h-l)<1e-7):
        sum=0
        for i in va:
            sum+=int(i/mid)
        if(sum>=f):
            l=mid
        else:
            h=mid
        mid=(h+l)/2
    print('%.6f' % mid)

if __name__ == '__main__':
    start = tm.time()
    main()
    print('Đã tốn %s giây để thực hiện' % (tm.time() - start))
