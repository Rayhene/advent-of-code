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
    result += dict[line[2]]

    if(dict[line[0]] == dict[line[2]]):
        result += dict["tie"]
    elif(dict[line[2]] - dict[line[0]] == -1 or dict[line[2]] - dict[line[0]] == 2):
        result += dict["lose"]
    else:
        result += dict["win"]

print(result)
