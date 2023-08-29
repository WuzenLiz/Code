a = [1,3,5,7,8,10,12] 
b = [4,6,9,11]
def dIm(n,y):
    if n in a:
        return 31
    elif n in b:
        return 30
    else:
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            return 29
        else:
            return 28
if __name__ == '__main__':
    t = int(input("Nhap thang: "))
    n = int(input("Nhap nam: "))
    print("Thang",t,"co",dIm(t,n),"ngay!")