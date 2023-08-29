#Euclidean Extended
egcd = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or egcd(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
#Euclidean
gcd = lambda a,b: gcd(b, a % b) if b else a 
#for clear console
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

print(egcd(3,11))