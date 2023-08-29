import time as tm
def fibonacci(n):
    a = "A" 
    b = "B"
    if n<0:
        print('Lỗi!')
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

FIBstr = lambda n: 'A' if n == 0 else 'B' if n == 1 else FIBstr(n-1) + FIBstr(n-2)

def main():
    n = int(input('Nhập số cần tìm fibonacci: '))
    m = fibonacci(n)
    print("Dãy Fibonacci cần tìm là:" ,FIBstr(n) , end="\n")
    print("Dãy Fibonacci cần tìm là:" ,m , end="\n")
    i = int(input('Bạn muốn tìm kí tự thứ mấy trong xâu fibonacci: '))
    if (i>len(m)):
        print("Không tìm thấy kí tự tại vị trí ",i)
    else:
        print("Kí tự cần tìm:",m[i] )

if __name__ == '__main__':
    start = tm.time()
    main()
    print('Đã tốn %s giây để tính xong' % (tm.time() - start))