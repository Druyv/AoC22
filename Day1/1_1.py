puzzle = 2

if puzzle == 1:
    print(max([sum([int(x) for x in y]) for y in [i.split() for i in ' '.join(open("input.txt",'r').readlines()).split('\n')]]))

if puzzle == 2:
    print(sum(sorted([sum([int(x) for x in y]) for y in [i.split() for i in ' '.join(open("input.txt",'r').readlines()).split('\n')]])[-3:]))
        