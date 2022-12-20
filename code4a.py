# set((range(3,7))).issubset(range(2,8))
#
# range(data4.pairs[0][1][0],data4.pairs[0][1][1])
import data4

# example, I get correct answers visavi this...
# pairs = [
#     [[2, 4], [6, 8]],
#     [[2, 3], [4, 5]],
#     [[5, 7], [7, 9]],
#     [[2, 8], [3, 7]],  # subset
#     [[6, 6], [4, 6]],  # subset
#     [[2, 6], [4, 8]],
# ]

pairs = data4.pairs
count = 0
edge = 0


def log_result(row, pair, range1, range2):
    print(f"row:{row}, pair:{pair},", end="")
    print(f" lengths: {len(range1)} {len(range2)}", end="")


def check_for_subsets(count, edge, row, pair, range1, range2):
    if len(range1) >= len(range2):  # if 2 fits in 1 (>=)
        if set(range2).issubset(range1):
            #log_result(row, pair, range1, range2)
            #print(" => second is a subset of first", end="")
            # print("")
            count += 1
            # break
    elif len(range2) >= len(range1):  # if 1 fits in 2 (>=)
        if set(range1).issubset(range2):
            #log_result(row, pair, range1, range2)
            #print(" => first is a subset of second", end="")
            # print("")
            count += 1
    else:  # some edge condition?
        log_result(row, pair, range1, range2)
        if set(range1).issubset(range2):
            print(" 1 is sub of 2 ")
        elif set(range2).issubset(range1):
            print(" 2 is sub of 1 ")
        print("")
        edge += 1

    return count, edge, row


# MAIN LOOP
for row, pair in enumerate(pairs[:]):
    range1 = range(pair[0][0], pair[0][1])
    # print(range1)
    range2 = range(pair[1][0], pair[1][1])
    # print(range2)

    count, edge, row = check_for_subsets(
        count, edge, row, pair, range1, range2)

print(f"count: {count}")
print(f"edge conditions detected: {edge}")
print(f"edge+count: {edge+count}")
