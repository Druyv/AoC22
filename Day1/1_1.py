puzzle = 2

with open("input.txt", "r") as f:
    lines = f.readlines()

    elves = []
    res = 0
    for line in lines:
        if line != '\n':
            res+=int(line)
        else:
            elves.append(res)
            res = 0

    if puzzle == 1:
        print(max(elves))

    if puzzle == 2:
        total = 0
        for _ in range(3):
            total += max(elves)
            elves.remove(max(elves))
        print(total)
        