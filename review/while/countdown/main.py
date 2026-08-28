def countdown(start):
    count = 0
    counters  = []

    while count < start:
        c = start - count
        counters.append(c)
        count += 1

    return counters

print(countdown(11))