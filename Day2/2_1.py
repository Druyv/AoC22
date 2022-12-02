with open("input.txt", "r") as f:
    lines = f.readlines()
lines = [(x.split()[0],x.split()[1]) for x in lines]

# X = Rock, Y = Paper, Z = Scissor
rps = {"X":1 , "Y":2 , "Z":3 }
def score_for_round(opponent, me):
    if ord(opponent) == ord(me)-23:
        return 3 # tie
    if opponent == 'A':
        if me == 'Y':
            return 6
    elif opponent == 'B':
        if me == 'Z':
            return 6
    elif opponent == 'C':
        if me == 'X':
            return 6
    return 0

res = [score_for_round(x[0],x[1])+rps[x[1]] for x in lines]
print(res)
print(sum(res))