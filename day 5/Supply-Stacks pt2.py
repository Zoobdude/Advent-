import re #importing regular expressions for use in parsing the input file

#couldn't be bothered to parse the stacks from the input file so I just hard coded them in
stack1 = ["D", "T", "W", "N", "L"]
stack2 = ["H", "P", "C"]
stack3 = ["J", "M", "G", "D", "N", "H", "P", "W"]
stack4 = ["L", "Q", "T", "N", "S", "W", "C"]
stack5 = ["N", "C", "H", "P"]
stack6 = ["B", "Q", "W", "M", "D", "N", "H", "T"]
stack7 = ["L", "S", "G", "J", "R", "B", "M"]
stack8 = ["T", "R", "B", "V", "G", "W", "N", "Z"]
stack9 = ["L", "P", "N", "D", "G", "W"]
crane = []#the crane is the list that will be used to move the items from one stack to another

inputFile = open("input.txt", "r")
movements = inputFile.read().splitlines()
inputFile.close()

for i in range(len(movements)):#loops through every movement in the input file
    currentMovement = movements[i]
    currentMovementList = re.findall(r'\d+', currentMovement)#in first coloumn it is how many items will be moved, the second coloumn is the stack number to strt from and the third coloumn is the stack number to move to
    amountOfItmesToMove = int(currentMovementList[0])
    stackNumberToStartFrom = int(currentMovementList[1])
    stackNumberToMoveTo = int(currentMovementList[2])

    for j in range(amountOfItmesToMove):#loops through the amount of items to move
        #these if statements are used to determine which stack to remove the items from
        if stackNumberToStartFrom == 1:
            addToOtherList = stack1.pop(0)
            crane.append(addToOtherList)
        elif stackNumberToStartFrom == 2:
            addToOtherList = stack2.pop(0)
            crane.append(addToOtherList)
        elif stackNumberToStartFrom == 3:
            addToOtherList = stack3.pop(0)
            crane.append(addToOtherList)
        elif stackNumberToStartFrom == 4:
            addToOtherList = stack4.pop(0)
            crane.append(addToOtherList)
        elif stackNumberToStartFrom == 5:
            addToOtherList = stack5.pop(0)
            crane.append(addToOtherList)
        elif stackNumberToStartFrom == 6:
            addToOtherList = stack6.pop(0)
            crane.append(addToOtherList)
        elif stackNumberToStartFrom == 7:
            addToOtherList = stack7.pop(0)
            crane.append(addToOtherList)
        elif stackNumberToStartFrom == 8:
            addToOtherList = stack8.pop(0)
            crane.append(addToOtherList)
        elif stackNumberToStartFrom == 9:
            addToOtherList = stack9.pop(0)
            crane.append(addToOtherList)
        addToOtherList = []
        print(crane)
    #these if statements are used to determine which stack to add the items to
    if stackNumberToMoveTo == 1:
        stack1 = crane + stack1
    elif stackNumberToMoveTo == 2:
        stack2 = crane + stack2
    elif stackNumberToMoveTo == 3:
        stack3 = crane + stack3
    elif stackNumberToMoveTo == 4:
        stack4 = crane + stack4
    elif stackNumberToMoveTo == 5:
        stack5 = crane + stack5
    elif stackNumberToMoveTo == 6:
        stack6 = crane + stack6
    elif stackNumberToMoveTo == 7:
        stack7 = crane + stack7
    elif stackNumberToMoveTo == 8:
        stack8 = crane + stack8
    elif stackNumberToMoveTo == 9:
        stack9 = crane + stack9
    crane = []

#output junk
print("Output:")
print(stack1)
print(stack2)
print(stack3)
print(stack4)
print(stack5)
print(stack6)
print(stack7)
print(stack8)
print(stack9)

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