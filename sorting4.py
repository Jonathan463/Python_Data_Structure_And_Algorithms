def sorting4(numbers):
    numbers_copy = numbers[:]
    for i in range(len(numbers)):
        max_index = i
        for j in range(i+1, len(numbers)):
            if numbers_copy[j] > numbers_copy[i]:
                max_index = j
        numbers_copy[i],numbers_copy[max_index] = numbers_copy[max_index],numbers_copy[i]
    return numbers_copy
