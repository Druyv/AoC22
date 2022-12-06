with open("input.txt") as f:
    line = f.read()
 
for i in range(4,len(line)):
    if len(set(line[i-4:i])) == 4:
        print(f'6_1: {i}')
        break
 
for i in range(14,len(line)):
    if len(set(line[i-14:i])) == 14:
        print(f'6_2: {i}')
        break


      