#with open("input.txt") as f:
#    lines = f.readlines()

z = lambda x: (ord(x)-ord('a')+1) if x.islower() else (ord(x)-ord('A')+27)
    
lines = [open("input.txt").readlines()[i:i+3] for i in range(0, len(open("input.txt").readlines()), 3)]

res = [] 
for line in lines:
    e1 = set(line[0].replace('\n',''))
    e2 = set(line[1].replace('\n',''))
    e3 = set(line[2].replace('\n',''))
    
    set1 = e1.intersection(e2)
    set2 = set1.intersection(e3)
    final = list(set2)
    res.append(z(final[0]))
print(sum(res))
    