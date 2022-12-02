file = open('input.txt')
calories = []
aux = 0
    
for line in file:
    if(line != "\n"):
        aux += int(line)
    else:
        calories.append(aux)
        aux = 0

calories.sort(reverse = True)

#part 1       
print(calories[-1])

#part 2
print(sum(calories[0:3]))

    
    


