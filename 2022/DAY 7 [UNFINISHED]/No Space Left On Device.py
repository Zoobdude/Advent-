import re

inputFile = open("input.txt", "r")
consoleOutput = inputFile.read().splitlines()
inputFile.close()

outputFile = open("output2.txt", "w")

folderSize = 0
currentDirectory = ""

for i in range(0, len(consoleOutput)):
    currentLine = consoleOutput[i]#tempporarily stores the current line
    isItAFile = currentLine[0].isnumeric()#this is to check if the first character is a number
    if isItAFile == True:
        #outputFile.write("  " + currentLine + "\n")
        fileSize = re.findall(r'\d+', currentLine)[0]#this finds all the numbers in the line
        folderSize += int(fileSize)


    if currentLine[0] == "$":
        currentLine = currentLine[2:]#this removes the "$ " from the beginning of the line
        if currentLine[0] == "l":#this means it will be the "ls" (list) command
            expectOutputNext = True
        if currentLine[0] == "c":#this means it will be the "cd" (change directory) command
            currentLine = currentLine[3:]#this removes the "cd " from the beginning of the line
            if currentLine == "..":#this means it will remove the last directory from the path
                currentDirectory = currentDirectory[0:currentDirectory.rfind("/")]
                outputFile.write("\n folderSize " + str(folderSize) + "\n")
                folderSize = 0
                outputFile.write("\n \n" + currentDirectory + "\n \n")
            else:#this means it will add the directory to the path
                currentDirectory += ("/" + currentLine)
                outputFile.write("\n folderSize " + str(folderSize) + "\n")
                folderSize = 0
                outputFile.write("\n \n" + currentDirectory + "\n \n")

outputFile.write("\n FolderSize " + str(folderSize) + "\n")

outputFile.close()
