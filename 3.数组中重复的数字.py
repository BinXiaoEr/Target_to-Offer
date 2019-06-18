def duplicate(numbers, length):
    new_numbers = []
    for i in range(length):
        if numbers[i] not in new_numbers:
            new_numbers.append(numbers[i])
            continue
        print(numbers[i])
duplicate([2,3,1,0,2,5,3],7)

def duplicate2(numbers, length):
    numbers.sort()
    i = 0
    while i < length - 1:
        if numbers[i] == numbers[i + 1]:
            print(numbers[i])
            i += 2
            continue
        i += 1
duplicate2([2,3,1,0,2,5,3],7)

def duplicate3(numbers, length):
    for i in range(length):
        while (numbers[i] != i):
            if numbers[i] == numbers[numbers[i]]:
                print(numbers[i])
                break
            else:
                numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
duplicate3([2, 3, 1, 0, 2, 5, 3], 7)
