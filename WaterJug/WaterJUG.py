class waterjug:
    def __init__(self,j1m,j2m,j1,j2,target):
        super().__init__()
        self.jug1_max = j1m
        self.jug2_max = j2m
        self.jug1     = j1
        self.jug2     = j2
        self.fill     = target
    
    def j1_is_max(self):
        self.jug1 = self.jug1_max
    def j2_is_max(self):
        self.jug2 = self.jug2_max
    
    def Empty_Jug1(self):
        self.jug1 = 0
    def Empty_Jug2(self):
        self.jug2 = 0  

    def waterjug_solution(self,jug1,jug2):
        print("%d\t%d" % (jug1, jug2))
        if jug2 is self.fill:
            return
        elif jug2 is self.jug2_max:
            self.waterjug_solution(0, jug1)
        elif jug1 != 0 and jug2 == 0:
            self.waterjug_solution(0, jug1)
        elif jug1 is self.fill:
            self.waterjug_solution(jug1, 0)
        elif jug1 < self.jug1_max:
            self.waterjug_solution(self.jug1_max, jug2)
        elif jug1 < (self.jug2_max-jug2):
            self.waterjug_solution(0, (jug1+jug2))
        else:
            self.waterjug_solution(jug1-(self.jug2_max-jug2), (self.jug2_max-jug2)+jug2)
def check(a, b):
	if a == 0:
		return b
	return check(b%a, a)
def main():
    jug1    = int(input("Nhập thể tích bình 1: "))
    jug2    = int(input("Nhập thể tích bình 2: "))
    target  = int(input("Nhập mục tiêu cần đạt: "))
    w = waterjug(jug1,jug2,0,0,target)
    if target % check(jug1,jug2) == 0:
        print("Bình 1\tBình 2")
        w.waterjug_solution(0,0)
    else:
        print("Không thể thực hiện!")

if __name__ == "__main__":
    main()