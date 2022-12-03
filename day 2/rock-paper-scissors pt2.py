#rock paper scissors analysis

inputFile  = open("input.txt", "r")
inputFile = inputFile.read().splitlines()
totalScore = 0

def letterConvertPlayer(letter):
    if letter == "X":
        return "loose"
    elif letter == "Y":
        return "draw"
    elif letter == "Z":
        return "win"

def letterConvertPlayerOld(letter):
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
    playerPick = letterConvertPlayerOld(currentLine[1])
    print(playerPick)
    print(player)
    #base score for choosing rock
    if playerPick == "rock":
        initialScore = 1
    #base score for choosing paper
    if playerPick == "paper":
        initialScore = 2
    #base score for choosing scissors
    if playerPick == "scissors":
        initialScore = 3
    print(initialScore)

    #if opponent chooses rock
    if opponent == "rock":
        if player == "draw":
            score = 3
        elif player == "win":
            score = 6
        elif player == "loose":
            score = 0

    #if opponent chooses paper
    if opponent == "paper":
        if player == "loose":
            score = 0
        elif player == "draw":
            score = 3
        elif player == "win":
            score = 6

    #if opponent chooses scissors
    if opponent == "scissors":
        if player == "win":
            score = 6
        elif player == "loose":
            score = 0
        elif player == "draw":
            score = 3

    totalScore = totalScore + (score + initialScore)

    print(totalScore)
