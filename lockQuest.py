import itertools

def guessables(num):
    guesses = []
    for p in itertools.permutations(range(0,10),num):
        if p[0] != 0:
            guesses.append(''.join(map(str, p))) 
    return guesses

def convert(list): 
    s = [str(i) for i in list] 
    res = int("".join(s))     
    return(res) 

def zen(lt):
    relt = []
    for p in lt:
        e = [int(d) for d in str(p)]
        e.sort()
        relt.append(convert(e))
    return relt


q = guessables(9)
p = zen(q)
p.sort()
new_p = list(p for p,_ in itertools.groupby(p))
print(new_p,"\n",len(new_p))
