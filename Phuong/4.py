import math as m
import re
def isTrig(a,b,c):
    if a+b>c and a+c>b and b+c>a and a > 0 and b > 0 and c > 0:
        return True
    else:
        return False

def chuVi(a,b,c):
    return (a+b+c)/2

def dienTich(a,b,c):
    cv = chuVi(a,b,c)
    return m.sqrt(cv*(cv - a)*(cv - b)*(cv - c))

if __name__ == '__main__':
    a = float(input("Canh a: "))
    b = float(input("Canh b: "))
    c = float(input("Canh c: "))
    if isTrig(a,b,c):
        print("3 canh da nhap tao nen 1 tam giac co\nChu vi: ",chuVi(a,b,c),"\nDien tich: ",dienTich(a,b,c))
    else:
        print("3 canh nhap vao khong tao nen tam giac")