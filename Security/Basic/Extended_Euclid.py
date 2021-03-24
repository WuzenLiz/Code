def Cal_func(x, y):
	if x == 0:
		return (y, 0, 1)
	else:
		gcd, a, b = Cal_func(y % x, x)
		return (gcd, b - (y//x) * a, a)
		
def EuclidE(a,b):
	gcd, x, y = Cal_func(a, b)
	if a<b:
		if x<0:
			return x + b
		else:
			return x
	else:
		if y<0:
			return y + a
		else:
			return y