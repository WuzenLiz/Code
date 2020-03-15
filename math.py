import math
def tgt(n):
    a=[]
    for i in range(1,n+1):
        a.append(math.factorial(i))
    for n in a:
        print(n)  
    return len(a),sum(a)

n=20
print(math.factorial(n))
print(tgt(n))