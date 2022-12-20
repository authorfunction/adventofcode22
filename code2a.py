import data2

# example:
# game = [
#     ['A', 'Y'],  # Y=B
#     ['B', 'X'],  # X=A
#     ['C', 'Z']  # Z=C
# ]

game = data2.game

# clean up data for easier cmp:
for i, pair in enumerate(game):
    if pair[1] == 'Y':
        game[i][1] = 'B'
    elif pair[1] == 'X':
        game[i][1] = 'A'
    elif pair[1] == 'Z':
        game[i][1] = 'C'

score = 0
total = 0
round = 0
print(game[:10])
for i, pair in enumerate(game[:]):
    # round starts
    round += 1
    # check for draw:
    if pair[0] == pair[1]:
        #draw +3
        score += 3
        print("draw! ", end="")
    # not a draw, check for win conditions:
    elif pair[0] == 'A':  # opponent has rock
        if pair[1] == 'B':  # paper=>win
            score += 6
            print("win! ", end="")
        elif pair[1] == 'C':  # scissors=>loss
            score += 0
            print("loss! ", end="")
    elif pair[0] == 'B':  # oppondet has paper
        if pair[1] == 'A':  # rock=>loss
            score += 0
            print("loss! ", end="")
        elif pair[1] == 'C':  # scissors=>win
            score += 6
            print("win! ", end="")
    elif pair[0] == 'C':  # oppondet has scissors
        if pair[1] == 'A':  # rock=>win
            score += 6
            print("win! ", end="")
        elif pair[1] == 'B':  # paper=>loss
            score += 0
            print("loss! ", end="")
    else:
        print("error 0!")

    # add hand score
    if pair[1] == 'A':
        #rock +1
        score += 1
    elif pair[1] == 'B':
        #paper +2
        score += 2
    elif pair[1] == 'C':
        #scissors +3
        score += 3
    else:
        print("error 1!")

    print("round " 
          + str(round) 
          + ", score: " 
          + str(score))
    total += score
    score = 0
print("Total: " 
      + str(total))


# felresultat 1: 11325
# correct answer: 11475
