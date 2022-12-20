import data3
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# rucksacks = [
#     'vJrwpWtwJgWrhcsFMMfFFhFp',
#     'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#     'PmmdzqPrVvPwwTWBwg',
#     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#     'ttgJtRGJQctTZtZT',
#     'CrZsJsPPZsGzwwsLwLmpwMDw'
# ]

rucksacks = data3.rucksacks

match = ''
priority = 0
sum = 0
for _ in rucksacks:
    length = len(_)
    half = int(length / 2)
    # print(_[half])
    first = _[:half]
    second = _[half:]
    # print(second)
    for c in first:
        if c in second:
            match = c
            print(c)
            break  # match, break loop
    for i, a in enumerate(alpha):
        #print(i + 1, a)
        if match == a:
            priority = i + 1
            sum += priority
print(sum)

# correct, first try: 8109
