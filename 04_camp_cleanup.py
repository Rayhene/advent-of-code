with open('input.txt') as file:
    data = [i for i in file.read().split("\n")]

    result_1 = result_2 = 0
    ranges = []
    for line in data:
        ranges.append(line.replace("-", ",").split(","))

    for element in ranges:
        first_range = range(int(element[0]), int(element[1])+1)
        second_range = range(int(element[2]), int(element[3])+1)

        if first_range.start >= second_range.start and first_range.stop <= second_range.stop or second_range.start >= first_range.start and second_range.stop <= first_range.stop:
            result_1 += 1

        if set(first_range).intersection(set(second_range)):
            result_2 += 1

    #part 1
    print(result_1)

    #part 2
    print(result_2)

  


      


      

            


