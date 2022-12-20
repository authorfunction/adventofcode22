import data1

elves = data1.elves
currentelf = 0
highscore = 0
individuals = 0
score_board = []

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
        # save elf's calories to score_board
        score_board.append(currentelf)
        # reset current calorie counter,
        currentelf = 0
        # then go on to the
        # next elf counter...

# print results
print("---")
print(highscore)
print(individuals)
print(len(score_board))
print(score_board[-3:])
score_board.sort()
print(score_board[-3:])
# answer:
print(sum(score_board[-3:]))
