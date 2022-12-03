import string

with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

    alphabet = dict(zip(string.ascii_lowercase, (i for i in range(1, 27))))
    alphabet.update(dict(zip(string.ascii_uppercase, (i for i in range(27, 53)))))

    result_1 = 0
    for items in data:
        first_half  = items[:len(items)//2]
        second_half = items[len(items)//2:]

        flag = False; 

        for letter in first_half:
            if letter in second_half and not flag:
                flag=True
                result_1 += alphabet[letter]
        flag=False

#part 1 result
print(result_1)

def data_chunks(data):
    for i in range(0, len(data), 3):
        yield data[i:i + 3]

chunks = list(data_chunks(data))

result_2 = 0
for chunk in chunks:

    for character in chunk[0]:
        if(character in chunk[1] and character in chunk[2]):   
            result_2 += alphabet[character]
            break

#part 2 result
print(result_2)



   








