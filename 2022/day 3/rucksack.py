import string #used to find position of letter in alphabet

inputFile = open("input.txt", "r")#open input file

inputFile = inputFile.read()#read input file
inputFile = inputFile.split()#split input file into list
runningPrioroty = 0#set running priority to 0

for i in range(len(inputFile)):#for each item in input file
    currentLine = inputFile[i]#set current line to current bag in the list
    lineLength = len(currentLine)#get length of current line
    lineLength = int(lineLength / 2)#get half of the length of the line so that we can get the number of items in each compartment
    compartment1 = currentLine[0:lineLength]#get first compartment
    compartment2 = currentLine[lineLength:]#get second compartment
    bothCompartments = list(set(compartment1) & set(compartment2))#get the intersection of the two compartments
    overPacked = bothCompartments[0]#I know that there is only one item in the intersection, so I can just get the first item
    if overPacked == overPacked.lower():#Check if the item is lowercase if it is then it has a lower priority than uppercase
       prioroty = (string.ascii_lowercase.index(overPacked)+1)#get the position of the letter in the alphabet
    else:#if it wasnt lowercase then it must be uppercase
        prioroty = (string.ascii_lowercase.index(overPacked.lower()) + 27)#get the position of the letter in the alphabet and add 26 to it to get the priority of the uppercase letter
    print(prioroty)
    runningPrioroty += prioroty#add the priority of the current bag to the running priority

print(runningPrioroty)