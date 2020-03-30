import qsort as QS
def binarySearch (arr, low, high, x):
    QS.zi(arr) #Xap sep lai cac phan tu theo thu tu  
    if high >= low: 
        m = low + (high - low) // 2
        if arr[m] == x: 
            return m
        elif arr[m] > x: 
            return binarySearch(arr, low, m-1, x) 
        else: 
            return binarySearch(arr, m + 1, high, x) 
    else: 
        return -1

if __name__ == "__main__":
    arr_def = [9,6,4,-2,56,7,12,-6,-80,5,8]
    arr = []
    n=int(input("Nhập số lượng phần tử (Nhập 0 để sử dụng dãy default): "))
    if (n==0):
        arr = arr_def
    else:
        for i in range(0,n):
            arr = int(input("Nhập phần tử thứ ",i,": "))
    x = int(input("Nhập phần tử cần tìm: "))
    m = binarySearch(arr, 0, len(arr)-1, x) 
    if m != -1: 
        print ("Tìm thấy tại vị trí thứ:",m) 
    else: 
        print ("Phần tử cần tìm không tồn tại") 

