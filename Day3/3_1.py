print(sum([(lambda x:(ord(x)-ord('a')+1) if x.islower() else (ord(x)-ord('A')+27))(list(set(line[slice(0,len(line)//2)])&set(line[slice(len(line)//2,len(line))]))[0]) for line in open("input.txt").readlines()])) 