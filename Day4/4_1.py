with open("input.txt") as f:
    lines = f.readlines()

split = [pair.strip().split(',') for pair in lines]
split = [[pair[0].split('-'),pair[1].split('-')] for pair in split]
print(split)
ranges = [(list(range(int(x[0][0]),int(x[0][-1])+1)), list(range(int(x[1][0]),int(x[1][-1])+1))) for x in split]
print(ranges)

sum = 0
for pair in ranges:
    if all(x in pair[1] for x in pair[0]) or all(x in pair[0] for x in pair[1]):
        sum +=1
        
print(sum)