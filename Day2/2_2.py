with open("input.txt", "r") as f:
    lines = f.readlines()
lines = [(x.split()[0],x.split()[1]) for x in lines]

# X = Rock, Y = Paper, Z = Scissor
rps = {"X":0 , "Y":3 , "Z":6 }
rpso = {"A":1, "B":2, "C":3}
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
    
def get_move(opponent, me):
    if me == 'Y':
        return opponent
    if me == 'Z':
        if opponent == 'A':
            return 'B'
        if opponent == 'B':
            return 'C'
        if opponent == 'C':
            return 'A'
    if me == 'X':
        if opponent == 'C':
            return 'B'
        if opponent == 'B':
            return 'A'
        if opponent == 'A':
            return 'C'

res = [rps[x[1]]+rpso[get_move(x[0],x[1])] for x in lines]
print(res)
print(sum(res))