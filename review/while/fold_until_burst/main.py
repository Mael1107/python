def fold_until_burst(limit):
    count = 1
    while count < limit:
        count *= 2
    return count

print(fold_until_burst(100))

 