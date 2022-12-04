import string #used to find position of letter in alphabet

inputFile = open("input.txt", "r")#open input file

inputFile = inputFile.read()#read input file
inputFile = inputFile.split()#split input file into list
runningPrioroty = 0#set running priority to 0

for i in range(len(inputFile)):#for each item in input file
    if i % 3 == 0:#cheaks if on a multipe of 3 becuase elfs are in groups of 3
        bag1 = inputFile[i-3]#gets the contents the first elfs bag
        bag2 = inputFile[i-2]#gets the contents the second elfs bag
        bag3 = inputFile[i-1]#gets the contents the third elfs bag
        bothCompartments = list(set(bag1) & set(bag2) & set(bag3))#get the intersection of the three bags
        overPacked = bothCompartments[0]#I know that there is only one item in the intersection, so I can just get the first item
        if overPacked == overPacked.lower():#Check if the item is lowercase if it is then it has a lower priority than uppercase
             prioroty = (string.ascii_lowercase.index(overPacked)+1)#get the position of the letter in the alphabet
        else:#if it wasnt lowercase then it must be uppercase
            prioroty = (string.ascii_lowercase.index(overPacked.lower()) + 27)#get the position of the letter in the alphabet and add 26 to it to get the priority of the uppercase letter
        print(prioroty)
        runningPrioroty += prioroty#add the priority of the current bag to the running priority

print(runningPrioroty)