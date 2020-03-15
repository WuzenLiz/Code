import time as tm
def fibonacci(n):
    a = 1 
    b = 1
    if n<0:
        print('Lỗi!')
    elif n==1:
        return a
    elif n==2:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b
 
def main():
    n = int(input('Nhập số cần tìm fibonacci: '))
    m = fibonacci(n)
    print(m)
    
if __name__ == '__main__':
    start = tm.time()
    main()
    print('Đã tốn %s giây để tính xong' % (tm.time() - start))