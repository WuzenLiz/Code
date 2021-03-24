import FibonacyWord as Fi
def Findi(i,n):
    stri = Fi.fibonacci(n)
    print(stri[i])
    
if __name__ == "__main__":
    n = int(input('Nhập số cần tìm fibonacci: '))
    i = int(input('Bạn muốn tìm kí tự thứ mấy trong xâu fibonacci: '))
    Findi(i,n)