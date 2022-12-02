file = open('input.txt')

result = 0;
dict = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
    "win": 6,
    "lose": 0,
    "tie": 3
}

for line in file:
    if(line[2] == 'Y'):
        result += dict[line[0]] + dict['tie']
    elif(line[2] == 'X'):
        result += dict['lose']
        result += 3 if dict[line[0]] == 1 else (1 if dict[line[0]] == 2 else (2 if dict[line[0]] == 3 else 0))
    elif(line[2] == 'Z'):
        result += dict['win']
        result += 2 if dict[line[0]] == 1 else (3 if dict[line[0]] == 2 else (1 if dict[line[0]] == 3 else 0))
print(result)



    
