def canMeasureWater(x, y, z):
    if x > y:
        temp = x
        x = y
        y = temp   
    if z > x + y:
        return False
    queue = [(0, 0)]
    visited = set((0, 0))
    while len(queue) > 0:
        a, b = queue.pop(0)
        if a + b == z:
            return True
        states = set()
        states.add((x, b)) # fill jar x;
        states.add((a, y)) # fill jar y;
        states.add((0, b)) # empty jar x;
        states.add((a, 0)) # empty jar y;
        states.add((min(x, b + a), 0 if b < x - a else b - (x - a))) # pour jar y to x;
        states.add((0 if a + b < y else a - (y - b), min(b + a, y))) # pour jar x to y;
        for state in states:
            if state in visited:
                continue
            queue.append(state)
            visited.add(state)      
    return False

def main():
    x = 3
    y = 5
    z = 4
    print(canMeasureWater(x,y,z))
if __name__ == "__main__":
    main()