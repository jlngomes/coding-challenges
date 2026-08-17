def move_zeros(lst):
    array_index = []
    for number in range(len(lst)):
        if lst[number] == 0:
            array_index.append(number)

    cont = 0
    for index in array_index:
        lst.pop(index - cont)
        lst.append(0)
        cont += 1

    return lst

print(move_zeros(lst=[9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

# Result: [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
