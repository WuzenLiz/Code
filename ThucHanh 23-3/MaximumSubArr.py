minimum = -1000000
def Global_Sum_subarr(arr,l,m,h):
    # l - low; m - mid; h - high
    right_sum = minimum
    left_sum = minimum
    # Left sum
    sum = 0
    for i in range(m, l-1, -1):
        sum = sum+arr[i]
        if (sum>left_sum):
            left_sum = sum
    # Righ_sum
    sum = 0
    for i in range(m+1,h+1):
        sum = sum+arr[i]
        if (sum>right_sum):
            right_sum = sum
    
    return right_sum+left_sum

def max_sum_subarr(arr,l,h):
    if (h==l):
        return arr[h]
    m = (h+l)//2
    return max(max_sum_subarr(arr,l,m),
            max_sum_subarr(arr,m+1,h),
            Global_Sum_subarr(arr,l,m,h))


if __name__ == "__main__":
    a=[-2, 11, -4, 13, -5, 2]
    print(max_sum_subarr(a,0,len(a)-1))
