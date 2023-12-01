#rock paper scissors analysis

inputFile  = open("input.txt", "r")
inputFile = inputFile.read().splitlines()
totalScore = 0

def letterConvertPlayer(letter):
    if letter == "X":
        return "rock"
    elif letter == "Y":
        return "paper"
    elif letter == "Z":
        return "scissors"

def letterConvertComputer(letter):
    if letter == "A":
        return "rock"
    elif letter == "B":
        return "paper"
    elif letter == "C":
        return "scissors"

for i in range(len(inputFile)):
    currentLine = inputFile[i].split()
    print(currentLine)
    opponent = letterConvertComputer(currentLine[0])
    print(opponent)
    player = letterConvertPlayer(currentLine[1])
    print(player)
    #base score for choosing rock
    if player == "rock":
        initialScore = 1
    #base score for choosing paper
    if player == "paper":
        initialScore = 2
    #base score for choosing scissors
    if player == "scissors":
        initialScore = 3

    #if opponent chooses rock
    if opponent == "rock":
        if player == "rock":
            score = 3
        elif player == "paper":
            score = 6
        elif player == "scissors":
            score = 0

    #if opponent chooses paper
    if opponent == "paper":
        if player == "rock":
            score = 0
        elif player == "paper":
            score = 3
        elif player == "scissors":
            score = 6

    #if opponent chooses scissors
    if opponent == "scissors":
        if player == "rock":
            score = 6
        elif player == "paper":
            score = 0
        elif player == "scissors":
            score = 3

    totalScore = totalScore + (score + initialScore)

    print(totalScore)

inputFile.close()