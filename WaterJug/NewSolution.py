from collections import defaultdict as pdict
Solution_Path = pdict(list)
def canMeasureWater(x: int, y: int, z: int) -> bool:
    dict_index=0
    big, small = max(x, y), min(x, y)
    if z > big + small or z < 0 or small < 0:
        return False
    if z == 0 or z == big + small:
        return True
        Solution_Path[dict_index].append({x,y})
    if small == 0:
        return z == big
    gcd(big, small)
    return z % gcd == 0
    
def gcd(cls, x, y) -> int:
    while True:
        if x % y == 0:
            return y
        else:
            x, y = y, x % y
    
if __name__ == "__main__":
    x,y,z=4,3,2
    canMeasureWater(x,y,z)
    print(Solution_Path)