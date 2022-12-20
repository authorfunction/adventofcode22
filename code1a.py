import data1

elves = data1.elves
currentelf = 0
highscore = 0
individuals = 0

for i, value in enumerate(elves):
    # only add integers:
    if type(value) is int:
        currentelf += value
    # str indicates we have a new elf:
    elif type(value) is str:
        individuals += 1
        print("this elf("
              + str(individuals)
              + "):"
              + str(currentelf)
              + "")
        if currentelf > highscore:
            highscore = currentelf
            print("new highscore: "
                  + str(highscore))

        # reset current calorie counter,
        currentelf = 0
        # then go on to the
        # next elf counter...

# print results
print("---")
print(highscore)
print(individuals)
