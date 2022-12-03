with open("input.txt") as f:
    lines = f.readlines()

def convert_to_priority(item):
    return (ord(item)-ord('a')+1) if item.islower() else (ord(item)-ord('A')+27)

res = [] 
for line in lines:
    n = len(line)
    s1 = slice(0,n//2)
    s2 = slice(n//2,n)
    res.append(convert_to_priority(list(set(line[s1])&set(line[s2]))[0]))
print(sum(res))
    