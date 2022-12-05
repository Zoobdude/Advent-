import re #importing regular expressions to parse the input file

#couldn't be bothered to parse the input file so I wrote the stacks into the code
stack1 = ["D", "T", "W", "N", "L"]
stack2 = ["H", "P", "C"]
stack3 = ["J", "M", "G", "D", "N", "H", "P", "W"]
stack4 = ["L", "Q", "T", "N", "S", "W", "C"]
stack5 = ["N", "C", "H", "P"]
stack6 = ["B", "Q", "W", "M", "D", "N", "H", "T"]
stack7 = ["L", "S", "G", "J", "R", "B", "M"]
stack8 = ["T", "R", "B", "V", "G", "W", "N", "Z"]
stack9 = ["L", "P", "N", "D", "G", "W"]

inputFile = open("input.txt", "r")
movements = inputFile.read().splitlines()
inputFile.close()

for i in range(len(movements)):#loops for each line in the input file (each line is a movement)
    currentMovement = movements[i]
    currentMovementList = re.findall(r'\d+', currentMovement)#in first coloumn it is how many items will be moved, the second coloumn is the stack number to strt from and the third coloumn is the stack number to move to
    amountOfItmesToMove = int(currentMovementList[0])
    stackNumberToStartFrom = int(currentMovementList[1])
    stackNumberToMoveTo = int(currentMovementList[2])

    for j in range(amountOfItmesToMove):#loops for each item to be moved
        #checks which stack to start from and moves the item to a temporary variable
        if stackNumberToStartFrom == 1:
            addToOtherList = stack1.pop(0)
            print(addToOtherList)
        elif stackNumberToStartFrom == 2:
            addToOtherList = stack2.pop(0)
            print(addToOtherList)
        elif stackNumberToStartFrom == 3:
            addToOtherList = stack3.pop(0)
            print(addToOtherList)
        elif stackNumberToStartFrom == 4: 
            addToOtherList = stack4.pop(0)
            print(addToOtherList)
        elif stackNumberToStartFrom == 5:
            addToOtherList = stack5.pop(0)
            print(addToOtherList)
        elif stackNumberToStartFrom == 6:
            addToOtherList = stack6.pop(0)
            print(addToOtherList)
        elif stackNumberToStartFrom == 7:
            addToOtherList = stack7.pop(0)
            print(addToOtherList)
        elif stackNumberToStartFrom == 8:
            addToOtherList = stack8.pop(0)
            print(addToOtherList)
        elif stackNumberToStartFrom == 9:
            addToOtherList = stack9.pop(0)
            print(addToOtherList)

        #checks which stack to move to and moves the item to that stack
        if stackNumberToMoveTo == 1:
            stack1.insert(0, addToOtherList)
        elif stackNumberToMoveTo == 2:
            stack2.insert(0, addToOtherList)
        elif stackNumberToMoveTo == 3:
            stack3.insert(0, addToOtherList)
        elif stackNumberToMoveTo == 4:
            stack4.insert(0, addToOtherList)
        elif stackNumberToMoveTo == 5:
            stack5.insert(0, addToOtherList)
        elif stackNumberToMoveTo == 6:
            stack6.insert(0, addToOtherList)
        elif stackNumberToMoveTo == 7:
            stack7.insert(0, addToOtherList)
        elif stackNumberToMoveTo == 8:
            stack8.insert(0, addToOtherList)
        elif stackNumberToMoveTo == 9:
            stack9.insert(0, addToOtherList)

#outputs the stacks to a file
outputFile = open("output.txt", "w")
outputFile.write(str(stack1) + "\n")
outputFile.write(str(stack2) + "\n")
outputFile.write(str(stack3) + "\n")
outputFile.write(str(stack4) + "\n")
outputFile.write(str(stack5) + "\n")
outputFile.write(str(stack6) + "\n")
outputFile.write(str(stack7) + "\n")
outputFile.write(str(stack8) + "\n")
outputFile.write(str(stack9) + "\n")
outputFile.close()
    


