print(f'1: {max([sum([int(x) for x in y]) for y in [i.split() for i in " ".join(open("input.txt","r").readlines()).split("\n")]]))}')
print(f'2: {sum(sorted([sum([int(x) for x in y]) for y in [i.split() for i in " ".join(open("input.txt","r").readlines()).split("\n")]])[-3:]))}')
        