#with open("input.txt") as f:
#    lines = f.readlines()

#(lambda x:(ord(x)-ord('a')+1) if x.islower() else (ord(x)-ord('A')+27))

print(sum([(lambda x:(ord(x)-ord('a')+1) if x.islower() else (ord(x)-ord('A')+27))(list(set(line[slice(0,len(line)//2)])&set(line[slice(len(line)//2,len(line))]))[0]) for line in open("input.txt").readlines()])) 
#for line in lines:
#    n = len(line)
#    s1 = slice(0,n//2)
#    s2 = slice(n//2,n)
#    res.append(convert_to_priority(list(set(line[s1])&set(line[s2]))[0]))
#print(sum(res))
    