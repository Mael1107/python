# def biggest_value(*numbers):
#     return max(numbers)

# print(biggest_value(10, 20, 30))


def biggest_value(*numbers):
    biggest = numbers[0]

    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest

print(biggest_value(10, 20, 30))