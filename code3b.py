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
count = 0
current_group = []

for _ in rucksacks[:]:
    current_group.append(_)  # append elf
    count += 1  # inc counter
    if count % 3 == 0:
        # count mod 3 is zero => a group of three has been collected
        # DEBUG: print("Processed group of three:")
        # DEBUG: print(current_group)
        # loop over three entities to find first char
        # that is present in each
        for c in current_group[0]:
            if c in current_group[1]:
                if c in current_group[2]:
                    match = c
                    # DEBUG: print(c)
                    # calculate and add priority score of
                    # match:
                    for i, a in enumerate(alpha):
                        if match == a:
                            priority = i + 1
                            sum += priority
                            # DEBUG: print(priority)
                    break  # found match, added score; break loop

        # reset counter/content:
        current_group = []
        count = 0

print(sum)

# correct answer, first try: 2738
